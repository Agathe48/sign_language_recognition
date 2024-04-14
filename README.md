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

## Todo list

- [ ] écrire l'état de l'art
- [ ] écrire l'introduction
- [ ] trouver une base de données

## Articles

https://www-public.telecom-sudparis.eu/~horain/ARC-LSF/Rapport_Stage_Deslandes.pdf
https://hal.science/hal-01332141/document
https://www.nature.com/articles/s41598-023-43852-x
https://arxiv.org/ftp/arxiv/papers/2201/2201.01486.pdf
https://link.springer.com/chapter/10.1007/978-981-19-7126-6_11
https://www.researchgate.net/publication/325011717_Sign_Language_Recognition_based_on_Hand_and_Body_Skeletal_Data/link/5af160e3a6fdcc24364b1024/download


https://data-flair.training/blogs/sign-language-recognition-python-ml-opencv/
https://www.researchgate.net/publication/227166112_Sign_Language_Recognition
https://ieeexplore.ieee.org/abstract/document/7916786?casa_token=ge_cWHZcE44AAAAA:Eh-wPyn0OtcOEQE3z_Jd4sP78azCBUNQeuqpf_GBNPcWRlaSTRn35v9VFTfS6I6EAOfm2-oaUN0i
https://ieeexplore.ieee.org/abstract/document/9990643?casa_token=4rPG-1-XEGkAAAAA:6whOuhyMenlHDDZ2x4gAXAyBt_1LjUd6rx3fRs6TuNbBhYwZzjLzjhe_IGpMcDYVfuhKHSqa_G58
https://ieeexplore.ieee.org/abstract/document/10178445?casa_token=I63VbDp2ZFUAAAAA:ofgAxFaRWliYIDx6hyDdSGtBpCsFBKTz3s72NMKV6CqmhGp297fmn5kJc2mKTLmzhpEetTOhSlWF

## Utilization

### Obtain the database

For this work, we use the train and test set downloadable on this [*Kaggle* notebook](https://www.kaggle.com/datasets/debashishsau/aslamerican-sign-language-aplhabet-dataset?resource=download).

Then we put both folders (train and test set) of the *zip* file on the folder `dataset/`.

Larger test dataset:
https://public.roboflow.com/object-detection/american-sign-language-letters/1

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

MobileNetV2, 6 époques, contours : 69% d'accuracy, 88% d'accuracy sur 3

MobileNetV2, 8 époques, contours : 71% d'accuracy, 88% d'accuracy sur 3
MobileNetV2, 8 époques, sans contours, HSV, avec background : xx% d'accuracy, xx% d'accuracy sur 3
MobileNetV2, 8 époques, sans contours, HSV : 51% d'accuracy, 78% d'accuracy sur 3
MobileNetV2, 8 époques, contours, HSV : 64% d'accuracy, 82% d'accuracy sur 3
MobileNetV2, 8 époques, contours, HSV, avec background : 35% d'accuracy, 56% d'accuracy sur 3
MobileNetV2, 8 époques, sans contours, HSV, avec background : 22% d'accuracy, 42% d'accuracy sur 3
MobileNetV2, 8 époques, sans contours, avec background : 27% d'accuracy, 53% d'accuracy sur 3
MobileNetV2, 8 époques, contours, avec background : 48% d'accuracy, 72% d'accuracy sur 3

MobileNetV2, 10 époques, contours : 70% d'accuracy, 88% d'accuracy sur 3
MobileNetV2, 10 époques, contours, HSV : 64% d'accuracy, 83% d'accuracy sur 3
MobileNetV2, 10 époques, sans contours, HSV : 51% d'accuracy, 76% d'accuracy sur 3





CNN, 3 époques, contours : 47% d'accuracy, 69% d'accuracy sur 3

Résultats sur la vidéo :
MobileNetV2, 8 époques, contours, anciens datasets : 95 mots bien retrouvés sur 295
[10, 5, 9, 1, 8, 2, 5, 1, 6, 9, 1, 1, 3, 1, 1, 2, 1, 9, 1, 2, 2, 6, 3, 9, 5, 2, 3, 5, 2, 5, 1, 3, 10, 1, 3, 2, 5, 3, 2, 1, 3, 5, 5, 8, 10, 2, 5, 6, 1, 3, 2, 1, 1, 2, 1, 8, 10, 6, 2, 1, 4, 1, 1, 6, 1, 1, 3, 1, 7, 10, 2, 1, 10, 1, 5, 8, 3, 7, 4, 1, 5, 1, 4, 3, 6, 6, 2, 1, 9, 5, 2, 10, 2, 6, 1]
