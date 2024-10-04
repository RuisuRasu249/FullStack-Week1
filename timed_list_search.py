import time

# this prints and returns 
# the time execution it takes to search/ lookup words
def time_execution(code):
	start = time.perf_counter()
	eval(code)
	run_time = time.perf_counter() - start
	return run_time

# Adds data to our collection
def add_word(this_collection, keyword, url):
	# it checks each entry of the collection
	# looking for a match with keyword passed as a parameter
	# if a match is found it adds that URL to the list for that word
	for entry in this_collection:
		if entry[0] == keyword:
			entry[1].append(url)
			return
		# if a match is not found it creates a new entry
		# with the URL  as the second part if the list entry
	this_collection.append([keyword,[url]])	

# the number of words we request it adds that number of words
# to the collection at the dummy URL location
def make_collection(all_words, size):
	this_collection = []
	for i in range(size):
		add_word(this_collection, all_words[i], "dummyURL")
	return this_collection

# lookup is the search operation
# if you pass it a keyword 
# it will check every element in the collection
def lookup(keyword, index):
	for e in index:
		# if the first part of the element matches the keyword
		# it then returns the second part
		# which is the list of URLs
		if e[0] == keyword:
			return e[1]
		# if it completes without finding any keyword 
		# it will return an empty list
	return []

all_words = []
fin = open("words.txt")
for line in fin:
    word = line.strip()
    all_words.append(word)
fin.close()	

collection = make_collection(all_words, 1000)
print("Lookup for 1000 words")
print(time_execution("lookup('xxx', collection)"))

collection = make_collection(all_words, 2000)
print("Lookup for 2000 words")
print(time_execution("lookup('xxx', collection)"))

collection = make_collection(all_words, 4000)
print("Lookup for 4000 words")
print(time_execution("lookup('xxx',collection)"))

collection = make_collection(all_words, 8000)
print("Lookup for 8000 words")
print(time_execution("lookup('xxx', collection)"))

collection = make_collection(all_words, 16000)
print("Lookup for 16000 words")
print(time_execution("lookup('xxx', collection)"))
	
collection = make_collection(all_words, 32000)
print("Lookup for 32000 words")
print(time_execution("lookup('xxx', collection)"))