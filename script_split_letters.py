"""
Python file to isolate the five letters for each video.
"""

###############
### Imports ###
###############

### Python imports ###

import cv2
import os

### Local imports ###

from tools.tools_constants import (
    PATH_VIDEOS,
    PATH_LIST_WORDS_CLEAN,
    PATH_FRAMES_VIDEO
)

NB_LETTERS = 5
TIME_REDUCE = 0.87 # 0.87
START_OFFSET = 3 # 3
if not os.path.exists(PATH_FRAMES_VIDEO):
    os.mkdir(PATH_FRAMES_VIDEO)

def split_video_word_on_letters(idx,word):
    """
    Split the video word on the letters.

    Parameters
    ----------
    idx : int
        Index of the video
    word : str
        Word of the video
    
    Returns
    -------
    None
    """
    
    # Load the video
    cap = cv2.VideoCapture(PATH_VIDEOS + f"{str(idx)}_{word}.avi")

    # Check if the video is opened correctly
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()

    # Get the total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    useful_frames = total_frames - START_OFFSET
    time_split = int(useful_frames*TIME_REDUCE/NB_LETTERS)

    # Create folder for letters
    path_letters_video = PATH_FRAMES_VIDEO + str(idx) + '_' + word + "/"
    if not os.path.exists(path_letters_video):
        os.mkdir(path_letters_video)

    letter_id = 0

    for frame_number in range(int(total_frames*TIME_REDUCE)):
        ret, frame = cap.read()

        if frame_number == START_OFFSET + int(time_split/2) + time_split * letter_id:
            try:
                cv2.imwrite(path_letters_video + f"{letter_id}_{word[letter_id]}.png",frame)
            except:
                pass
            letter_id += 1
        
def split_letters_for_videos_in_csv(path_csv):
    """
    Split the letters for the videos in the csv.

    Parameters
    ----------
    path_csv : str
        Path of the csv
    
    Returns
    -------
    None
    """
    with open(path_csv,"r") as file:
        for line in file:
            idx,word = line.replace("\n","").split(",")
            idx = int(idx)
            split_video_word_on_letters(idx, word)

split_letters_for_videos_in_csv(PATH_LIST_WORDS_CLEAN)
