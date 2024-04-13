import os
import shutil
import tqdm

from tools.tools_constants import (
    PATH_DATASET,
    PATH_TEST_DATASET,
    PATH_TRAIN_DATASET,
    PATH_VALID_DATASET
)

list_modes = [
    [PATH_TEST_DATASET, PATH_DATASET + "test_raw/"],
    [PATH_TRAIN_DATASET, PATH_DATASET + "train_raw/"],
    [PATH_VALID_DATASET, PATH_DATASET + "valid_raw/"]
]

list_former_test_set = os.listdir(PATH_DATASET + "asl_alphabet_test/")
list_former_train_set = []
for folder in os.listdir(PATH_DATASET + "asl_alphabet_train/"):
    for file in os.listdir(PATH_DATASET + "asl_alphabet_train/" + folder + "/"):
        list_former_train_set.append(folder + file)
list_former_new_set = os.listdir(PATH_DATASET + "asl_alphabet_new/")

for mode in list_modes:
    path_clean = mode[0]
    path_raw = mode[1]
    for image in tqdm.tqdm(os.listdir(path_clean)):
        type_image = image[0]

        image_jpg = image.replace(".png", ".jpg")
        image_name_jpg = image_jpg[1:]

        image_jpeg = image.replace(".png", ".jpeg")
        image_name_jpeg = image_jpeg[1:]

        if image_jpg in list_former_test_set:
            shutil.copyfile(
            PATH_DATASET + "asl_alphabet_test/" + image_jpg,
            path_raw + image_jpg)
        elif image_jpeg in list_former_test_set:
            shutil.copyfile(
            PATH_DATASET + "asl_alphabet_test/" + image_name_jpeg,
            path_raw + image_name_jpeg)

        elif image_jpg in list_former_train_set:
            shutil.copyfile(
            PATH_DATASET + "asl_alphabet_train/" + type_image + "/" + image_name_jpg,
            path_raw + image_jpg)
        elif image_jpeg in list_former_train_set:
            shutil.copyfile(
            PATH_DATASET + "asl_alphabet_train/" + type_image + "/" + image_name_jpeg,
            path_raw + image_jpeg)

        elif image_jpg in list_former_new_set:
            shutil.copyfile(
            PATH_DATASET + "asl_alphabet_new/" + image_jpg,
            path_raw + image_jpg)
        elif image_jpeg in list_former_new_set:
            shutil.copyfile(
            PATH_DATASET + "asl_alphabet_new/" + image_name_jpeg,
            path_raw + image_name_jpeg)
        else:
            print(image)
