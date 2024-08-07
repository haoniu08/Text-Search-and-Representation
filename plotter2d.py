import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np

def plot_words(vectors, words, input_word=None):
    # Project vectors to 2D
    pca = PCA(n_components=2)
    vectors_2d = pca.fit_transform(vectors)

    fig, ax = plt.subplots()
    ax.scatter(vectors_2d[:, 0], vectors_2d[:, 1], color='blue', label='Words')

    for i, word in enumerate(words):
        ax.annotate(word, (vectors_2d[i, 0], vectors_2d[i, 1]))

    if input_word:
        input_vector = vectors_2d[-1]
        ax.scatter(input_vector[0], input_vector[1], color='red', label='Input Word')
        ax.annotate(input_word, (input_vector[0], input_vector[1]), color='red')

    plt.xlabel('Dimension 1')
    plt.ylabel('Dimension 2')
    plt.title('2D Visualization of Words')
    plt.legend()
    plt.show()