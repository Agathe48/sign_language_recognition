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
PATH_TRAIN_DATASET = PATH_DATASET + "asl_alphabet_train_clean/"
PATH_TEST_DATASET = PATH_DATASET + "asl_alphabet_test/"

#################
### Constants ###
#################

LIST_LETTERS_STATIC = [
    "A", "B", "C", "D", "E", "F", "G", "H",
    "I", "K", "L", "M", "N", "O", "P", "Q",
    "R", "S", "T", "U", "V", "W", "X", "Y"]

IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32

NUMBER_BATCHES_TRAINING = 100
TRAIN_MODE = False
NUMBER_EPOCHS = 2
