"""
Main Python file to perform the sign language recognition.
"""

###############
### Imports ###
###############

### Python imports ###

import os

### Local imports ###

from tools.tools_constants import (
    PATH_MODELS,
    TRAIN_MODE,
    NUMBER_EPOCHS,
    BATCH_SIZE,
    PATH_RESULTS,
    MODEL_NAME,
    BOOL_PREPROCESSING_CONTOURS
)
from tools.tools_dataset import (
    create_train_val_set,
    create_test_set
)
from tools.tools_metrics import (
    analyse_predictions,
    compute_accuracy,
    display_confusion_matrix,
    display_training_accuracy
)
from tools.tools_models import (
    create_mobilenetv2,
    create_cnn
)
from tools.tools_preprocessing import (
    normalize_dataset,
    extract_contours
)

#################
### Main code ###
#################

isExist = os.path.exists(PATH_RESULTS + 'mobilenetv2/')
if not isExist:
    os.makedirs(PATH_RESULTS + 'mobilenetv2/')

### Data loading ###

print("Load dataset")

train_set, validation_set = create_train_val_set()
test_images, test_labels = create_test_set()

### Preprocessing ###

train_set, validation_set = normalize_dataset(
    train_set=train_set,
    validation_set=validation_set
)

if BOOL_PREPROCESSING_CONTOURS:
    train_set, validation_set = extract_contours(
        train_set=train_set,
        validation_set=validation_set
    )

### Training ###

if MODEL_NAME == "mobilenetv2":
    model = create_mobilenetv2()
elif MODEL_NAME == "cnn":
    model = create_cnn()

path_to_save = PATH_MODELS + MODEL_NAME + '/E'+ str(NUMBER_EPOCHS)
if BOOL_PREPROCESSING_CONTOURS:
    path_to_save += "_contours"

if TRAIN_MODE:
    print("Train model")
    history = model.fit(
        train_set,
        batch_size=BATCH_SIZE,
        validation_data=validation_set,
        epochs=NUMBER_EPOCHS,
        verbose=1)

    model_history = history.history
    display_training_accuracy(model_history, path_to_save)

    # Save the weights of the trained model
    print("Save model")
    model.save_weights(path_to_save + "/")

else:
    # Restore the weights
    print("Load model")
    model.load_weights(path_to_save + "/")

### Predictions ###

print("Predict labels")

predictions = model.predict(test_images)
predicted_classes_3 = analyse_predictions(
    predictions=predictions,
    number_elements_to_take=3)
predicted_classes_1 = analyse_predictions(
    predictions=predictions,
    number_elements_to_take=1)

### Metrics ###

compute_accuracy(
    predicted_labels=predicted_classes_3,
    test_labels=test_labels)

compute_accuracy(
    predicted_labels=predicted_classes_1,
    test_labels=test_labels)

display_confusion_matrix(
    predicted_labels=[element[0] for element in predicted_classes_1],
    test_labels=test_labels,
    path_to_save=path_to_save
)
