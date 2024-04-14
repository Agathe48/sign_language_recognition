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

# split the video and save the videos when there is no hand (aka we see the shirt hence more blue pixels)

reference_pause = 0
counter_frame = 0
bool_split_video = False
bool_in_pause = False
bool_wait_for_split = False
bool_is_recording = False
bool_start_record = False
frame_wait_for_split = 0
frame_pause = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # convert the frame to grayscale
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # get the histogram of the frame
    histogram = cv2.calcHist([frame_gray], [0], None, [255], [0, 255])
    # get the number of pixels under the value of 125 in the histogram
    number_pixel_under_125 = np.sum(histogram[:125])

    if frame_number == 0:
        reference_pause = number_pixel_under_125
        print("Reference for pause", reference_pause)
    
    print(number_pixel_under_125)
    if reference_pause * 0.95 <= number_pixel_under_125:
        if video is not None:
            bool_wait_for_split = True
            print("yo")
    else:
        print("I want to start")
        if not bool_is_recording:
            bool_start_record = True
            bool_is_recording = True

    if bool_start_record and not bool_in_pause:
        print("I START RECORD")
        bool_start_record = False
        bool_in_pause = False
        video = cv2.VideoWriter(
            os.path.join(PATH_VIDEOS, f"{str(video_number)}_{LIST_WORDS[video_number]}.avi"),
            cv2.VideoWriter_fourcc(*'XVID'),
            fps,
            (width, height)
        )
        video_number += 1

    if bool_in_pause:
        frame_pause += 1
    if frame_pause >= 10:
        bool_in_pause = False
        frame_pause = 0

    if bool_wait_for_split:
        print("I want to stop")
        frame_wait_for_split += 1
    if frame_wait_for_split >= 10:
        bool_split_video = True
        frame_wait_for_split = 0

    # if bool_split_video and bool_finish_pause:
    if bool_split_video:
        print("I stop")
        bool_split_video = False
        bool_wait_for_split = False
        bool_is_recording = False
        bool_in_pause = True

        if video is not None:
            video.release()

    if bool_is_recording:
        video.write(frame)

    frame_number += 1
