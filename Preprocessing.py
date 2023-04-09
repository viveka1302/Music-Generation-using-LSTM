import os
import json
import music21
import numpy as np
from tensorflow import keras

class Preprocessing:

    def __init__(self, MIDI_FILES_PATH):
        self.MIDI_FILES_PATH = MIDI_FILES_PATH
        self.TIME_STEP = 0.25
        self.SEQUENCE_LENGTH = 64

    def load_songs_in_midi(self):
        songs = []
        for path , _ , files in os.walk(self.MIDI_FILES_PATH):
            for file in files:
                song = music21.converter.parse(os.path.join(path,file)) 
                songs.append(song)
        return songs 
                  
    def transposed(self,song):
        #Get Key
        parts = song.getElementsByClass(music21.stream.Part)
        measures_part0 = parts[0].getElementsByClass(music21.stream.Measure)
        key = measures_part0[0][3]
        #Estimate key
        if  not isinstance(key,music21.key.Key): 
            key = song.analyze('key')
        #Get interval for transposition
        if key.mode == 'major':
            interval = music21.interval.Interval(key.tonic, music21.pitch.Pitch('C'))
        elif key.mode == 'minor':
            interval = music21.interval.Interval(key.tonic, music21.pitch.Pitch('A'))
        #Transpose song by calculated interval 
        transposed_song = song.transpose(interval)
        return transposed_song
    
    def encode_song(self,song):
        encoded_song = []
        symbol='_'
        for event in song.flat.notesAndRests:
            if isinstance(event, music21.note.Note):
                symbol = event.pitch.midi
            elif isinstance(event, music21.note.Rest):
                symbol='r'
            steps = int(event.duration.quarterLength / self.TIME_STEP)
            for step in range(steps):
                if step == 0:
                    encoded_song.append(symbol)
                else:
                    encoded_song.append('_')
        encoded_song = ' '.join(map(str,encoded_song))
        return encoded_song
    
    def preprocess(self, perfffy):
        #songs = self.load_songs_in_midi()
        songs= perfffy
        for i , song in enumerate(songs):
            transposed_song = self.transposed(song)
            encoded_song = self.encode_song(transposed_song)
            save_path = os.path.join('Time_Series_Dataset',str(i))
            with open(save_path,'w') as fp:
                fp.write(encoded_song)

    def load(self,file_path):
        with open(file_path,'r') as fp:
            song = fp.read()
        return song

    def create_single_line_dataset(self):
        new_song_delimiter = ' / '*self.SEQUENCE_LENGTH
        songs=''
        for path , _ , files in os.walk('Time_Series_Dataset'):
            for file in files:
                file_path = os.path.join(path,file)
                song = self.load(file_path)
                songs = songs + song + " " + new_song_delimiter
        songs = songs[:-1]
        with open('Songs_Dataset','w') as fp:
            fp.write(songs)
        return songs 

    def create_mapping(self,songs):
        mapping = {}
        songs = songs.split()
        vocabulary = list(set(songs))
        for i , symbol in enumerate(vocabulary):
            mapping[symbol]=i
        with open('Mapping.json','w') as fp:
            json.dump(mapping,fp,indent=4)

    def convert_songs_to_int(self,songs):
        int_songs = []
        with open('Mapping.json','r') as fp:
            mapping = json.load(fp)
        songs = songs.split()
        for symbol in songs:
            int_songs.append(mapping[symbol])
        return int_songs
    
    def generate_training_sequences(self):
        songs = self.load('Songs_Dataset')
        int_songs = self.convert_songs_to_int(songs)
        inputs = []
        targets = []
        num_sequences = len(int_songs)-self.SEQUENCE_LENGTH
        for i in range(num_sequences):
            inputs.append(int_songs[i:i+self.SEQUENCE_LENGTH])
            targets.append(int_songs[i+self.SEQUENCE_LENGTH])
        vocabulary_size = len(set(int_songs))
        inputs = keras.utils.to_categorical(inputs , num_classes=vocabulary_size)
        targets = np.array(targets)
        return inputs,targets


                

    