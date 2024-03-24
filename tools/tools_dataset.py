"""
Tools Python file to deal with the dataset.
"""

###############
### Imports ###
###############

### Python imports ###

import cv2
import os
import numpy as np
from tqdm import tqdm
import tensorflow as tf

### Local imports ###

from tools.tools_constants import (
    PATH_TRAIN_DATASET,
    PATH_TEST_DATASET,
    LIST_LETTERS_STATIC,
    IMAGE_SIZE,
    BATCH_SIZE
)

#################
### Functions ###
#################

def create_train_val_set():
    train_set, val_ds = tf.keras.utils.image_dataset_from_directory(
        PATH_TRAIN_DATASET,
        label_mode="categorical",
        validation_split=0.2,
        subset="both",
        seed=123,
        image_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE)

    return train_set, val_ds

def create_test_set():
    test_images = []
    test_labels = []

    for image_file in tqdm(os.listdir(PATH_TEST_DATASET)):
        type_image = image_file[0]

        if type_image in LIST_LETTERS_STATIC:
            image = cv2.imread(PATH_TEST_DATASET + image_file)

            # Get the RGB colors
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Crop the image
            image = cv2.resize(image, IMAGE_SIZE)

            test_images.append(image)
            test_labels.append(type_image)

    test_images = np.array(test_images, dtype="float") / 255.0
    test_labels = np.array(test_labels)

    return test_images, test_labels
