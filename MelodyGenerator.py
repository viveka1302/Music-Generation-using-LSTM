import tensorflow.keras as keras
import json
import numpy as np
import music21 as m21

class MelodyGenerator:
    
    def __init__(self,model_path):

        self.model_path = model_path
        self.model = keras.models.load_model(model_path)
        self.step_duration = 0.25

        with open('Mapping.json','r') as fp:
            self._mappings = json.load(fp)

        self._start_symbols = ['/']*64

    def generate_melody(self,seed,num_steps,max_sequence_length,temperature):
        seed = seed.split()
        melody = seed
        seed = self._start_symbols + seed
        seed = [self._mappings[symbol] for symbol in seed]

        for _ in range(num_steps):
            seed = seed[-max_sequence_length:]
            onehot_seed = keras.utils.to_categorical(seed,num_classes=len(self._mappings))
            onehot_seed = onehot_seed[np.newaxis,...]
            probabilities = self.model.predict(onehot_seed)[0]
            output_int = self._sample_with_temperature(probabilities,temperature)
            seed.append(output_int)
            output_symbol = [keys for keys,value in self._mappings.items() if value==output_int][0]

            if output_symbol == '/':
                break

            melody.append(output_symbol)
        return melody


    def _sample_with_temperature(self,probabilities,temperature):
        predictions = np.log(probabilities)/temperature
        probabilites = np.exp(predictions)/np.sum(np.exp(predictions))
        choices = range(len(probabilites))
        index = np.random.choice(choices,p=probabilites)
        return index
    
    def save_melody(self,melody,format='midi',file_name='output2.midi'):

        stream = m21.stream.Stream()
        start_symbol = None
        step_counter = 1 

        for index,symbol in enumerate(melody):
            if symbol!='_' or index+1==len(melody):
                if start_symbol is not None:
                    quater_length_duration = self.step_duration * step_counter
                    if start_symbol=='r':
                        m21_event = m21.note.Rest(quarterLength=quater_length_duration)
                    else:
                        m21_event = m21.note.Note(int(start_symbol), quarterLength=quater_length_duration)
                    stream.append(m21_event)
                    step_counter=1
                start_symbol = symbol
            else:
                step_counter+=1
        
        stream.write(format,file_name)

