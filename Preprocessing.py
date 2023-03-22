import os
import music21
class Preprocessing:
    def __init__(self, MIDI_FILES_PATH):
        self.MIDI_FILES_PATH = MIDI_FILES_PATH

    def load_songs_in_midi(self):
        songs = []
        for path , subdirs , files in os.walk(self.MIDI_FILES_PATH):
            for file in files:
                song = music21.converter.parse(os.path.join(path,file)) 
                songs.append(song)
        return songs                       

    def preprocess(self):
        print('Loading Songs')
        songs = self.load_songs_in_midi(self.MIDI_FILES_PATH)
        print(f'Loaded {len(songs)} songs')

    