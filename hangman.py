import random

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
# variable that counts how many guesses the user has so far
guess_string = "_" * number_of_letters
while lives > 0:
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
    print(guess_string)

# If the user enters their details after winning or losing the game 
# it will add in a new player in the hangman_scores file
if lives > 0:
    player = input("Enter player name: ")
    fout = open("hangman_scores.txt", "a")
    score = lives * number_of_letters
    new_score_text = "{}, {}\n".format(player, score)
    fout.write(new_score_text)
    fout.close()