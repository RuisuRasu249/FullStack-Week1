#Specify the file you want to open and the type of file it is 'r'
fin = open("words.txt", "r")
#Initialize the variables of the length of the biggest word 
# and the number of words found
biggest, num_of_words=0, 0

#We iterate across each line of the file
for line in fin:
    #First part of the forloop the variable line will contain 
    # the first line of the text file
    # the second line will contain the second line of the text file
    # and so on
    # user strip() to remove white or black space characters
    word = line.strip()
    # This will add the number of words found
    num_of_words = num_of_words + 1
    # Then this will test and compare the values for 'biggest' against the 
    # 'number_of_words' length found so far
    if len(word) > biggest:
        biggest = len(word)

# Once found and has been set we can print those on the screen
print("The longest of the {} words contains {} characters".format(num_of_words, biggest))

# Now we want to go back through the file again and look at those 
# words that match the longest length 
# We can use the seek() method to position ourselve within the file
fin.seek(0)
# we can open an output file called biggest.txt
# we can open that file for writing using 'w'
fout = open("biggest.txt", "w")
# for every lin ein the input file 
for line in fin:
    # we will read in the word, strip it again, and this time compare
    # the length of the word to the biggest length found
    word = line.strip()
    # if this word matches well add a newline character to the word
    # and write that word to the output file
    if len(word) == biggest:
        output = word + "\n"
        fout.write(output)
        # we will also print the word to the console screen aswell
        print(word)  
        
# Make sure to end and close the output files after
fin.close()		
fout.close()
