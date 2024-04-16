# Sign language recognition

## Table of contents

- [Sign language recognition](#sign-language-recognition)
  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Utilization](#utilization)
    - [Setting the code environment](#setting-the-code-environment)
      - [Cloning the repository](#cloning-the-repository)
      - [Creation of a virtual environment](#creation-of-a-virtual-environment)
      - [Installation of the necessary librairies](#installation-of-the-necessary-librairies)
    - [Obtain the train, valid and test databases](#obtain-the-train-valid-and-test-databases)
      - [Download the datasets](#download-the-datasets)
      - [Create the train, valid and test bases](#create-the-train-valid-and-test-bases)
    - [Obtain the test video for ASL recognition](#obtain-the-test-video-for-asl-recognition)
    - [Launch the main code](#launch-the-main-code)
  - [Architecture of this project](#architecture-of-this-project)
  - [Results](#results)

## Introduction

## Utilization

### Setting the code environment

#### Cloning the repository

To clone the github repository, you have to search the clone button on the main page of the project. Then click on it and select `https` or `ssh` depending on your favorite mode of connexion. Copy the given id and then open a terminal on your computer, go to the folder where you want to install the project and use the following command:

```bash
git clone <your copied content>
```

#### Creation of a virtual environment

You might want to use a virtual environment to execute the code. To do so, use the following command:

```bash
python -m virtualenv venv
```

To start it, use the command on *Windows*:

```bash
venv/Scripts/Activate.ps1
```

Or for *MacOS* and *Linux*:

```bash
venv/Scripts/activate
```

#### Installation of the necessary librairies

To execute this software, you need several *Python* librairies, specified in the `requirements.txt` file. To install them, use the following command:

```bash
pip install -r requirements.txt
```

### Obtain the train, valid and test databases

#### Download the datasets

For this work, we use several databases we obtained at different sources.

The first dataset we use is the set downloadable on this [*Kaggle* notebook](https://www.kaggle.com/datasets/debashishsau/aslamerican-sign-language-aplhabet-dataset?resource=download). We removed to this dataset the letters j, z, space, delete and nothing, as the two first ones are in movement, whereas the three others are not interesting for our study case.
Then we put both folders (train and test set) of the *zip* file in the folder `dataset/`.

The second dataset we use is the set downloadable on this [site](https://public.roboflow.com/object-detection/american-sign-language-letters/1). We decided to use this one in addition to the first one to have more diversity in the database. Indeed, the results were significantly improved with the mixte of both datasets.
Then we put the folder containing three subfolders (`train`, `valid` and `test`) of the *zip* file in the folder `dataset/`.

The third dataset we use is the set downloadable on this [site](https://data.mendeley.com/datasets/xs6mvhx6rh/1). We only used the images contained in the `images/` folder. Then for each subfolder `User_1/`, `User_2/`, `User_3/` and `User_4/` we removed the folders `fn/` and `sp/`.
Then we put the folder containing four subfolders (`User_1/`, `User_2/`, `User_3/` and `User_4/`) of the *zip* file in the folder `dataset/`.

#### Create the train, valid and test bases

To create the train, validation and test set, you have to run the following command:

```bash
python script_create_dataset.py
```

### Obtain the test video for ASL recognition

To test our model on a real video, we downloaded this [video](https://www.youtube.com/watch?v=yizRk2CP9gs) containing 299 words of 5 letters realized with ASL.

We created then a script to split the video to each word, using a threshold thanks to the hand disappearing from the screen. This threshold corresponds to the ratio between the number of red pixels and the number of blue ones in the image, which is significantly different when the hand is disappearing from the screen. We chose 0.99 as threshold value for this ratio; this value has been determined thanks to the graph we traced at the beginning of the video. This graph can be found in `images/ratio_red_on_blue.png` (and `images/ratio_red_on_blue_250.png`); the abscissa corresponds to the number of frames and the ordinate to the ratio. Overall, to get these individual videos, the user has to run the following command:

```bash
python script_split_video.py
```

After a few minutes, the original video has been separated into 299 small videos containing each one word, all located in the folder `dataset/video_words/`.

Nevertheless, some words were not appropriate for our study, for instance the words with j or z inside. We thus wrote a script to remove these videos and create a *csv* file associating each word with its unique id. It can be run with the following command:

```bash
python script_filter_videos.py
```

We wanted then to isolate each letter of the word and we thus create a script to extract five frames of the video, corresponding more and less to the letter (this script is based on timing and there are sometimes mistakes as the rhythm is not always the same when tracing letters). To isolate these frames, the user has to run the following command:

```bash
python script_split_letters.py
```

### Launch the main code

## Architecture of this project

## Results

MobileNetV2, 3 époques, contours : 61% d'accuracy, 83% d'accuracy sur 3
MobileNetV2, 3 époques, contours, HSV : 57% d'accuracy, 77% d'accuracy sur 3
MobileNetV2, 3 époques, sans contours : 39% d'accuracy, 69% d'accuracy sur 3
MobileNetV2, 3 époques, sans contours, HSV : 48% d'accuracy, 73% d'accuracy sur 3
MobileNetV2, 3 époques, sans contours, HSV, avec background : 16% d'accuracy, 36% d'accuracy sur 3
MobileNetV2, 3 époques, contours, HSV, avec background : 31% d'accuracy, 54% d'accuracy sur 3
MobileNetV2, 3 époques, sans contours, avec background : 26% d'accuracy, 50% d'accuracy sur 3
MobileNetV2, 3 époques, contours, avec background : 41% d'accuracy, 66% d'accuracy sur 3
MobileNetV2, 3 époques, contours, XYZ: 64% d'accuracy, 85% d'accuracy sur 3
MobileNetV2, 3 époques, contours, LAB: 61% d'accuracy, 81% d'accuracy sur 3

MobileNetV2, 6 époques, contours : 69% d'accuracy, 88% d'accuracy sur 3

MobileNetV2, 8 époques, contours : 71% d'accuracy, 88% d'accuracy sur 3
MobileNetV2, 8 époques, sans contours, HSV : 51% d'accuracy, 78% d'accuracy sur 3
MobileNetV2, 8 époques, contours, HSV : 64% d'accuracy, 82% d'accuracy sur 3
MobileNetV2, 8 époques, contours, HSV, avec background : 35% d'accuracy, 56% d'accuracy sur 3
MobileNetV2, 8 époques, sans contours, HSV, avec background : 22% d'accuracy, 42% d'accuracy sur 3
MobileNetV2, 8 époques, sans contours, avec background : 27% d'accuracy, 53% d'accuracy sur 3
MobileNetV2, 8 époques, contours, avec background : 48% d'accuracy, 72% d'accuracy sur 3
MobileNetV2, 8 époques, contours, XYZ: 70% d'accuracy, 87% d'accuracy sur 3
MobileNetV2, 8 époques, contours, LAB: 66% d'accuracy, 86% d'accuracy sur 3

MobileNetV2, 8 époques, large dataset, contours, RGB: 67% d'accuracy, 88% d'accuracy sur 3
MobileNetV2, 8 époques, large dataset, contours, HSV: 59% d'accuracy, 81% d'accuracy sur 3
MobileNetV2, 8 époques, large dataset, contours, XYZ: 69% d'accuracy, 88% d'accuracy sur 3
MobileNetV2, 8 époques, large dataset, contours, LAB: 64% d'accuracy, 85% d'accuracy sur 3

MobileNetV2, 10 époques, contours : 70% d'accuracy, 88% d'accuracy sur 3
MobileNetV2, 10 époques, contours, HSV : 64% d'accuracy, 83% d'accuracy sur 3
MobileNetV2, 10 époques, sans contours, HSV : 51% d'accuracy, 76% d'accuracy sur 3
MobileNetV2, 10 époques, large dataset, contours : 69% d'accuracy, 88% d'accuracy sur 3

MobileNetV2, 15 époques, large dataset, contours, RGB: 70% d'accuracy, 89% d'accuracy sur 3


CNN temps d'entraînement sur 3 époques : 35 minutes


CNN, 3 époques, contours : 47% d'accuracy, 69% d'accuracy sur 3

Résultats sur la vidéo :
MobileNetV2, 8 époques, contours, anciens datasets : 95 mots bien retrouvés sur 295
[10, 5, 9, 1, 8, 2, 5, 1, 6, 9, 1, 1, 3, 1, 1, 2, 1, 9, 1, 2, 2, 6, 3, 9, 5, 2, 3, 5, 2, 5, 1, 3, 10, 1, 3, 2, 5, 3, 2, 1, 3, 5, 5, 8, 10, 2, 5, 6, 1, 3, 2, 1, 1, 2, 1, 8, 10, 6, 2, 1, 4, 1, 1, 6, 1, 1, 3, 1, 7, 10, 2, 1, 10, 1, 5, 8, 3, 7, 4, 1, 5, 1, 4, 3, 6, 6, 2, 1, 9, 5, 2, 10, 2, 6, 1]


MobileNetV2, 15 époques, contours, large datasets : 123 mots bien retrouvés sur 295
[5, 4, 4, 4, 1, 7, 1, 5, 1, 1, 1, 4, 1, 1, 6, 3, 4, 1, 3, 3, 5, 1, 1, 1, 4, 6, 4, 1, 7, 10, 3, 4, 1, 1, 2, 2, 9, 5, 1, 10, 5, 4, 9, 8, 4, 10, 5, 1, 8, 10, 10, 1, 1, 1, 1, 10, 2, 4, 6, 3, 1, 4, 7, 1, 1, 1, 1, 10, 1, 1, 2, 1, 10, 1, 1, 1, 10, 2, 1, 7, 3, 1, 3, 9, 1, 1, 8, 1, 4, 5, 3, 1, 2, 1, 5, 7, 2, 7, 1, 1, 2, 1, 4, 1, 5, 4, 3, 7, 3, 1, 2, 5, 1, 7, 1, 1, 3, 6, 2, 2, 1, 3, 1]
['would', 'could', 'after', 'still', 'child', 'great', 'where', 'woman', 'group', 'again', 'world', 'shall', 'under', 'party', 'place', 'while', 'local', 'bring', 'write', 'quite', 'power', 'order', 'young', 'water', 'level', 'until', 'stand', 'study', 'least', 'right', 'after', 'later', 'price', 'issue', 'speak', 'today', 'class', 'spend', 'paper', 'table', 'clear', 'range', 'trade', 'cover', 'apply', 'raise', 'light', 'claim', 'story', 'board', 'model', 'place', 'human', 'occur', 'labor', 'close', 'color', 'music', 'piece', 'prove', 'royal', 'plant', 'wrong', 'round', 'space', 'award', 'legal', 'means', 'sound', 'happy', 'floor', 'doubt', 'horse', 'glass', 'prime', 'hotel', 'share', 'sorry', 'claim', 'labor', 'whole', 'admit', 'aware', 'above', 'round', 'maybe', 'heavy', 'ready', 'apart', 'mouth', 'laugh', 'study', 'green', 'fully', 'sport', 'offer', 'civil', 'truth', 'clear', 'issue', 'along', 'order', 'route', 'usual', 'track', 'press', 'worry', 'grant', 'phone', 'adult', 'until', 'award', 'broad', 'favor', 'equal', 'rural', 'limit', 'while', 'dream', 'error', 'quick', 'block', 'crowd']



MobileNetV2, 15 époques, contours, large datasets, XYZ : 120 mots bien retrouvés sur 295
[5, 10, 6, 2, 7, 6, 1, 7, 2, 6, 2, 1, 1, 5, 1, 1, 6, 1, 5, 10, 1, 4, 4, 1, 1, 1, 3, 8, 8, 1, 1, 2, 1, 1, 1, 1, 4, 5, 3, 3, 3, 5, 3, 7, 9, 3, 4, 5, 2, 9, 8, 2, 8, 1, 1, 7, 1, 1, 3, 8, 2, 1, 2, 4, 6, 1, 1, 2, 7, 1, 2, 1, 2, 1, 8, 9, 4, 1, 1, 4, 7, 4, 1, 1, 1, 9, 1, 1, 1, 2, 1, 6, 1, 3, 3, 2, 7, 5, 4, 5, 10, 1, 1, 2, 2, 1, 8, 1, 2, 1, 1, 7, 3, 7, 9, 5, 1, 10, 4, 1]
['would', 'their', 'could', 'about', 'after', 'still', 'child', 'great', 'where', 'woman', 'group', 'again', 'world', 'shall', 'under', 'party', 'place', 'while', 'local', 'where', 'bring', 'write', 'power', 'order', 'young', 'water', 'level', 'until', 'allow', 'study', 'least', 'later', 'price', 'issue', 'speak', 'today', 'class', 'spend', 'force', 'learn', 'table', 'clear', 'range', 'trade', 'break', 'cover', 'apply', 'light', 'claim', 'story', 'union', 'board', 'model', 'place', 'human', 'serve', 'occur', 'labor', 'color', 'heart', 'prove', 'royal', 'plant', 'wrong', 'round', 'space', 'award', 'legal', 'means', 'sound', 'above', 'happy', 'floor', 'doubt', 'glass', 'prime', 'hotel', 'sorry', 'labor', 'whole', 'throw', 'aware', 'above', 'round', 'maybe', 'blood', 'ready', 'apart', 'study', 'radio', 'green', 'drink', 'fully', 'offer', 'civil', 'clear', 'agent', 'along', 'order', 'route', 'close', 'usual', 'press', 'worry', 'grant', 'phone', 'touch', 'adult', 'until', 'award', 'broad', 'favor', 'rural', 'while', 'dream', 'error', 'quick', 'below', 'phase', 'crowd']

