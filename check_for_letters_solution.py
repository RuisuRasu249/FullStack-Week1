# Open words.txt file for input
fin = open("words.txt", "r")
# open output file letters.txt
fout = open("letters.txt", "w")

# input a three letter string
letters = input("Enter a three-letter sequence >> ")

# For each line of the file will read the word
for line in fin: 
    word = line.strip()

    # we will then check each letter in the word 
    # that has been inputted
    pos0 = word.find(letters[0])
    # This will find the first second and third position
    # of each letter that has been inputted
    # once its found print the word
    if pos0 > -1:
        pos1 = word.find(letters[1], pos0 + 1)
        if pos0 > -1:
            pos2 = word.find(letters[2], pos1 + 1)
            if pos2 > -1:
                # once the word and letters have been found
                # will write it to the output file 
                # then print it in the terminal
                fout.write(word + '\n')
                print(word)

fin.close()
fout.close()
