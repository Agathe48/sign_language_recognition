"""
Tools Python file with the models for recognition.
"""

###############
### Imports ###
###############

### Python imports ###

import tensorflow as tf
import tensorflow_hub as hub

### Local imports ###

from tools.tools_constants import (
    LIST_LETTERS_STATIC
)

#################
### Functions ###
#################

def create_mobilenetv2(number_classes=len(LIST_LETTERS_STATIC)):
    mobilenet_v2 = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4"
    mobile_net_layers = hub.KerasLayer(mobilenet_v2, input_shape=(224,224,3))

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
