import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
import numpy as np
import words

def plot_words_3d(vectors, words, input_word=None):
    # Project vectors to 3D
    pca = PCA(n_components=3)
    vectors_3d = pca.fit_transform(vectors)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(vectors_3d[:, 0], vectors_3d[:, 1], vectors_3d[:, 2], color='blue', label='Words')

    for i, word in enumerate(words):
        ax.text(vectors_3d[i, 0], vectors_3d[i, 1], vectors_3d[i, 2], word)

    if input_word:
        input_vector = vectors_3d[-1]
        ax.scatter(input_vector[0], input_vector[1], input_vector[2], color='red', label='Input Word')
        ax.text(input_vector[0], input_vector[1], input_vector[2], input_word, color='red')

    ax.set_xlabel('Dimension 1')
    ax.set_ylabel('Dimension 2')
    ax.set_zlabel('Dimension 3')
    ax.set_title('3D Visualization of Words')
    ax.legend()
    plt.show()

words_3 = ["Abe", "Ben", "Cal", "Dan", "Eli", "Fay", "Gus", "Hal", "Ian", "Jim", "Kay", "Leo", "Mia", "Ned", "Ola", "Pam", "Quin", "Ray", "Sam", "Tom", "Uma", "Vic", "Wes", "Xia", "Yas", "Zoe"]

# random vectors here for demonstration
vectors = np.random.rand(26, 50)  

three_d_words = words.three_letter_words

print(three_d_words)

plot_words_3d(vectors, three_d_words, input_word="Abe")
