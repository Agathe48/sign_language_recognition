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
BOOL_TENSORFLOW = False
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

            # Resizing
            frame = frame[width_to_crop:height+width_to_crop, :]
            frame = cv2.resize(frame, IMAGE_SIZE)
            # cv2.imshow("toto", frame)
            plt.matshow(np.mean(frame, axis=2))


            # Remove background
            frame = remove(frame)
            # Detect contours
            frame = canny_detector(frame)

            # plt.show()
            frame = np.array(frame, dtype="float") / 255.0
            frame = np.expand_dims(frame, axis=0)
            if BOOL_TENSORFLOW:
                predictions = model.predict(frame)
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
