import tensorflow
import os
from tensorflow import keras as keras
from keras.layers import LSTM
from keras.layers import BatchNormalization
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Activation
from Callbacks import Callbacks


class NNTrain:
    
    def __init__(self,inputs,targets):
        #os.environ["TF_GPU_ALLOCATOR"] = "cuda_malloc_async"
        physical_devices= tensorflow.config.list_physical_devices("GPU")
        print(physical_devices)
        # config = ConfigProto()
        # config.gpu_options.per_process_gpu_memory_fraction = 0.2
        # config.gpu_options.allow_growth = True
        # session = InteractiveSession(config=config)
        #gpu_options = tensorflow.compat.v1.GPUOptions(per_process_gpu_memory_fraction=0.560)
        ''' tensorflow.config.set_logical_device_configuration(
        physical_devices[0],
        [tensorflow.config.LogicalDeviceConfiguration(memory_limit=3072)])'''
        #sess = tensorflow.compat.v1.Session(config=tensorflow.compat.v1.ConfigProto(gpu_options=gpu_options))
        #tensorflow.config.experimental.set_memory_growth(physical_devices[0],True)
        # config = tensorflow.compat.v1.ConfigProto()
        # config.gpu_options.per_process_gpu_memory_fraction = 0.7
        # session = tensorflow.compat.v1.Session(config=config)
        self.INPUT = inputs
        self.OUTPUT = targets
        self.OUTPUT_UNITS = 88
        self.LOSS_FUNCTION = 'sparse_categorical_crossentropy'
        self.LEARNING_RATE = 0.001
        self.BATCH_SIZE = 128
      #  Dst_tensor = tensorflow.zeros(shape=[self.BATCH_SIZE, self.OUTPUT_UNITS])


    def build_model(self):
        model = keras.models.Sequential()
        model.add(LSTM(
            512,
            input_shape = (self.INPUT.shape[1],self.INPUT.shape[2]),
            recurrent_dropout=0,
            return_sequences=True
        ))
        model.add(LSTM(512,return_sequences=True,recurrent_dropout=0))
        model.add(LSTM(512))
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

    def train(self):
        cb = Callbacks()
        model = self.build_model()
        model.fit(self.INPUT,self.OUTPUT,epochs=100,batch_size=self.BATCH_SIZE,callbacks=cb)
        model.save('model.h5')