###############
### Imports ###
###############

### Python imports ###

import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

### Local imports ###

from tools.tools_constants import (
    PATH_RAW_VIDEO,
    PATH_VIDEOS,
    LIST_WORDS
)


def calculhisto(I,color):
    for i,col in enumerate(color):
        histr = cv2.calcHist([I],[i],None,[256],[0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])
    plt.show()
    
    

#################
### Main code ###
#################

# Load the video
cap = cv2.VideoCapture(PATH_RAW_VIDEO)

# Check if the video is opened correctly
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Get the frames per second (fps)
fps = cap.get(cv2.CAP_PROP_FPS)

# Get the width and height of the video
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Get the total number of frames in the video
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Initialize variables
frame_number = 0
hand_disappeared = False
video_number = 0
video = None

bool_split_video = False
bool_is_recording = False
bool_start_record = False

limit_ratio_red_blue = 0.99

while True:
    ret, frame = cap.read()

    if not ret:
        break

    red = frame[:,:,0]
    blue = frame[:,:,2]

    ratio_red_on_blue = np.sum(red)/np.sum(blue)

    if ratio_red_on_blue > limit_ratio_red_blue:
        # Pause
        bool_split_video = True
    else:
        if not bool_is_recording:
            bool_start_record = True
            bool_is_recording = True

    if bool_start_record:
        bool_start_record = False
        video = cv2.VideoWriter(
            os.path.join(PATH_VIDEOS, f"{str(video_number)}_{LIST_WORDS[video_number]}.avi"),
            cv2.VideoWriter_fourcc(*'XVID'),
            fps,
            (width, height)
        )
        video_number += 1

    if bool_split_video:
        bool_split_video = False
        bool_is_recording = False

        if video is not None:
            video.release()

    if bool_is_recording:
        video.write(frame)
    
    frame_number += 1
