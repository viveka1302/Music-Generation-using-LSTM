import os
import music21

MIDI_FILES_PATH = 'midi_songs_piano/'

def load_songs_in_midi(data_path):
    songs = []
    for path , subdirs , files in os.walk(data_path):
        for file in files:
            song = music21.converter.parse(os.path.join(path,file)) 
            songs.append(song)
    return songs                       

def preprocess(data_path):
    print('Loading Songs')
    songs = load_songs_in_midi(MIDI_FILES_PATH)
    print(f'Loaded {len(songs)} songs')

if __name__ == '__main__':
    music21.configure.run()
    songs = load_songs_in_midi(MIDI_FILES_PATH)
    print(f'Loaded {len(songs)} songs')
    song = songs[0]
    song.show()