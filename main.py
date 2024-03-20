"""
Main Python file to perform the sign language recognition.
"""

###############
### Imports ###
###############

### Python imports ###

import tensorflow as tf

### Local imports ###

from tools.tools_constants import (
    PATH_MODELS,
    TRAIN_MODE,
    NUMBER_EPOCHS,
    BATCH_SIZE,
    NUMBER_BATCHES_TRAINING
)
from tools.tools_dataset import (
    create_train_val_set,
    create_test_set,
    reduce_size_dataset
)
from tools.tools_metrics import (
    analyse_predictions
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
        PATH_MODELS + 'mobilenetv2/'+ "E" + str(NUMBER_EPOCHS) + "_N" + str(NUMBER_BATCHES_TRAINING) + "/")

else:
    print("Load model")

    # Restore the weights
    model.load_weights(
        PATH_MODELS + 'mobilenetv2/'+ "E" + str(NUMBER_EPOCHS) + "_N" + str(NUMBER_BATCHES_TRAINING) + "/")

### Predictions ###

print("Predict labels")

predictions = model.predict(test_images)
predicted_classes = analyse_predictions(predictions=predictions)

print(predicted_classes)
print(test_labels)

### Metrics ###
