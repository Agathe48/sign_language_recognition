"""
Python file to create the train, valid and test databases.
"""

###############
### Imports ###
###############

### Python imports ###

import tqdm
import os
import random as rd
import shutil
from rembg import remove
from PIL import Image

### Local imports ###

from tools.tools_constants import (
    PATH_RAW_TRAIN_DATASET_1,
    PATH_RAW_TEST_DATASET_1,
    PATH_RAW_DATASET_2,
    PATH_RAW_DATASET_3,
    PATH_TRAIN_DATASET,
    PATH_VALID_DATASET,
    PATH_TEST_DATASET,
    PATH_TRAIN_DATASET_RAW,
    PATH_VALID_DATASET_RAW,
    PATH_TEST_DATASET_RAW
)

#################
### Main code ###
#################

### Create the folders ###

isExist = os.path.exists(PATH_TRAIN_DATASET)
if not isExist:
    os.makedirs(PATH_TRAIN_DATASET)
isExist = os.path.exists(PATH_VALID_DATASET)
if not isExist:
    os.makedirs(PATH_VALID_DATASET)
isExist = os.path.exists(PATH_TEST_DATASET)
if not isExist:
    os.makedirs(PATH_TEST_DATASET)
isExist = os.path.exists(PATH_TRAIN_DATASET_RAW)
if not isExist:
    os.makedirs(PATH_TRAIN_DATASET_RAW)
isExist = os.path.exists(PATH_VALID_DATASET_RAW)
if not isExist:
    os.makedirs(PATH_VALID_DATASET_RAW)
isExist = os.path.exists(PATH_TEST_DATASET_RAW)
if not isExist:
    os.makedirs(PATH_TEST_DATASET_RAW)

### Attribute to train, valid or test ###

def choose_train_valid_test():
    """
    Choose the folder to put the image.

    Parameters
    ----------
    None

    Returns
    -------
    path : str
        Path of the folder to put the image
    """
    # Train or valid
    if rd.random() <= 0.8:
        # Train
        if rd.random() <= 0.8:
            return PATH_TRAIN_DATASET, PATH_TRAIN_DATASET_RAW
        else:
            return PATH_VALID_DATASET, PATH_VALID_DATASET_RAW
    else:
        return PATH_TEST_DATASET, PATH_TEST_DATASET_RAW

### Use the first dataset, train ###

for folder in tqdm.tqdm(os.listdir(PATH_RAW_TRAIN_DATASET_1)):
    type_image = folder
    for file in tqdm.tqdm(os.listdir(PATH_RAW_TRAIN_DATASET_1 + folder + "/")):
        if rd.random() > 0.97:
            path_clean, path_raw = choose_train_valid_test()           
            shutil.copyfile(
                PATH_RAW_TRAIN_DATASET_1 + folder + '/' + file,
                path_raw + type_image + file)

            # Remove background
            image = Image.open(PATH_RAW_TRAIN_DATASET_1 + folder + '/' + file,) 
            image = remove(image)
            image.save(path_clean + type_image + file)

### Use the first dataset, test ###

for file in tqdm.tqdm(os.listdir(PATH_RAW_TEST_DATASET_1)):
    path_clean, path_raw = choose_train_valid_test()           
    shutil.copyfile(
        PATH_RAW_TEST_DATASET_1 + file,
        path_raw + file)

    # Remove background
    image = Image.open(PATH_RAW_TEST_DATASET_1 + file,) 
    image = remove(image)
    image.save(path_clean + type_image + file)

### Use the second dataset ###

for mode in tqdm.tqdm(["train/", "valid/", "test/"]):
    for file in tqdm.tqdm(os.listdir(PATH_RAW_DATASET_2 + mode)):
        if file[0] not in ["j", "J", "z", "Z"]:
            path_clean, path_raw = choose_train_valid_test()     
            shutil.copyfile(
                PATH_RAW_DATASET_2 + mode + file,
                path_raw + file)

            # Remove background
            image = Image.open(PATH_RAW_DATASET_2 + mode + file,) 
            image = remove(image)
            image.save(path_clean + file)

### Use the third dataset ###

for user in tqdm.tqdm(os.listdir(PATH_RAW_DATASET_3)):
    for folder in tqdm.tqdm(os.listdir(PATH_RAW_DATASET_3 + user + "/")):
        type_image = folder.upper()
        for file in tqdm.tqdm(os.listdir(PATH_RAW_DATASET_3 + user + '/' + folder)):
            path_clean, path_raw = choose_train_valid_test()           
            shutil.copyfile(
                PATH_RAW_DATASET_3 + user + '/' + folder + '/' + file,
                path_raw + type_image + file)

            # Remove background
            image = Image.open(PATH_RAW_DATASET_3 + user + '/' + folder + '/' + file,) 
            image = remove(image)
            image.save(path_clean + type_image + file)
