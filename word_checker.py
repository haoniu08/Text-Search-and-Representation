import numpy as np
import time
from ball_tree import BallTree
from kd_tree import KDTree

class WordChecker:
    def __init__(self, words, vectorization_type, tree_type):
        self.words = words
        self.vectorization_type = vectorization_type
        self.tree_type = tree_type
        self.max_length = max(len(word) for word in words)
        self.vectors = [self.word_to_vector(word) for word in words]

        if self.tree_type == "KD_TREE":
            self.kd_tree = KDTree(self.vectors)
        elif self.tree_type == "BALL_TREE":
            self.ball_tree = BallTree(self.vectors)
        else:
            raise ValueError("Invalid tree type")
    
    def word_to_vector(self, word):
        if self.vectorization_type == "NAIVE":
            return self.naive_vectorization(word)
        elif self.vectorization_type == "NAIVE_REPEAT":
            return self.naive_repeat_vectorization(word)
        elif self.vectorization_type == "BINARY":
            return self.binary_vectorization(word)
        elif self.vectorization_type == "BINARY_REPEAT":
            return self.binary_repeat_vectorization(word)
        
    def naive_vectorization(self, word):
        num_list = [ord(char) - ord('a') + 1 for char in word.lower()]
        if len(num_list) > self.max_length:
            num_list = num_list[:self.max_length]
        else:
            num_list += [0] * (self.max_length - len(num_list))

        return np.array(num_list, dtype=np.float32)
    

    def naive_repeat_vectorization(self, word):

        base_vector = self.naive_vectorization(word)
        
        repeated_vector = np.tile(base_vector, 10)

        for i in range(1, 10):
            repeated_vector[i*self.max_length:(i+1)*self.max_length] = (
            repeated_vector[i*self.max_length:(i+1)*self.max_length] * (i + 1) + 
            np.sin(repeated_vector[:self.max_length] * np.pi / 4)
        )

        return repeated_vector
    

    def binary_vectorization(self, word):
        vector = np.zeros(26, dtype=np.float32)
        for char in word.lower():
            index = ord(char) - ord('a')
            if 0 <= index < 26:
                vector[index] = 1
        return vector
    
    def binary_repeat_vectorization(self, word):
        vector = np.zeros(26, dtype=np.float32)
        for char in word.lower():
            index = ord(char) - ord('a')
            if 0 <= index < 26:
                vector[index] = 1
        
        vector_260 = np.tile(vector, 10)

        for i in range(1, 10):
            vector_260[i*26:(i+1)*26] = vector_260[i*26:(i+1)*26] * (i+1) + np.sin(vector_260[:26] * np.pi / 4)

        return vector_260
    
    def print_word_vectors(self):
        print(f"Vectorization type: {self.vectorization_type}")
        for word, vector in zip(self.words, self.vectors):
            print(f"Word: {word}, Vector: {vector}")

    def find_nearest(self, word):
        vector = self.word_to_vector(word)
        if self.tree_type == "KD_TREE":
            nearest_vector, _ = self.kd_tree.nearest_neighbor(vector)
        elif self.tree_type == "BALL_TREE":
            nearest_vector, _ = self.ball_tree.nearest_neighbor(vector)
            
        for i, vec in enumerate(self.vectors):
            if np.array_equal(vec, nearest_vector):
                nearest_word_index = i
                break
        return self.words[nearest_word_index]
    
    def search_word(self, input_word): 
        start_time = time.time()
        nearest_word = self.find_nearest(input_word)
        query_time = time.time() - start_time

        return nearest_word, round(query_time, 4)
    
    def measure_performance(self, input_word, num_times):
        runtime = []
        correct_hits = 0
        for i in range(num_times):
            nearest_word, query_time = self.search_word(input_word)
            runtime.append(query_time)
            if nearest_word == input_word:
                correct_hits += 1
            
            avg_runtime = round (sum(runtime) / num_times, 8)
            accuracy_percentage = correct_hits / num_times * 100

        return avg_runtime, accuracy_percentage, correct_hits 




        
    

        