"""
Tools Python file to deal with the dataset.
"""

###############
### Imports ###
###############

### Python imports ###

from token import NUMBER
import cv2
import os
import numpy as np
from tqdm import tqdm
import tensorflow as tf
import random as rd

### Local imports ###

from tools.tools_constants import (
    PATH_TRAIN_DATASET,
    PATH_TEST_DATASET,
    LIST_LETTERS_STATIC,
    IMAGE_SIZE,
    BATCH_SIZE,
    BOOL_PREPROCESSING_CONTOURS
)
from tools.tools_preprocessing import (
    cv2_extract_contours
)

#################
### Functions ###
#################

# Create a train and validation set image per image without going through tensorflow dataset
def create_train_val_set_image_per_image():
    train_images = []
    train_labels = []
    val_images = []
    val_labels = []

    for image_folder in tqdm(os.listdir(PATH_TRAIN_DATASET)):
        for image_file in os.listdir(PATH_TRAIN_DATASET + image_folder + "/"):
            type_image = image_folder
            path_image = PATH_TRAIN_DATASET + image_folder + "/" + image_file

            if type_image in LIST_LETTERS_STATIC:
                image = cv2.imread(path_image)
                type_image = [0] * len(LIST_LETTERS_STATIC)
                type_image[LIST_LETTERS_STATIC.index(image_folder)] = 1

                # Get the RGB colors
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

                # Crop the image
                image = cv2.resize(image, IMAGE_SIZE)

                # Convert the image to gray
                if BOOL_PREPROCESSING_CONTOURS:
                    image = cv2_extract_contours(image)
                    
                new_image = np.zeros((224, 224, 3))
                for i in range(3):
                    new_image[:,:,i] = image

                if rd.random() < 0.8:
                    train_images.append(new_image)
                    train_labels.append(type_image)
                else:
                    val_images.append(new_image)
                    val_labels.append(type_image)

    train_images = np.array(train_images, dtype="float") / 255.0
    train_labels = np.array(train_labels)
    val_images = np.array(val_images, dtype="float") / 255.0
    val_labels = np.array(val_labels)

    return train_images, train_labels, val_images, val_labels

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
