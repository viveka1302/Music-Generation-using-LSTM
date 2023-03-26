import tensorflow.keras as keras

class Callbacks(keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if(logs.get('loss')<0.4 and logs.get('accuracy')>0.96):
            print()
            print(r'Loss is less than 40% and Accuarcy more than 96%')
            self.model.stop_training=True
            
       