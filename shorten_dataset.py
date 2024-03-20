from tqdm import tqdm
import os
import random as rd
import shutil

from tools.tools_constants import (
    PATH_RAW_SHORT_TRAIN_DATASET,
    PATH_RAW_TRAIN_DATASET
)

folder_path = PATH_RAW_TRAIN_DATASET
folder_destination = PATH_RAW_SHORT_TRAIN_DATASET

for folder in tqdm(os.listdir(folder_path)):
    for file in tqdm(os.listdir(folder_path + folder)):
        if rd.random() > 0.97:
            if not os.path.exists(folder_destination + '/' + folder):
                os.makedirs(folder_destination + '/' + folder)
            shutil.copyfile(
                folder_path + '/' + folder + '/' + file,
                folder_destination + '/' + folder + '/' + file)