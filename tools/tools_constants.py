"""
Tools Python file with the main constants.
"""

#############
### Paths ###
#############

PATH_DATASET = "dataset/"
PATH_MODELS = "models/"
PATH_RESULTS = "results/"

PATH_RAW_TRAIN_DATASET = PATH_DATASET + "asl_alphabet_train/"
PATH_RAW_SHORT_TRAIN_DATASET = PATH_DATASET + "asl_alphabet_train_short/"
PATH_RAW_TEST_DATASET = PATH_DATASET + "asl_alphabet_test/"
PATH_TRAIN_DATASET = PATH_DATASET + "train/"
PATH_VALID_DATASET = PATH_DATASET + "valid/"
PATH_TEST_DATASET = PATH_DATASET + "test/"

#################
### Constants ###
#################

LIST_LETTERS_STATIC = [
    "A", "B", "C", "D", "E", "F", "G", "H",
    "I", "K", "L", "M", "N", "O", "P", "Q",
    "R", "S", "T", "U", "V", "W", "X", "Y"]

IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32

MODEL_NAME = "mobilenetv2" # mobilenetv2 cnn
TRAIN_MODE = True
NUMBER_EPOCHS = 10
BOOL_PREPROCESSING_CONTOURS = False
BOOL_HSV = True
