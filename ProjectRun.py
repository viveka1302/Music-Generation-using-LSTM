from Preprocessing import Preprocessing as pp
from NNTrain import NNTrain

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
            #transposed_song = prep.transposed(songs[0])
           # transposed_song.show()
            # new_songs = prep.create_single_line_dataset()
            # prep.create_mapping(new_songs)
            inputs , targets = prep.generate_training_sequences()
            print(f'There are {len(inputs)} sequences')

            nn = NNTrain(inputs,targets)
            nn.train()
