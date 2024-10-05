import random
import os
import pickle

def replace_all(guess, word, letter):
    for pos in range(len(guess)):
        # this will find the position of each letter you have
        # guessed in the word 
        if word[pos] == letter:
            # if a letter has been guessed right this will add it in
            # and display it on the right position 
            guess = guess[:pos] + letter + guess[pos+1:]
            # once the word has been fully guessed we simply 
            # return the full guessed word to the user
    return guess

# read high score table from pickled dictionary if it exists
if os.path.isfile("hangman_scores_dictionary.txt"):
    # if the hangman_scores_dictionary file is present
    # then open it and use pickle to load the highscore table
    fin = open("hangman_scores_dictionary.txt", "rb")
    high_scores = pickle.load(fin)
    fin.close()
else:
    high_scores = {}

# Create a method that gets the words and the number of letters
def get_words(number_of_letters):
    words_found=[]
    # select the file you want to use
    fin = open("words.txt")
    for line in fin:
        # for each line in the txt document it will strip the space
        word = line.strip()
        # if the length of the word matches the number of letters we want to guess
        # then append or add in the word we want to guess
        if len(word) == number_of_letters:
            words_found.append(word)
    fin.close()		
    return words_found

# Create an input variable to allow the user to 
# enter the length of the word they want to guess
number_of_letters = int(input("Enter word length: "))
# once the user enters a specific number it will only allow the user to guess
# the amount of letters of words they want to guess
words = get_words(number_of_letters)
# This will then print out how many words there are that has the number of letters chosen
print("There are {} words with {} letters".format(len(words), number_of_letters))

# we can choose one of the words at random 
# by generating random number in the range from zero to one less than the number of words
# this will pick a random word in the list
guess_word = words[random.randint(0, len(words) - 1)]
# print the random guessing word chosen from the list
print("Guessing the word: {}".format(guess_word))


# setup 6 lives for the user
lives = 6

# Initialise the string of letters available
letters_available = "abcdefghijklmnopqrstuvwxyz"

# variable that counts how many guesses the user has so far
guess_string = "_" * number_of_letters
while lives > 0:
    # show the string of letters available
    print("Letters available: {}".format(letters_available))
    this_letter = input("Guess a letter: ")
    if this_letter in guess_word:
        # if one of the letters has been guessed then update the string and 
        # replace it with the letter that has been guessed
        guess_string = replace_all(guess_string, guess_word, this_letter)
        # if the word has been guessed then stop the game
        if guess_string == guess_word:
            print("You guessed the word!")
            break
    else:
        # if not then remove one life 
        lives = lives-1
        print("Letter not found - lives remaining: {}".format(lives))
    print("\n" + guess_string)

    # replace the guessed letter with _ in the string of the letters available
    letters_available = letters_available.replace(this_letter, "_")
print("\nGame Over!\n")

if guess_string == guess_word:
    #game is over and word was guessed
    player = input("Enter player name: ")
    score = lives* number_of_letters

    # update the high scores dictionary
    # when the game is complete we want to update
    # the high scores dictionary
    # if the plaryer is already contained in the high score table
    # we then update the entry for that playeer by 
    # adding the score to the existing value
    if player in high_scores:
        high_scores[player] = high_scores[player] + score

    # if the player is not contained in the dictionary,
    # we create a new dictionary for that player 
    # setting the value to their current score
    else:
        high_scores[player] = score
    # open the dictionary.txt file for writing then
    # dump the current state of our high_scores dictionary to that file
    fout = open("hangman_scores_dictionary.txt", "wb")
    pickle.dump(high_scores, fout)
    fout.close()

else:
    # the game is over but the word was not guessed, so show it
    print("the word was - {}".format(guess_word))

# show the new current high scores
print("\nHIGH SCORES TABLE")
for person in high_scores.keys():
    print(str(high_scores[person]).rjust(4) + " " + person)

    # high scores file maintains cumulative scores
    fin = open("hangman_scores.txt", "r")
    #open a temporary file for the updated output
    fout = open("temp.txt", "w")
    # need to keep track of wether the current player is a new one
    player_found = False
    # check each line in scores file
    for line in fin:
        #split the line
        line_parts = line.strip().split(",")
        # does the player on this line match the name provided?
        if line_parts[0] == player:
            # names match, so add this score to the previous score in the file
            new_score = int(line_parts[1]) + score
            # line of output will be the players name and their updated score
            new_line = "{},{}\n".format(line_parts[0], new_score)
            # record that the player was already in te scores file
            player_found = True
        else:
            # names dont match so the line of output will be the originial name and score
            new_line = "{},{}\n".format(line_parts[0], line_parts[1])
        # add line of output to the temporary file
        fout.write(new_line)

    if not player_found:
        # all file entries checked and player not found
        # so add a line of output for the new player
        new_line = "{},{}\n".format(player, score)
        fout.write(new_line)
    fin.close()
    fout.close()

    # results file updated, so replace scores file with temporary file
    os.replace("temp.txt", "hangman_scores.txt")
else:
    print("the word was - {}".format(guess_word))