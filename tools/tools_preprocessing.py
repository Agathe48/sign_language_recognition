"""
Tools Python file to perform preprocessing on images.
"""

###############
### Imports ###
###############

### Python imports ###

import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
from rembg import remove 
import os
from PIL import Image
from tqdm import tqdm
import sys
sys.path.append("./")
import numpy as np
  
### Local imports ###

from tools.tools_constants import (
    BOOL_HSV,
    BOOL_LAB,
    BOOL_XYZ
)

#################
### Functions ###
#################

def load_image(src, show = True):
    """
    Load an image from the specified path.

    Parameters
    ----------
    src : str
        Path of the image
    show : bool

    Returns
    -------
    rgb : np.array
        Image in RGB format
    """
    img=cv2.imread(src,1)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    if show : 
        plt.imshow(rgb,interpolation='nearest')
        plt.show()
    return rgb

def calcul_histogram(I,color):
    """
    Calculate the histogram of an image.

    Parameters
    ----------
    I : np.array
        Image to analyze
    color : list
        List of colors to analyze

    Returns
    -------
    None
    """
    for i,col in enumerate(color):
        histr = cv2.calcHist([I],[i],None,[256],[0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])
    plt.show()

def remove_background(folder_path, folder_destination, file_mode=True):
    """
    Remove the background of an image.

    Parameters
    ----------
    folder_path : str
        Path of the folder containing the images
    folder_destination : str
        Path of the folder to save the images
    file_mode : bool
        If True, the function will remove the background of the images in the folder_path.

    Returns
    -------
    None
    """
    if not os.path.exists(folder_destination):
        os.makedirs(folder_destination)
    if not file_mode:
        for folder in tqdm(os.listdir(folder_path)):
            for file in tqdm(os.listdir(folder_path + folder)):
                if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
                    file_path = folder_path + folder + '/' + file
                    input = Image.open(file_path) 
                    output = remove(input) 
                    if not os.path.exists(folder_destination + '/' + folder):
                        os.makedirs(folder_destination + '/' + folder)
                    filename, extension = os.path.splitext(file)
                    output.save(folder_destination + '/' + folder + '/' + filename + '.png')
    else:
        for file in tqdm(os.listdir(folder_path)):
            if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
                file_path = folder_path + file
                input = Image.open(file_path) 
                output = remove(input) 
                if not os.path.exists(folder_destination):
                    os.makedirs(folder_destination)
                filename, extension = os.path.splitext(file)
                output.save(folder_destination + filename + '.png')

def canny_detector(img, min_threshold = 40, max_threshold = 100, edges = 5):
    """
    Detect the contours of an image.

    Parameters
    ----------
    img : np.array
        Image to analyze
    min_threshold : int
        Minimum threshold for the Canny detector
    max_threshold : int
        Maximum threshold for the Canny detector
    edges : int
        Number of edges

    Returns
    -------
    img_canny : np.array
        Image with the contours
    """
    # contour detector
    img_canny = cv2.Canny(img, min_threshold, max_threshold, edges = edges)
    return img_canny

def laplacian_detector(img_gray):
    """
    Detect the contours of an image using the Laplacian detector.

    Parameters
    ----------
    img_gray : np.array
        Image in grayscale
    
    Returns
    -------
    laplacian : np.array
        Image with the contours
    """
    # contour detector
    laplacian = cv2.Laplacian(img_gray,cv2.CV_64F)
    return laplacian

def sobelx_detector(img_gray, ksize = 5):
    """
    Detect the contours of an image using the Sobel detector.

    Parameters
    ----------
    img_gray : np.array
        Image in grayscale
    ksize : int
        Size of the kernel
    
    Returns
    -------
    sobelx : np.array
        Image with the contours
    """
    # contour detector
    sobelx = cv2.Sobel(img_gray,cv2.CV_64F, 1, 0, ksize = ksize)
    return sobelx

def sobely_detector(img_gray, ksize = 5):
    """
    Detect the contours of an image using the Sobel detector.

    Parameters
    ----------
    img_gray : np.array
        Image in grayscale
    ksize : int
        Size of the kernel
    
    Returns
    -------
    sobely : np.array
        Image with the contours
    """
    # contour detector
    sobely = cv2.Sobel(img_gray,cv2.CV_64F, 0, 1, ksize = ksize)
    return sobely

def plot_canny_img(img, img_canny):
    """
    Plot the original image and the image with the contours.

    Parameters
    ----------
    img : np.array
        Original image
    img_canny : np.array
        Image with the contours
    
    Returns
    -------
    None
    """
    plt.subplot(1,2,1),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(1,2,2),plt.imshow(img_canny ,cmap = 'gray')
    plt.title('OpenCv Canny'), plt.xticks([]), plt.yticks([])
    plt.show()

def extract_contours(train_images, validation_images):
    """
    Preprocessing pipeline to extract contours from an image.

    Parameters
    ----------
    train_images : np.array
        Training images
    validation_images : np.array
        Validation images
    
    Returns
    -------
    np.array
        Training images with the contours
    """
    canny_train_images = []
    canny_val_images = []

    for element in tqdm(train_images):
        canny_train_images.append(canny_detector(element))
    for element in tqdm(validation_images):
        canny_val_images.append(canny_detector(element))

    return np.array(canny_train_images), np.array(canny_val_images)

