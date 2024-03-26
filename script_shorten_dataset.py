"""
Python script to shorten the dataset, to avoid too long computations.
"""

###############
### Imports ###
###############

### Python imports ###

from tqdm import tqdm
import os
import random as rd
import shutil

### Local imports ###

from tools.tools_constants import (
    PATH_RAW_SHORT_TRAIN_DATASET,
    PATH_RAW_TRAIN_DATASET
)

#################
### Main code ###
#################

for folder in tqdm(os.listdir(PATH_RAW_TRAIN_DATASET)):
    for file in tqdm(os.listdir(PATH_RAW_TRAIN_DATASET + folder)):
        if rd.random() > 0.97:
            if not os.path.exists(PATH_RAW_SHORT_TRAIN_DATASET + '/' + folder):
                os.makedirs(PATH_RAW_SHORT_TRAIN_DATASET + '/' + folder)
            shutil.copyfile(
                PATH_RAW_TRAIN_DATASET + '/' + folder + '/' + file,
                PATH_RAW_SHORT_TRAIN_DATASET + '/' + folder + '/' + file)
