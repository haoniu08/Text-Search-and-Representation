"""
This file contains a basic program which resembles a word checker. 
The word checker implemments ball-tree while using nearest neighbour
search to find the closest word to the input word.
"""

import numpy as np

class BallTreeNode:
    def __init__(self, points, left=None, right=None):
        self.points = points
        self.left = left
        self.right = right
        self.center = None
        self.radius = None
        if points:
            self.center = np.mean(points, axis=0)
            self.radius = np.max(np.linalg.norm(points - self.center, axis=1))

class BallTree:
    def __init__(self, points):
        self.root = self.build_tree(points)
    
    def build_tree(self, points):
        if len(points) <= 1:
            return BallTreeNode(points)
        
        # Split the data into two subsets
        indices = np.random.permutation(len(points))
        mid = len(points) // 2
        left_indices = indices[:mid]
        right_indices = indices[mid:]
        
        left_points = points[left_indices]
        right_points = points[right_indices]
        
        left_child = self.build_tree(left_points)
        right_child = self.build_tree(right_points)
        
        # Create the root node of this subtree
        node = BallTreeNode(points)
        node.left = left_child
        node.right = right_child
        
        return node

    def nearest_neighbor(self, point):
        return self._nearest_neighbor(self.root, point)

    def _nearest_neighbor(self, node, point, best=None, best_dist=float('inf')):
        if node is None:
            return best, best_dist

        # Calculate distance to the center of the ball
        dist_to_center = np.linalg.norm(point - node.center)

        # Check if the ball might contain the nearest neighbor
        if dist_to_center - node.radius < best_dist:
            for p in node.points:
                dist = np.linalg.norm(point - p)
                if dist < best_dist:
                    best = p
                    best_dist = dist

            # Recurse on the child nodes
            best, best_dist = self._nearest_neighbor(node.left, point, best, best_dist)
            best, best_dist = self._nearest_neighbor(node.right, point, best, best_dist)

        return best, best_dist

class WordChecker:
    def __init__(self, words):
        self.words = words
        self.max_length = max(len(word) for word in words)
        self.vectors = np.array([self.word_to_vector(word) for word in words])
        self.ball_tree = BallTree(self.vectors)

    def word_to_vector(self, word):
        char_list = list(word)
        num_list = [ord(char) for char in char_list]
        if len(num_list) > self.max_length:
            num_list = num_list[:self.max_length]
        else:
            num_list += [0] * (self.max_length - len(num_list))
        num_array = np.array(num_list, dtype=np.float32)
        return num_array

    def find_nearest(self, word):
        vector = self.word_to_vector(word)
        print(f"Input word vector: {vector}")
        nearest_vector, distance = self.ball_tree.nearest_neighbor(vector)
        print(f"Nearest vector found: {nearest_vector}")
        
        # Find the index of the nearest vector
        nearest_word_index = -1
        for i, vec in enumerate(self.vectors):
            if np.array_equal(vec, nearest_vector):
                nearest_word_index = i
                break
                
        return self.words[nearest_word_index]

# Example usage
words = ["apple", "banana", "grape", "orange", "peach", "pear"]
checker = WordChecker(words)
input_word = "strawberry"
nearest_word = checker.find_nearest(input_word)
print(f"Nearest word to '{input_word}' is '{nearest_word}'")



