"""
Main Python file to perform the sign language recognition.
"""

###############
### Imports ###
###############

### Local imports ###

from tools.tools_constants import (
    PATH_MODELS,
    TRAIN_MODE,
    NUMBER_EPOCHS,
    BATCH_SIZE
)
from tools.tools_dataset import (
    create_train_val_set,
    create_test_set
)
from tools.tools_metrics import (
    analyse_predictions,
    compute_accuracy,
    display_confusion_matrix
)
from tools.tools_models import (
    create_mobilenetv2
)
from tools.tools_preprocessing import (
    normalize_dataset
)

#################
### Main code ###
#################

### Data loading ###

print("Load dataset")

train_set, validation_set = create_train_val_set()
test_images, test_labels = create_test_set()

### Preprocessing ###

train_set, validation_set = normalize_dataset(
    train_set=train_set,
    validation_set=validation_set
)

### Training ###

model = create_mobilenetv2()

if TRAIN_MODE:
    print("Train model")
    model_fit = model.fit(
        train_set,
        batch_size=BATCH_SIZE,
        validation_data=validation_set,
        epochs=NUMBER_EPOCHS,
        verbose=1)

    # Save the weights of the trained model
    print("Save model")
    model.save_weights(
        PATH_MODELS + 'mobilenetv2/'+ "E" + str(NUMBER_EPOCHS) + "/")

else:
    print("Load model")

    # Restore the weights
    model.load_weights(
        PATH_MODELS + 'mobilenetv2/'+ "E" + str(NUMBER_EPOCHS) + "/")

### Predictions ###

print("Predict labels")

predictions = model.predict(test_images)
predicted_classes_3 = analyse_predictions(predictions=predictions)
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
    test_labels=test_labels
)

