"""
Tools Python file to deal with the dataset.
"""

###############
### Imports ###
###############

### Python imports ###

from ctypes.wintypes import BOOL
import cv2
import os
import numpy as np
from tqdm import tqdm

### Local imports ###

from tools.tools_constants import (
    PATH_TRAIN_DATASET,
    PATH_VALID_DATASET,
    PATH_TEST_DATASET,
    LIST_LETTERS_STATIC,
    IMAGE_SIZE,
    TRAIN_MODE,
    BOOL_PREPROCESSING_CONTOURS,
    BOOL_HSV,
    BOOL_XYZ,
    BOOL_LAB
)
from tools.tools_preprocessing import (
    canny_detector
)

#################
### Functions ###
#################

# Create a train and validation set image per image without going through tensorflow dataset
def create_train_val_test_set():
    """
    Create the train, validation and test set.

    Parameters
    ----------
    None 
    
    Returns
    -------
    train_images : np.array
    train_labels : np.array
    val_images : np.array
    val_labels : np.array
    test_images : np.array
    test_labels : np.array
    """
    train_images = []
    train_labels = []
    val_images = []
    val_labels = []
    test_images = []
    test_labels = []

    if TRAIN_MODE:
        list_modes = [
            ["train", PATH_TRAIN_DATASET],
            ["validation", PATH_VALID_DATASET],
            ["test", PATH_TEST_DATASET]
        ]
    else:
        list_modes = [
            ["test", PATH_TEST_DATASET]
        ]

    for element in list_modes:
        mode = element[0]
        path_mode = element[1]
        for image_file in tqdm(os.listdir(path_mode)):
            type_image = image_file[0]
            path_image = path_mode + image_file

            if type_image in LIST_LETTERS_STATIC:
                image = cv2.imread(path_image)
                label_image = [0] * len(LIST_LETTERS_STATIC)
                label_image[LIST_LETTERS_STATIC.index(type_image)] = 1

                # Get the RGB colors
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                if BOOL_HSV:
                    image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
                if BOOL_XYZ:
                    image = cv2.cvtColor(image, cv2.COLOR_RGB2XYZ)
                if BOOL_LAB:
                    image = cv2.cvtColor(image, cv2.COLOR_RGB2LAB)
                # Crop the image
                image = cv2.resize(image, IMAGE_SIZE)
                new_image = image

                # Convert the image to gray
                if BOOL_PREPROCESSING_CONTOURS:
                    image = canny_detector(image)
                    
                    new_image = np.zeros((224, 224, 3))
                    for i in range(3):
                        new_image[:,:,i] = image

            if mode == "train":
                train_images.append(new_image)
                train_labels.append(label_image)
            elif mode == "validation":
                val_images.append(new_image)
                val_labels.append(label_image)
            elif mode == "test":
                test_images.append(new_image)
                test_labels.append(label_image)

    train_images = np.array(train_images, dtype=np.float16) / 255.0
    train_labels = np.array(train_labels)
    val_images = np.array(val_images, dtype=np.float16) / 255.0
    val_labels = np.array(val_labels)
    test_images = np.array(test_images, dtype=np.float16) / 255.0
    test_labels = np.array(test_labels)

    return train_images, train_labels, val_images, val_labels, test_images, test_labels
