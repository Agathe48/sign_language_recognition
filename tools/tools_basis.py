"""
Tools Python file to deal with basic functions.
"""

###############
### Imports ###
###############

### Python imports ###

import json

#################
### Functions ###
#################

def load_json_file(file_path: str) -> dict:
    """
    Load a json file, according the specified path.

    Parameters
    ----------
    file_path : str
        Path of the json file

    Returns
    -------
    res : dict
        Content of the json file
    """
    with open(file_path, "r", encoding="utf-8") as file:
        res = json.load(file)
    return res

def save_json_file(file_path: str, dict_to_save: dict) -> None:
    """
    Save the content of the given dictionary inside the specified json file.

    Parameters
    ----------
    file_path : str
        Path of the json file
    dict_to_save : dict
        Dictionary to save

    Returns
    -------
    None
    """
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(dict_to_save, file, indent=4)
