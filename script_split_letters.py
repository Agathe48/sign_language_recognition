import cv2
import os
from tools.tools_constants import (
    PATH_VIDEOS,
    PATH_LIST_WORDS_CLEAN,
    PATH_FRAMES_VIDEO
)

NB_LETTERS = 5
TIME_REDUCE = 1
START_OFFSET = 5
print("AAAAAAAAAAAAAAAA")
def split_video_word_on_letters(idx,word):
    
    # Load the video
    cap = cv2.VideoCapture(PATH_VIDEOS + f"{str(idx)}_{word}.avi")

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
    useful_frames = total_frames - START_OFFSET
    print("TOTAL FRAMES", total_frames, useful_frames)
    time_split = int(useful_frames*TIME_REDUCE/NB_LETTERS)

    # Create folder for letters
    path_letters_video = PATH_FRAMES_VIDEO + word + "/"
    if not os.path.exists(path_letters_video):
        os.mkdir(path_letters_video)

    letter_id = 0

    for frame_number in range(int(total_frames*TIME_REDUCE)):
        ret, frame = cap.read()

        if frame_number == START_OFFSET + int(time_split/2) + time_split * letter_id:
            print(START_OFFSET + int(time_split/2) + time_split * letter_id)
            cv2.imwrite(path_letters_video + f"{letter_id}_{word[letter_id]}.png",frame)
            letter_id += 1
        



    # if frame_number % time_split == 0:
    #     # Pause
    #     bool_split_video = True
    # else:
    #     if not bool_is_recording:
    #         bool_start_record = True
    #         bool_is_recording = True

    # if bool_start_record:
    #     bool_start_record = False
    #     video = cv2.VideoWriter(
    #         os.path.join(PATH_VIDEOS, f"{str(video_number)}_{LIST_WORDS[video_number]}.avi"),
    #         cv2.VideoWriter_fourcc(*'XVID'),
    #         fps,
    #         (width, height)
    #     )
    #     video_number += 1

    # if bool_split_video:
    #     bool_split_video = False
    #     bool_is_recording = False

    #     if video is not None:
    #         video.release()

    # if bool_is_recording:
    #     video.write(frame)


def split_letters_for_videos_in_csv(path_csv):
    with open(path_csv,"r") as file:
        for line in file:
            idx,word = line.replace("\n","").split(",")
            idx = int(idx)
            split_video_word_on_letters(idx, word)
            if idx >= 5:
                break

split_letters_for_videos_in_csv(PATH_LIST_WORDS_CLEAN)
