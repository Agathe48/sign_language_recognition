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

BOOL_PREPROCESSING_BACKGROUND = True
if BOOL_PREPROCESSING_BACKGROUND:
    PATH_TRAIN_DATASET = PATH_DATASET + "train/"
    PATH_VALID_DATASET = PATH_DATASET + "valid/"
    PATH_TEST_DATASET = PATH_DATASET + "test/"
else:
    PATH_TRAIN_DATASET = PATH_DATASET + "train_raw/"
    PATH_VALID_DATASET = PATH_DATASET + "valid_raw/"
    PATH_TEST_DATASET = PATH_DATASET + "test_raw/"

PATH_RAW_VIDEO = PATH_DATASET + "Finger_spelling_ASL.mp4"
PATH_VIDEOS = PATH_DATASET + "video_words/"
PATH_LIST_WORDS = PATH_DATASET + "list_words_video.txt"
PATH_LIST_WORDS_CLEAN = PATH_DATASET + "list_words_video_clean.csv"
PATH_FRAMES_VIDEO = PATH_DATASET + "frames_video/"

PATH_ENGLISH_WORDS = PATH_DATASET + "english_words_10k.txt"

#################
### Constants ###
#################

LIST_LETTERS_STATIC = [
    "A", "B", "C", "D", "E", "F", "G", "H",
    "I", "K", "L", "M", "N", "O", "P", "Q",
    "R", "S", "T", "U", "V", "W", "X", "Y"]

# get the list of word in path_list_words
with open(PATH_LIST_WORDS, "r") as file:
    LIST_WORDS = file.read().splitlines()

IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32

MODEL_NAME = "mobilenetv2" # mobilenetv2 cnn
TRAIN_MODE = True
NUMBER_EPOCHS = 3
BOOL_PREPROCESSING_CONTOURS = True
BOOL_HSV = False
BOOL_XYZ = False
BOOL_LAB = True

def get_5_words_list():
    five_words_list = []
    with open(PATH_ENGLISH_WORDS,"r") as file:
        for line in file:
            line = line.replace("\n","")
            if len(line) == 5:
                five_words_list.append(line)
    return five_words_list

FIVE_LETTERS_WORDS_LIST = get_5_words_list()
