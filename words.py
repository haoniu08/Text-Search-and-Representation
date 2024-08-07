import nltk
nltk.download('words')
from nltk.corpus import words

fruits = ["apple", "banana", "grape", "orange", "peach", "pear", "pineapple", "plum", "strawberry",
           "watermelon", "kiwi", "mango", "papaya", "blueberry", "blackberry", "raspberry", "cherry",
           "apricot", "cantaloupe", "honeydew", "nectarine", "grapefruit", "lemon", "lime", "tangerine"]

fruits.sort()

middle_fruit = fruits[len(fruits) // 2]

three_letter_names = [ "Abe", "Ben", "Cal", "Dan", "Eli", "Fay", "Gus", "Hal", "Ian", "Jim", "Kay", "Leo", "Mia",
                     "Ned", "Ola", "Pam", "Qui", "Ray", "Sam", "Tom", "Uma", "Vic", "Wes", "Xia", "Yas", "Zoe"]

middle_three_letter_name = three_letter_names[12]

# Get a list of unique English words from NLTK
all_words = list(set(words.words()))

# Sort the list of words, alphabetically
all_words.sort()

# Get the maximum length of a word in the list
max_length = max(len(word) for word in all_words)
# print(f"Max word length: {max_length}")

middle_word_in_list = all_words[max_length // 2]

# Get those words that are only 3 letters long
three_letter_words = [word for word in all_words if len(word) == 3]

# Sort the list of 3-letter words, alphabetically
three_letter_words.sort()

middle_three_letter_word = three_letter_words[len(three_letter_words) // 2]

# Get all the 10-letter words
ten_letter_words = [word for word in all_words if len(word) == 10]

# Sort the list of 10-letter words, alphabetically
ten_letter_words.sort()

middle_ten_letter_word = ten_letter_words[len(ten_letter_words) // 2]


