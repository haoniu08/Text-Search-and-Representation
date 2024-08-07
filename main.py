
from word_checker import WordChecker
import words

NAIVE = "NAIVE"
NAIVE_REPEAT = "NAIVE_REPEAT"
BINARY = "BINARY"
BINARY_REPEAT = "BINARY_REPEAT"

KD_TREE = "KD_TREE"
BALL_TREE = "BALL_TREE"

all_words = words.all_words
max_length = words.max_length
print (max_length)

three_letter_names = words.three_letter_names
fruits = words.fruits

three_letter_words = words.three_letter_words
ten_letter_words = words.ten_letter_words

# Performance test for kd tree
checker_names_naive = WordChecker(three_letter_names, NAIVE, KD_TREE)
checker_fruits_naive = WordChecker(fruits, NAIVE, KD_TREE)

checker_three_letter_naive = WordChecker(three_letter_words, NAIVE, KD_TREE)
checker_three_letter_naive_repeat = WordChecker(three_letter_words, NAIVE_REPEAT, KD_TREE)
checker_three_letter_binary = WordChecker(three_letter_words, BINARY, KD_TREE)
checker_three_letter_binary_repeat = WordChecker(three_letter_words, BINARY_REPEAT, KD_TREE)

checker_ten_letter_naive = WordChecker(ten_letter_words, NAIVE, KD_TREE)
checker_ten_letter_naive_repeat = WordChecker(ten_letter_words, NAIVE_REPEAT, KD_TREE)
checker_ten_letter_binary = WordChecker(ten_letter_words, BINARY, KD_TREE)
checker_ten_letter_binary_repeat = WordChecker(ten_letter_words, BINARY_REPEAT, KD_TREE)

checker_all_words_naive = WordChecker(all_words, NAIVE, KD_TREE)
checker_all_words_naive_repeat = WordChecker(all_words, NAIVE_REPEAT, KD_TREE)
checker_all_words_binary = WordChecker(all_words, BINARY, KD_TREE)
checker_all_words_binary_repeat = WordChecker(all_words, BINARY_REPEAT, KD_TREE)


avg_time, accuracy, correct_hits = checker_names_naive.measure_performance(words.middle_three_letter_name, 1)
print(
    "Performance test for three letter names using naive approach with kd-tree:\n"
    "Words count: ", len(three_letter_names), "Time: ", avg_time, ", Accuracy: ", accuracy, ", Correct hits: ", correct_hits
)


avg_time, accuracy, correct_hits = checker_fruits_naive.measure_performance(words.middle_fruit, 1)
print(
    "Performance test for fruits using naive approach with kd-tree:\n"
    "Words count: ", len(fruits), "Time: ", avg_time, ", Accuracy: ", accuracy, ", Correct hits: ", correct_hits
)

avg_time, accuracy, correct_hits = checker_three_letter_naive.measure_performance(words.middle_three_letter_word, 1)
print(
    "Performance test for three letter words using naive approach with kd-tree:\n"
    "Words count: ", len(three_letter_words), "Time: ", avg_time, ", Accuracy: ", accuracy, ", Correct hits: ", correct_hits
)

avg_time, accuracy, correct_hits = checker_three_letter_naive_repeat.measure_performance(words.middle_three_letter_word, 1)
print(
    "Performance test for three letter words using naive repeat approach with kd-tree:\n"
    "Words count: ", len(three_letter_words), "Time: ", avg_time, ", Accuracy: ", accuracy, ", Correct hits: ", correct_hits
)

avg_time, accuracy, correct_hits = checker_three_letter_binary.measure_performance(words.middle_three_letter_word, 1)
print(
    "Performance test for three letter words using binary approach with kd-tree:\n"
    "Words count: ", len(three_letter_words), "Time: ", avg_time, ", Accuracy: ", accuracy, ", Correct hits: ", correct_hits
)

avg_time, accuracy, correct_hits = checker_three_letter_binary_repeat.measure_performance(words.middle_three_letter_word, 1)
print(
    "Performance test for three letter words using binary repeat approach with kd-tree:\n"
    "Words count: ", len(three_letter_words), "Time: ", avg_time, ", Accuracy: ", accuracy, ", Correct hits: ", correct_hits
)

avg_time, accuracy, correct_hits = checker_ten_letter_naive.measure_performance(words.middle_ten_letter_word, 1)
print(
    "Performance test for ten letter words using naive approach with kd-tree:\n"
    "Words count: ", len(ten_letter_words), "Time: ", avg_time, ", Accuracy: ", accuracy, ", Correct hits: ", correct_hits
)

