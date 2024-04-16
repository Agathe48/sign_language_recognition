"""
Tools Python file with the models for recognition.
"""

###############
### Imports ###
###############

### Python imports ###

import tensorflow as tf
import tensorflow_hub as hub
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPool2D, Dropout

### Local imports ###

from tools.tools_constants import (
    LIST_LETTERS_STATIC
)

#################
### Functions ###
#################

def create_mobilenetv2(number_classes=len(LIST_LETTERS_STATIC)):
    """
    Create a model based on MobileNetV2.

    Parameters
    ----------
    number_classes : int
        Number of classes to predict
    
    Returns
    -------
    model : tf.keras.Model
        Model based on MobileNetV2
    """
    mobilenet_v2 = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4"
    input_shape = (224, 224, 3)
    mobile_net_layers = hub.KerasLayer(
        mobilenet_v2, input_shape=input_shape)

    # Do not change the weights of MobileNetV2 during training
    mobile_net_layers.trainable = False

    model = tf.keras.Sequential([
        tf.keras.layers.Dropout(0.1),
        mobile_net_layers,
        tf.keras.layers.Dropout(0.1),
        tf.keras.layers.Dense(number_classes, activation='softmax')
        ])

    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=['accuracy'])
    
    return model

def create_cnn(number_classes=len(LIST_LETTERS_STATIC)):
    """
    Create a CNN model.

    Parameters
    ----------
    number_classes : int
        Number of classes to predict
    
    Returns
    -------
    model : tf.keras.Model
        CNN model
    """
    model=Sequential()
    model.add(Conv2D(128,kernel_size=(5,5),
                    strides=1,padding='same',activation='relu',input_shape=(224,224,3)))
    model.add(MaxPool2D(pool_size=(3,3),strides=2,padding='same'))
    model.add(Conv2D(64,kernel_size=(2,2),
                    strides=1,activation='relu',padding='same'))
    model.add(MaxPool2D((2,2),2,padding='same'))
    model.add(Conv2D(32,kernel_size=(2,2),
                    strides=1,activation='relu',padding='same'))
    model.add(MaxPool2D((2,2),2,padding='same'))
            
    model.add(Flatten())

    model.add(Dense(units=512,activation='relu'))
    model.add(Dropout(rate=0.25))
    model.add(Dense(units=number_classes,activation='softmax'))

    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy'])
    
    return model

