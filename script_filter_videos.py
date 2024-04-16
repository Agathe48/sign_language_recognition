"""
Python file to filter the videos by removing the words with j and z.
"""

###############
### Imports ###
###############

### Python imports ###

import os

### Local imports ###

from tools.tools_constants import (
    PATH_VIDEOS,
    LIST_WORDS,
    LIST_LETTERS_STATIC,
    PATH_LIST_WORDS_CLEAN
)

def clean_videos_with_z_and_j():
    """
    Clean the videos by removing the words with j and z.

    Parameters
    ----------
    None
    
    Returns
    -------
    None
    """
    with open(PATH_LIST_WORDS_CLEAN,"w") as file:
        for idx,word in enumerate(LIST_WORDS):
            print(f"Processing {idx} {word}")
            save = True
            for letter in word:
                if not letter.upper() in LIST_LETTERS_STATIC:
                    save = False
                    os.remove(PATH_VIDEOS + str(idx) + "_" + word + ".avi")
            
            if save:
                file.write(f"{idx},{word}\n")

clean_videos_with_z_and_j()
