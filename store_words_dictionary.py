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

# can search for a max of 3 words
for _ in range(3):
    # create a search word input
    search_word = input("Enter a word to search for >> ")
    # search the initial letter of that word
    # which list the word might be in 
    # calculate the list index
    # by taking the ASCII value of the initial letter and 
    # subtracting the ASCII value of lowercase 'a'
    if search_word in words_dict[search_word[0]]:
        print("FOUND")
    else:
        print("NOT FOUND")