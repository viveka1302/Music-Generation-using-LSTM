from tensorflow import keras

class Callbacks(keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if(logs.get('accuracy')>0.77):
            print()
            print(r'Loss is less than 40% and Accuarcy more than 96%')
            self.model.stop_training=True
            
       