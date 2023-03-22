import music21
from Preprocessing import Preprocessing as pp
class ProjectRun:
    if __name__ == '__main__':
            music21.configure.run()
            prep= pp('midi_songs_piano/')
            songs= prep.load_songs_in_midi()
            print(f'Loaded {len(songs)} songs')
            song = songs[0]
            song.show()