avg_time, accuracy, correct_hits = checker_ten_letter_naive_repeat.measure_performance(words.middle_ten_letter_word, 1)
print(
    "Performance test for ten letter words using naive repeat approach with kd-tree:\n"
    "Words count: ", len(ten_letter_words), "Time: ", avg_time, ", Accuracy: ", accuracy, ", Correct hits: ", correct_hits
)

avg_time, accuracy, correct_hits = checker_ten_letter_binary.measure_performance(words.middle_ten_letter_word, 1)
print(
    "Performance test for ten letter words using binary approach with kd-tree:\n"
    "Words count: ", len(ten_letter_words), "Time: ", avg_time, ", Accuracy: ", accuracy, ", Correct hits: ", correct_hits
)

avg_time, accuracy, correct_hits = checker_ten_letter_binary_repeat.measure_performance(words.middle_ten_letter_word, 1)
print(
    "Performance test for ten letter words using binary repeat approach with kd-tree:\n"
    "Words count: ", len(ten_letter_words), "Time: ", avg_time, ", Accuracy: ", accuracy, ", Correct hits: ", correct_hits
)

avg_time, accuracy, correct_hits = checker_all_words_naive.measure_performance(words.middle_word_in_list, 1)
print(
    "Performance test for all words using naive approach with kd-tree:\n"
    "Words count: ", len(all_words), "Time: ", avg_time, ", Accuracy: ", accuracy, ", Correct hits: ", correct_hits
)

avg_time, accuracy, correct_hits = checker_all_words_naive_repeat.measure_performance(words.middle_word_in_list, 1)
print(
    "Performance test for all words using naive repeat approach with kd-tree:\n"
    "Words count: ", len(all_words), "Time: ", avg_time, ", Accuracy: ", accuracy, ", Correct hits: ", correct_hits
)

avg_time, accuracy, correct_hits = checker_all_words_binary.measure_performance(words.middle_word_in_list, 1)
print(
    "Performance test for all words using binary approach with kd-tree:\n"
    "Words count: ", len(all_words), "Time: ", avg_time, ", Accuracy: ", accuracy, ", Correct hits: ", correct_hits
)

avg_time, accuracy, correct_hits = checker_all_words_binary_repeat.measure_performance(words.middle_word_in_list, 1)
print(
    "Performance test for all words using binary repeat approach with kd-tree:\n"
    "Words count: ", len(all_words), "Time: ", avg_time, ", Accuracy: ", accuracy, ", Correct hits: ", correct_hits
)

print("---------------------------------------------------")

# Performance test for ball tree

checker_names_naive = WordChecker(three_letter_names, NAIVE, BALL_TREE)
checker_fruits_naive = WordChecker(fruits, NAIVE, BALL_TREE)

checker_three_letter_naive = WordChecker(three_letter_words, NAIVE, BALL_TREE)
checker_three_letter_naive_repeat = WordChecker(three_letter_words, NAIVE_REPEAT, BALL_TREE)
checker_three_letter_binary = WordChecker(three_letter_words, BINARY, BALL_TREE)
checker_three_letter_binary_repeat = WordChecker(three_letter_words, BINARY_REPEAT, BALL_TREE)

checker_ten_letter_naive = WordChecker(ten_letter_words, NAIVE, BALL_TREE)
checker_ten_letter_naive_repeat = WordChecker(ten_letter_words, NAIVE_REPEAT, BALL_TREE)
checker_ten_letter_binary = WordChecker(ten_letter_words, BINARY, BALL_TREE)
checker_ten_letter_binary_repeat = WordChecker(ten_letter_words, BINARY_REPEAT, BALL_TREE)

checker_all_words_naive = WordChecker(all_words, NAIVE, BALL_TREE)
checker_all_words_naive_repeat = WordChecker(all_words, NAIVE_REPEAT, BALL_TREE)
checker_all_words_binary = WordChecker(all_words, BINARY, BALL_TREE)
check_all_words_binary_repeat = WordChecker(all_words, BINARY_REPEAT, BALL_TREE)

avg_time, accuracy, correct_hits = checker_names_naive.measure_performance(words.middle_three_letter_name, 1)
print(
    "Performance test for three letter names using naive approach with ball-tree:\n"
    "Words count: ", len(three_letter_names), "Time: ", avg_time, ", Accuracy: ", accuracy, ", Correct hits: ", correct_hits
)

