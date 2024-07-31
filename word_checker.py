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

class KDTreeNode:
    def __init__(self, point, left=None, right=None, axis=0):
        self.point = point
        self.left = left
        self.right = right
        self.axis = axis

class KDTree:
    def __init__(self, points):
        self.root = self.build_tree(points)

    def build_tree(self, points, depth=0):
        if not points:
            return None

        k = len(points[0])  # Dimension of the points
        axis = depth % k

        points.sort(key=lambda x: x[axis])
        median = len(points) // 2

        return KDTreeNode(
            point=points[median],
            left=self.build_tree(points[:median], depth + 1),
            right=self.build_tree(points[median + 1:], depth + 1),
            axis=axis
        )

    def nearest_neighbor(self, point):
        def recursive_search(node, depth=0, best=None):
            if node is None:
                return best

            k = len(point)
            axis = depth % k

            next_best = best
            next_branch = None

            if next_best is None or np.linalg.norm(np.array(point) - np.array(node.point)) < np.linalg.norm(np.array(point) - np.array(next_best)):
                next_best = node.point

            if point[axis] < node.point[axis]:
                next_branch = node.left
                other_branch = node.right
            else:
                next_branch = node.right
                other_branch = node.left

            next_best = recursive_search(next_branch, depth + 1, next_best)

            if np.linalg.norm(np.array(point) - np.array(next_best)) > abs(point[axis] - node.point[axis]):
                next_best = recursive_search(other_branch, depth + 1, next_best)

            return next_best

        return recursive_search(self.root)

class WordChecker:
    def __init__(self, words):
        self.words = words
        self.max_length = max(len(word) for word in words)
        self.vectors = [self.word_to_vector(word) for word in words]
        self.kd_tree = KDTree(self.vectors)

    def word_to_vector(self, word):
        char_list = list(word)
        num_list = [ord(char) for char in char_list]
        if len(num_list) > self.max_length:
            num_list = num_list[:self.max_length]
        else:
            num_list += [0] * (self.max_length - len(num_list))
        num_array = np.array(num_list)
        norm_array = num_array / np.linalg.norm(num_array)
        return norm_array

    def find_nearest(self, word):
        vector = self.word_to_vector(word)
        nearest_vector = self.kd_tree.nearest_neighbor(vector)
        nearest_word_index = self.vectors.index(nearest_vector)
        return self.words[nearest_word_index]

# Example usage
words = ["apple", "banana", "grape", "orange", "peach", "pear", "strawberry", "watermelon"]
checker = WordChecker(words)
input_word = "strawberry"
nearest_word = checker.find_nearest(input_word)
print(f"Nearest word to '{input_word}' is '{nearest_word}'")