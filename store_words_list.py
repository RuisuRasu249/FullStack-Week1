import random
# this application is a list that contains 
# a collection of sublists, 
# one for each letter of the alphabet

# create a list all_words
all_words = []
# use words.txt file
fin = open("words.txt")

for line in fin:
    # read each word one at a time
    word = line.strip()
    # then append it to all words
    all_words.append(word)
    # all words will be a list containing
    # every word read from the file
fin.close()		

# initialize our structure as an empty list
words_list = []
# createe 26 empty lists each which gets
# appended as an element of 'words_list'
for _ in range(26):
    # words_list containing 26 elements
    # each one of those is itselft a list
    words_list.append([])

for _ in range(50):
    # we'll choose 50 random entries from 'all_words'
    # and for each one selected we will store it in the 'worlds_list' entry
    # that corresponds to its initial letter
    random_word = all_words[ random.randint(0, len(all_words) - 1) ]
    # so all words beggining with 'a' are in 'words_list' element 0
    # 'b' are in 'words_list' element 1 etc.
    words_list[ ord(random_word[0]) - ord('a') ].append(random_word)

# this file basically selects random words from the txt file
# then sorts them into their right alphabetical groupings
letters = "abcdefghijklmnopqrstuvwxyz"
for i in range(26):
    print(letters[i], words_list[i], '\n')

# can search for a max of 3 words
for _ in range(3):
    # create a search word input
    search_word = input("Enter a word to search for >> ")
    # search the initial letter of that word
    # which list the word might be in 
    # calculate the list index
    # by taking the ASCII value of the initial letter and 
    # subtracting the ASCII value of lowercase 'a'
    if search_word in words_list[ord(search_word[0]) - ord('a')]:
        print("FOUND")
    else:
        print("NOT FOUND")