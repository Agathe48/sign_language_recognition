# Sign language recognition

## Table of contents

- [Sign language recognition](#sign-language-recognition)
  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Todo list](#todo-list)
  - [Articles](#articles)
  - [Utilization](#utilization)
    - [Obtain the database](#obtain-the-database)
    - [Installing the requirements](#installing-the-requirements)
    - [Launch the main code](#launch-the-main-code)
  - [Architecture of this project](#architecture-of-this-project)
    - [Results](#results)

## Introduction

## Utilization

### Obtain the train, valid and test databases

For this work, we use several database we obtained at different sources.

The first dataset we use is the set downloadable on this [*Kaggle* notebook](https://www.kaggle.com/datasets/debashishsau/aslamerican-sign-language-aplhabet-dataset?resource=download). We removed to this dataset the letters j, z, space, delete and nothing, as the two first ones are in movement, whereas the three others are not interesting for our study case.

Then we put both folders (train and test set) of the *zip* file in the folder `dataset/`.

The second dataset we use is the set downloadable on this [site](https://public.roboflow.com/object-detection/american-sign-language-letters/1). We decided to use this one in addition to the first one to have more diversity in the results. Indeed, the results were significantly improved with the mixte of both datasets.

Then we put the folder containing three subfolders (train, valid, test) of the *zip* file in the folder `dataset/`.

Other datasets : 
The third dataset we use is the set downloadable on this [site](https://data.mendeley.com/datasets/xs6mvhx6rh/1). We only used the images contained in the `images/` folder. Then for each subfolder `User_1/`, `User_2/`, `User_3/` and `User_4/` we removed the folders `fn/` and `sp/`.

=> enlever les lettres fn, sp pour les quatre users

Final video :
https://www.youtube.com/watch?v=yizRk2CP9gs 


### Installing the requirements

### Launch the main code

## Architecture of this project

### Results

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
MobileNetV2, 8 époques, sans contours, HSV, avec background : xx% d'accuracy, xx% d'accuracy sur 3
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


CNN temps d'entraînement sur 3 époques : 35 minutes


CNN, 3 époques, contours : 47% d'accuracy, 69% d'accuracy sur 3

Résultats sur la vidéo :
MobileNetV2, 8 époques, contours, anciens datasets : 95 mots bien retrouvés sur 295
[10, 5, 9, 1, 8, 2, 5, 1, 6, 9, 1, 1, 3, 1, 1, 2, 1, 9, 1, 2, 2, 6, 3, 9, 5, 2, 3, 5, 2, 5, 1, 3, 10, 1, 3, 2, 5, 3, 2, 1, 3, 5, 5, 8, 10, 2, 5, 6, 1, 3, 2, 1, 1, 2, 1, 8, 10, 6, 2, 1, 4, 1, 1, 6, 1, 1, 3, 1, 7, 10, 2, 1, 10, 1, 5, 8, 3, 7, 4, 1, 5, 1, 4, 3, 6, 6, 2, 1, 9, 5, 2, 10, 2, 6, 1]
