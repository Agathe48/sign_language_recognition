from tools.tools_constants import (
    PATH_DATASET,
    PATH_TRAIN_DATASET,
    PATH_VALID_DATASET,
    PATH_TEST_DATASET
)

import os
import shutil
import tqdm
import random as rd

# for folder in tqdm.tqdm(os.listdir(PATH_TRAIN_DATASET)):
#     for file in os.listdir(PATH_TRAIN_DATASET + folder + "/"):
#         shutil.copyfile(
#             PATH_TRAIN_DATASET + folder + "/" + file,
#             PATH_DATASET + "asl_alphabet_all/" + folder + file)

for file in tqdm.tqdm(os.listdir(PATH_DATASET + "asl_alphabet_all/")):
    # Train or valid
    if rd.random() <= 0.8:
        # Train
        if rd.random() <= 0.8:
            shutil.copyfile(
                PATH_DATASET + "asl_alphabet_all/" + file,
                PATH_TRAIN_DATASET + file)
        else:
            shutil.copyfile(
                PATH_DATASET + "asl_alphabet_all/" + file,
                PATH_VALID_DATASET + file)
    else:
        shutil.copyfile(
            PATH_DATASET + "asl_alphabet_all/" + file,
            PATH_TEST_DATASET + file)
