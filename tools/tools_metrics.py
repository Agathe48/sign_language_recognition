"""
Tools Python file with the metrics to evaluate the performance of the pipeline.
"""

###############
### Imports ###
###############

### Python imports ###

import numpy as np

### Local imports ###

from tools.tools_constants import (
    LIST_LETTERS_STATIC
)

#################
### Functions ###
#################

def analyse_predictions(predictions):
    predicted_classes = []

    for prediction in predictions:
        sorted_id = np.argsort(prediction)[::-1]
        first_elements = sorted_id[:3]

        list_predicted_letters = [LIST_LETTERS_STATIC[id] for id in first_elements]
        predicted_classes.append(list_predicted_letters)
    
    return predicted_classes