avg_time, accuracy, correct_hits = checker_fruits_naive.measure_performance(words.middle_fruit, 1)
print(
    "Performance test for fruits using naive approach with ball-tree:\n"
    "Words count: ", len(fruits), "Time: ", avg_time, ", Accuracy: ", accuracy, ", Correct hits: ", correct_hits
)

avg_time, accuracy, correct_hits = checker_three_letter_naive.measure_performance(words.middle_three_letter_word, 1)
print(
    "Performance test for three letter words using naive approach with ball-tree:\n"
    "Words count: ", len(three_letter_words), "Time: ", avg_time, ", Accuracy: ", accuracy, ", Correct hits: ", correct_hits
)

avg_time, accuracy, correct_hits = checker_three_letter_naive_repeat.measure_performance(words.middle_three_letter_word, 1)
print(
    "Performance test for three letter words using naive repeat approach with ball-tree:\n"
    "Words count: ", len(three_letter_words), "Time: ", avg_time, ", Accuracy: ", accuracy, ", Correct hits: ", correct_hits
)

avg_time, accuracy, correct_hits = checker_three_letter_binary.measure_performance(words.middle_three_letter_word, 1)
print(
    "Performance test for three letter words using binary approach with ball-tree:\n"
    "Words count: ", len(three_letter_words), "Time: ", avg_time, ", Accuracy: ", accuracy, ", Correct hits: ", correct_hits
)

avg_time, accuracy, correct_hits = checker_three_letter_binary_repeat.measure_performance(words.middle_three_letter_word, 1)
print(
    "Performance test for three letter words using binary repeat approach with ball-tree:\n"
    "Words count: ", len(three_letter_words), "Time: ", avg_time, ", Accuracy: ", accuracy, ", Correct hits: ", correct_hits
)

avg_time, accuracy, correct_hits = checker_ten_letter_naive.measure_performance(words.middle_ten_letter_word, 1)
print(
    "Performance test for ten letter words using naive approach with ball-tree:\n"
    "Words count: ", len(ten_letter_words), "Time: ", avg_time, ", Accuracy: ", accuracy, ", Correct hits: ", correct_hits
)

avg_time, accuracy, correct_hits = checker_ten_letter_naive_repeat.measure_performance(words.middle_ten_letter_word, 1)
print(
    "Performance test for ten letter words using naive repeat approach with ball-tree:\n"
    "Words count: ", len(ten_letter_words), "Time: ", avg_time, ", Accuracy: ", accuracy, ", Correct hits: ", correct_hits
)

avg_time, accuracy, correct_hits = checker_ten_letter_binary.measure_performance(words.middle_ten_letter_word, 1)
print(
    "Performance test for ten letter words using binary approach with ball-tree:\n"
    "Words count: ", len(ten_letter_words), "Time: ", avg_time, ", Accuracy: ", accuracy, ", Correct hits: ", correct_hits
)

avg_time, accuracy, correct_hits = checker_ten_letter_binary_repeat.measure_performance(words.middle_ten_letter_word, 1) 
print(
    "Performance test for ten letter words using binary repeat approach with ball-tree:\n"
    "Words count: ", len(ten_letter_words), "Time: ", avg_time, ", Accuracy: ", accuracy, ", Correct hits: ", correct_hits
)

avg_time, accuracy, correct_hits = checker_all_words_naive.measure_performance(words.middle_word_in_list, 1)
print(
    "Performance test for all words using naive approach with ball-tree:\n"
    "Words count: ", len(all_words), "Time: ", avg_time, ", Accuracy: ", accuracy, ", Correct hits: ", correct_hits
)

avg_time, accuracy, correct_hits = checker_all_words_naive_repeat.measure_performance(words.middle_word_in_list, 1)
print(
    "Performance test for all words using naive repeat approach with ball-tree:\n"
    "Words count: ", len(all_words), "Time: ", avg_time, ", Accuracy: ", accuracy, ", Correct hits: ", correct_hits
)

avg_time, accuracy, correct_hits = checker_all_words_binary.measure_performance(words.middle_word_in_list, 1)
print(
    "Performance test for all words using binary approach with ball-tree:\n"
    "Words count: ", len(all_words), "Time: ", avg_time, ", Accuracy: ", accuracy, ", Correct hits: ", correct_hits
)

avg_time, accuracy, correct_hits = check_all_words_binary_repeat.measure_performance(words.middle_word_in_list, 1)
print(
    "Performance test for all words using binary repeat approach with ball-tree:\n"
    "Words count: ", len(all_words), "Time: ", avg_time, ", Accuracy: ", accuracy, ", Correct hits: ", correct_hits
)



