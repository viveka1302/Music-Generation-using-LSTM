from Preprocessing import Preprocessing as pp
#from NNTrain import NNTrain
from GRU_Model import GRU_Model
from MelodyGenerator import MelodyGenerator
import numpy as np

class ProjectRun:
    if __name__ == '__main__':
            prep= pp('midi_songs_piano/')
            songs = prep.load_songs_in_midi()
            print(f'Loaded {len(songs)} songs')            
            # try:
            #     x=0                
            #     perfFiles=[]
            #     i= list(x for x in range(0,92) if x not in [3,4,5,6,7,12,23])
            #     for z in i:
            #         song = songs[z]
            #         transposed_song = prep.transposed(song)
            #         print(z)
            #         perfFiles.append(songs[z])
            #     prep.preprocess(perfffy= perfFiles)
            # except Exception as e:
            #     print("failed on ")
           # transposed_song = prep.transposed(songs[0])
           # transposed_song.show()
            # new_songs = prep.create_single_line_dataset()
            # prep.create_mapping(new_songs)
            inputs , targets = prep.generate_training_sequences()
            print(f'There are {len(inputs)} sequences')

            # nn = NNTrain(inputs,targets)
            # nn.train()

            # gru = GRU_Model(inputs,targets)
            # gru.train()
            mg = MelodyGenerator('model_gru.h5')
            seed = '55 _ _ 60 _ _ 65 _ _ 57 _ _ r'
            melody = mg.generate_melody(seed,400,64,0.3)
            print(melody)
            mg.save_melody(melody)

