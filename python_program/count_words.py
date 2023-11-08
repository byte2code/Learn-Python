# Count Words in a String: Count the number of words in a given string. 
def count_words(input_string):
    num_words = 0
    is_previous_word_char = False
    for char in input_string:
        # Check if the current character is a word character (letter or digit)
        is_current_word_char = char.isalnum()

        if is_current_word_char and not is_previous_word_char:
            num_words += 1

        is_previous_word_char = is_current_word_char

    return num_words

input_string = "Mausam!Giri Btech CSE."
word_count = count_words(input_string)
print(f"Number of words in the string: {word_count}")
