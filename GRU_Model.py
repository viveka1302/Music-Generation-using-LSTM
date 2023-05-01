from sklearn.model_selection import train_test_split
from tensorflow import keras as keras
from keras.layers import GRU
from keras.layers import BatchNormalization
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Activation
from Callbacks import Callbacks

class GRU_Model:
    
    def __init__(self,inputs,targets):    
     
        self.INPUT = inputs
        self.OUTPUT = targets
        self.OUTPUT_UNITS = 88
        self.LOSS_FUNCTION = 'sparse_categorical_crossentropy'
        self.LEARNING_RATE = 0.001
        self.BATCH_SIZE = 128
     
    def build_model(self):
        model = keras.models.Sequential()
        model.add(GRU(
            512,
            input_shape = (self.INPUT.shape[1],self.INPUT.shape[2]),
            recurrent_dropout=0,
            return_sequences=True
        ))
        model.add(GRU(512,return_sequences=True,recurrent_dropout=0))
        model.add(GRU(512))
        model.add(BatchNormalization())
        model.add(Dropout(0.3))
        model.add(Dense(256))
        model.add(Activation('relu'))
        model.add(BatchNormalization())
        model.add(Dropout(0.3))
        model.add(Dense(88))
        model.add(Activation('softmax'))

        model.compile(loss=self.LOSS_FUNCTION,
                      optimizer=keras.optimizers.Adam(learning_rate=self.LEARNING_RATE),
                      metrics=['accuracy'])
        
        model.summary()
        return model  

    def split_data(self):
        x_train, x_test, y_train, y_test = train_test_split(self.INPUT, self.OUTPUT, test_size=0.2, random_state=42)
        return x_train,x_test,y_train,y_test

    def train(self):
        cb = Callbacks()
        model = self.build_model()
        x_train,x_test,y_train,y_test = self.split_data()
        history = model.fit(x_train,y_train,epochs=15,batch_size=self.BATCH_SIZE,callbacks=cb)
        eval = model.evaluate(history,x_test)
        model.save('model_gru.h5')