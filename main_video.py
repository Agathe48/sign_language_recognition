###############
### Imports ###
###############

### Python imports ###

import cv2
import tqdm
import numpy as np
from rembg import remove 

### Local imports ###

from tools.tools_constants import (
    PATH_MODELS,
    FIVE_LETTERS_WORDS_LIST,
    MODEL_NAME,
    NUMBER_EPOCHS,
    BOOL_PREPROCESSING_BACKGROUND,
    BOOL_PREPROCESSING_CONTOURS,
    BOOL_HSV,
    PATH_FRAMES_VIDEO,
    PATH_LIST_WORDS_CLEAN,
    IMAGE_SIZE,
    BOOL_LAB,
    BOOL_XYZ
)
from tools.tools_models import (
    create_mobilenetv2,
    create_cnn
)
from tools.tools_metrics import (
    analyse_predictions_probabilities
)
from tools.tools_preprocessing import (
    canny_detector,
    load_image
)

#################
### Main code ###
#################

if MODEL_NAME == "mobilenetv2":
    model = create_mobilenetv2()
elif MODEL_NAME == "cnn":
    model = create_cnn()

BOOL_LARGE_DATASET = True
if BOOL_LARGE_DATASET:
    add = "New_"
else:
    add = ""
path_to_save = PATH_MODELS + MODEL_NAME + '/' + add + 'E'+ str(NUMBER_EPOCHS)
if not BOOL_PREPROCESSING_BACKGROUND:
    path_to_save += "_background"
if BOOL_PREPROCESSING_CONTOURS:
    path_to_save += "_contours"
if BOOL_HSV:
    path_to_save += "_hsv"
if BOOL_LAB:
    path_to_save += "_lab"
if BOOL_XYZ:
    path_to_save += "_xyz"
model.load_weights(path_to_save + "/")

def predict_word_with_proba(proba_array, letters_array, nb_words_to_keep):
    score_array = np.zeros(len(FIVE_LETTERS_WORDS_LIST))
    for i in range(len(proba_array)): # ID de la lettre
        for j in range(len(proba_array[0])): # Rang de probabilité
            for word_id, word in enumerate(FIVE_LETTERS_WORDS_LIST):
                if word[i] == letters_array[i][j].lower():
                    score_array[word_id] += proba_array[i][j]
    best_scores_id = np.argsort(score_array)[::-1][:nb_words_to_keep]
    best_scores = score_array[best_scores_id]
    best_words = []
    for best_id in best_scores_id:
        best_words.append(FIVE_LETTERS_WORDS_LIST[best_id])
    
    return best_words, best_scores


def predict_word(idx, word):
    print("NEW WORD", word)

    path_word_letters_images = PATH_FRAMES_VIDEO + "offset_3_time_reduce_87/" + str(idx) + "_" + word + "/"
    list_predicted_letters = []
    list_predicted_probas = []
    
    for counter_letter in range(5):
        # Open image
        image = load_image(path_word_letters_images + f"{counter_letter}_{word[counter_letter]}.png", show = False)
        
        width = image.shape[0]
        height = image.shape[1]
        width_to_crop = int((height-width)/2)

        # Resizing and cropping
        image = image[:, width_to_crop:height+width_to_crop]
        image = cv2.resize(image, IMAGE_SIZE)

        # Remove background
        image = remove(image)
        new_image = image
        if BOOL_PREPROCESSING_CONTOURS:
            # Detect contours
            image = canny_detector(image)
            new_image = np.zeros((224, 224, 3))
            for i in range(3):
                new_image[:,:,i] = image

        new_image = np.array(new_image, dtype="float") / 255.0
        new_image = np.expand_dims(new_image, axis=0)
        predictions = model.predict(new_image)
        predicted_labels, predicted_probas = analyse_predictions_probabilities(
            prediction=predictions[0],
            number_elements_to_take=5)
        list_predicted_letters.append(predicted_labels)
        list_predicted_probas.append(predicted_probas)
        # print("Most probable letter ", counter_letter, " : ", predicted_labels, " with proba ", predicted_probas)

    best_words, best_scores = predict_word_with_proba(
        proba_array=list_predicted_probas,
        letters_array=list_predicted_letters,
        nb_words_to_keep=10
    )
    return best_words, best_scores

score_words = 0
list_index_words_predicted = []
list_words_predicted = []

with open(PATH_LIST_WORDS_CLEAN,"r") as file:
    for line in tqdm.tqdm(file):
        idx, word  = line.replace("\n","").split(",")
        idx = int(idx)
        best_words, best_scores = predict_word(idx, word)
        if word in best_words:
            print("\n", "--- VICTOIRE", word, best_words, best_scores, "\n")
            score_words += 1
            list_index_words_predicted.append(best_words.index(word) + 1)
            list_words_predicted.append(word)

print(score_words)
print(list_index_words_predicted)
print(list_words_predicted)
