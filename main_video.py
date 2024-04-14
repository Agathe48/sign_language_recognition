### Python imports ###

import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from rembg import remove 

### Local imports ###

from tools.tools_constants import (
    PATH_MODELS,
    MODEL_NAME,
    NUMBER_EPOCHS,
    BOOL_PREPROCESSING_BACKGROUND,
    BOOL_PREPROCESSING_CONTOURS,
    BOOL_HSV,
    PATH_VIDEOS,
    PATH_FRAMES_VIDEO,
    PATH_LIST_WORDS_CLEAN,
    IMAGE_SIZE
)
BOOL_TENSORFLOW = True
if BOOL_TENSORFLOW:
    from tools.tools_models import (
        create_mobilenetv2,
        create_cnn
    )
from tools.tools_metrics import (
    analyse_predictions_probabilities
)
from tools.tools_preprocessing import (
    canny_detector
)

if BOOL_TENSORFLOW:
    if MODEL_NAME == "mobilenetv2":
        model = create_mobilenetv2()
    elif MODEL_NAME == "cnn":
        model = create_cnn()

    path_to_save = PATH_MODELS + MODEL_NAME + '/E'+ str(NUMBER_EPOCHS)
    if not BOOL_PREPROCESSING_BACKGROUND:
        path_to_save += "_background"
    if BOOL_PREPROCESSING_CONTOURS:
        path_to_save += "_contours"
    if BOOL_HSV:
        path_to_save += "_hsv"
    model.load_weights(path_to_save + "/")

SKIP_FRAMES = 3

def split_video_word_on_letters_high_prediction(idx, word):
    print("NEW WORD", word)
    
    # Load the video
    cap = cv2.VideoCapture(PATH_VIDEOS + f"{str(idx)}_{word}.avi")

    # Get the total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width_to_crop = int((width-height)/2)

    # Create folder for letters
    path_letters_video = PATH_FRAMES_VIDEO + word + "/"
    if not os.path.exists(path_letters_video):
        os.mkdir(path_letters_video)

    letter_id = 0

    for frame_number in range(int(total_frames)):
        ret, frame = cap.read()

        if frame_number % SKIP_FRAMES == 0:

            # Resizing and cropping
            frame = frame[:, width_to_crop:height+width_to_crop]
            frame = cv2.resize(frame, IMAGE_SIZE)
            # Remove background
            frame = remove(frame)
            new_frame = frame
            if BOOL_PREPROCESSING_CONTOURS:
                # Detect contours
                frame = canny_detector(frame)
                # cv2.imwrite("toto.png", frame)
                new_frame = np.zeros((224, 224, 3))
                for i in range(3):
                    new_frame[:,:,i] = frame

            new_frame = np.array(new_frame, dtype="float") / 255.0
            new_frame = np.expand_dims(new_frame, axis=0)
            if BOOL_TENSORFLOW:
                predictions = model.predict(new_frame)
                predicted_labels = analyse_predictions_probabilities(predictions)
                print(predicted_labels)

def split_letters_for_videos_in_csv(path_csv):
    with open(path_csv,"r") as file:
        for line in file:
            idx,word = line.replace("\n","").split(",")
            idx = int(idx)
            split_video_word_on_letters_high_prediction(idx, word)
            if idx >= 1:
                break

split_letters_for_videos_in_csv(PATH_LIST_WORDS_CLEAN)


PATH_ENGLISH_WORDS = "english_words_280k.txt"

def get_5_words_list():
    five_words_list = []
    with open(PATH_ENGLISH_WORDS,"r") as file:
        for line in file:
            line = line.replace("\n","")
            if len(line) == 5:
                five_words_list.append(line)
    return five_words_list

FIVE_WORDS_LIST = get_5_words_list()

def predict_word_with_proba(proba_list,letters_list, nb_words_to_keep):
    score_array = np.zeros(len(FIVE_WORDS_LIST))
    for i in range(len(proba_list)):
        for word_id,word in enumerate(FIVE_WORDS_LIST):
            if word[i] == letters_list[i]:
                score_array[word_id] += proba_list[i]
    best_scores_id = np.argsort(score_array)[:nb_words_to_keep]
    best_scores = score_array[best_scores_id]
    best_words = []
    for best_id in best_scores_id:
        best_words.append(FIVE_WORDS_LIST[best_id])
    
    return best_words, best_scores

