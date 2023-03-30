import nltk
nltk.download('words')  # Download the 'words' corpus from NLTK

from nltk.corpus import words

def letter_sum(word):
    letter_values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    # Create a dictionary with each letter as the key and its corresponding numerical value as the value

    total = 0
    for letter in word.lower():
        if letter in letter_values:
            total += letter_values[letter]
    # Loop through each letter in the word, add its numerical value to the total if it exists in the letter_values dictionary
    
    return total

num = input("Enter a number pi: ")
matching_words = []
for word in words.words():
    if letter_sum(word) == int(num):
        matching_words.append(word)
# Loop through each word in the 'words' corpus from NLTK and check if its numerical value matches the input number. If it does, add it to the list of matching words.

if len(matching_words) > 0:
    print("The following words have a numerical value of", num + ":")
    for word in matching_words:
        print(word)
else:
    print("No words have a numerical value of", num)
