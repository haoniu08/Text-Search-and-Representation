"""
This file contains a basic program which resembles a word checker. 
The word checker implemments both kd-tree and ball-tree, while using 
nearest neighbour search to find the closest word to the input word.

The vector representation is manually implemented, and the word is converted
to a vector using the following method:
    - The word is first converted to a list of characters
    - Each character is then converted to a number by using the ord() function
    - The list of numbers is then converted to a numpy array
    - The numpy array is then reshaped to a 2D array with 1 row and n columns
    - The 2D array is then normalized using the L2 norm
    - The 2D array is then returned

The word checker is then used to find the closest word to the input word by
using the following method:
    - The input word is first converted to a vector using the method above
    - The vector is then used to find the nearest neighbour using the kd-tree
    - The nearest neighbour is then returned

The word checker is then tested using a list of words, and the closest word
to each word is printed to the console.
"""

import numpy as np
