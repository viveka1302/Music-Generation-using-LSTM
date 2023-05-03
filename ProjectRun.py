from Preprocessing import Preprocessing as pp
#from NNTrain import NNTrain
from GRU_Model import GRU_Model
from MelodyGenerator import MelodyGenerator
import numpy as np
import random
import streamlit as st
import time

class ProjectRun:
    if __name__ == '__main__':
            # prep= pp('midi_songs_piano/')
            # songs = prep.load_songs_in_midi()
            # print(f'Loaded {len(songs)} songs')            
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
            # inputs , targets = prep.generate_training_sequences()
            # print(f'There are {len(inputs)} sequences')

            # nn = NNTrain(inputs,targets)
            # nn.train()

            # gru = GRU_Model(inputs,targets)
            # gru.train()

            st.title('Music Composition Generator')
            st.markdown('This application is all about Generating Music Composition through Artificial Intelligence and Machine Learning on different instruments randomly')
            st.sidebar.title('Genenrating Music Composition')
            st.sidebar.markdown("We can give random music generation to the user")
            checkbox_enabled = False
        

            # def enable_checkbox():
            #     global checkbox_enabled
            #     st.write("Waiting...")
            #     # time.sleep(45)
            #     checkbox_enabled = True
            #     st.button("Download",on_click=)

            def make_melody():
                mg = MelodyGenerator('model.h5')
                seed = ''
                with open(r'Songs_Dataset','r') as fp:
                    allText = fp.read()
                    words = list(map(str, allText.split()))
                    for i in range(20):
                        word = random.choice(words)
                        if word!='/':
                            seed+=word+' '
                print(seed)
                # seed = '98 _ _ r _ _ 55 _ _ 80 _ 75 _'
                melody = mg.generate_melody(seed,450,64,0.3)
                print(melody)
                mg.save_melody(melody)
                st.text('File is Sucessfully Downloaded')

            st.button("Generate Piano Music",on_click=make_melody)
            
            
                # enable_checkbox()
                 
            # mg = MelodyGenerator('model.h5')
            # seed = ''
            # with open(r'Songs_Dataset','r') as fp:
            #       allText = fp.read()
            #       words = list(map(str, allText.split()))
            #       for i in range(20):
            #             word = random.choice(words)
            #             if word!='/':
            #                 seed+=word+' '
            # print(seed)
            # # seed = '98 _ _ r _ _ 55 _ _ 80 _ 75 _'
            # melody = mg.generate_melody(seed,550,64,0.5)
            # print(melody)
            # mg.save_melody(melody)

