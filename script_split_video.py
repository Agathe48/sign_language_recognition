"""
Python file to split the ASL video into 299 small videos for each word.
"""

###############
### Imports ###
###############

### Python imports ###

import cv2
import numpy as np
import os

### Local imports ###

from tools.tools_constants import (
    PATH_RAW_VIDEO,
    PATH_VIDEOS,
    LIST_WORDS
)

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

# Initialize the booleans for splitting the video
bool_split_video = False
bool_is_recording = False
bool_start_record = False

# Set the separating ratio between the number of red pixels and blue ones
limit_ratio_red_blue = 0.99

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Isolate the red and blue channels
    red = frame[:,:,0]
    blue = frame[:,:,2]

    # Compute the ratio between the number of red pixels and blue ones
    ratio_red_on_blue = np.sum(red)/np.sum(blue)

    # Split video when the current ratio is above the reference
    if ratio_red_on_blue > limit_ratio_red_blue:
        bool_split_video = True
    else:
        if not bool_is_recording:
            bool_start_record = True
            bool_is_recording = True

    # Start to record the video and save it the dataset/video_words
    if bool_start_record:
        bool_start_record = False
        video = cv2.VideoWriter(
            os.path.join(PATH_VIDEOS, f"{str(video_number)}_{LIST_WORDS[video_number]}.avi"),
            cv2.VideoWriter_fourcc(*'XVID'),
            fps,
            (width, height)
        )
        video_number += 1

    # Finish the video
    if bool_split_video:
        bool_split_video = False
        bool_is_recording = False

        if video is not None:
            video.release()

    # When recording, add the current frame
    if bool_is_recording:
        video.write(frame)
    
    frame_number += 1
