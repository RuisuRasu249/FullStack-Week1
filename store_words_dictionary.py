import random

# This file is used to crreate a dictionary
# this selects random words from the words.txt file
# then sorts them in in a dictionary 
# where its sorted that begin with that initial letter 
# and stores it as values

all_words = []
fin = open("words.txt")
for line in fin:
    word = line.strip()
    all_words.append(word)
fin.close()		

letters = "abcdefghijklmnopqrstuvwxyz"
words_dict = {}
for i in range(26):
    words_dict[letters[i]] = []

for _ in range(50):
    random_word = all_words[ random.randint(0, len(all_words) - 1) ]
    words_dict[random_word[0]].append(random_word)

for letter in letters:
    print(letter, words_dict[letter], '\n')