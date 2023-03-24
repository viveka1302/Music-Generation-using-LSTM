import os
from Preprocessing import Preprocessing as pp
class ProjectRun:
    if __name__ == '__main__':
            prep= pp('midi_songs_piano/')
            songs = prep.load_songs_in_midi()
            print(f'Loaded {len(songs)} songs')


            
            try:
                #prep.preprocess()
                x=0
                
                perfFiles=[]
                i= list(x for x in range(0,92) if x not in [3,4,5,6,7,12,23])
                for z in i:

                    song = songs[z]
                    transposed_song = prep.transposed(song)
                    print(z)
                    perfFiles.append(songs[z])
                    
            #song.show()
                prep.preprocess(perfffy= perfFiles)
                
                #transposed_song = prep.transposed(song)
            #transposed_song.show()
            except Exception as e:
                print("failed on ")