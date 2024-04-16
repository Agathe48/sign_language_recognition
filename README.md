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

(dire qu'on a le rapport dans le dossier results)