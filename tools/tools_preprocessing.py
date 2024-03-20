"""
Tools Python file to perform preprocessing on images.
"""

###############
### Imports ###
###############

### Python imports ###

import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
# from rembg import remove 
from PIL import Image 
  

### Local imports ###

#################
### Functions ###
#################

def normalize_dataset(train_set, validation_set):
    normalization_layer = tf.keras.layers.Rescaling(1./255)
    normalized_train_set = train_set.map(lambda x, y: (normalization_layer(x), y))
    normalized_val_set = validation_set.map(lambda x, y: (normalization_layer(x), y))

    return normalized_train_set, normalized_val_set

def gray_scale(img):
    img_gray= cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return img_gray


def remove_background(folder_path):

    # Store path of the image in the variable input_path 
    input_path =  file_name
    
    # Store path of the output image in the variable output_path 
    output_path = 'output.png' 
    
    # Processing the image 
    input = Image.open(input_path) 
    
    # Removing the background from the given Image 
    output = remove(input) 
    
    #Saving the image in the given path 
    output.save(output_path) 

def canny_detector(img, min_threshold, max_threshold, edges = 5):
    # contour detector
    img_canny = cv2.Canny(img, min_threshold, max_threshold, edges = edges)
    return img_canny

def laplacian_detector(img_gray):
    # contour detector
    laplacian = cv2.Laplacian(img_gray,cv2.CV_64F)
    return laplacian

def sobelx_detector(img_gray, ksize = 5):
    # contour detector
    sobelx = cv2.Sobel(img_gray,cv2.CV_64F, 1, 0, ksize = ksize)
    return sobelx

def sobely_detector(img_gray, ksize = 5):
    # contour detector
    sobely = cv2.Sobel(img_gray,cv2.CV_64F, 0, 1, ksize = ksize)
    return sobely

def plot_canny_img(img, img_canny):
    plt.subplot(1,2,1),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(1,2,2),plt.imshow(img_canny ,cmap = 'gray')
    plt.title('OpenCv Canny'), plt.xticks([]), plt.yticks([])
    plt.show()
