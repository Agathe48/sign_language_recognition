"""
Tools Python file with the metrics to evaluate the performance of the pipeline.
"""

###############
### Imports ###
###############

### Python imports ###

import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt
import os

### Local imports ###

from tools.tools_constants import (
    LIST_LETTERS_STATIC,
    PATH_RESULTS,
    NUMBER_EPOCHS
)

#################
### Functions ###
#################

def analyse_predictions(predictions, number_elements_to_take=3):
    predicted_labels = []

    for prediction in predictions:
        sorted_id = np.argsort(prediction)[::-1]
        first_elements = sorted_id[:number_elements_to_take]

        list_predicted_letters = [LIST_LETTERS_STATIC[id] for id in first_elements]
        predicted_labels.append(list_predicted_letters)
    
    return predicted_labels

def compute_accuracy(predicted_labels, test_labels):
    score = 0
    for counter in range(len(test_labels)):
        type_image = test_labels[counter]
        if type_image in predicted_labels[counter]:
            score += 1
    accuracy = score / len(test_labels)
    accuracy = round(accuracy, 2)

    print(accuracy)
    return accuracy

def display_confusion_matrix(predicted_labels, test_labels):
    confusion_matrix = metrics.confusion_matrix(test_labels, predicted_labels)
    cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = test_labels)
    cm_display.plot()

    isExist = os.path.exists(PATH_RESULTS + 'mobilenetv2/')
    if not isExist:
        os.makedirs(PATH_RESULTS + 'mobilenetv2/')

    plt.savefig(PATH_RESULTS + 'mobilenetv2/'+ "E" + str(NUMBER_EPOCHS) + "_confusion_matrix.png")
