# Design a method to find the frequency of occurrences of any given word in a
# book. What if we were running this algorithm multiple times? 

def returnBookHash():
	book_dict = {}
	with open('wordFrequenciesBook.txt', 'r') as f:
		for line in f:
			for word in line.split():
				clean_word = ''
				for char in word:
					if char.isalpha():
						clean_word += char
				clean_word = clean_word.lower()
				if clean_word not in book_dict:
					book_dict[clean_word] = 1
				else:
					book_dict[clean_word] += 1
	return book_dict

def getWordFreq(book_dict, word):
	if book_dict == None or word == None:
		return -1
	word = word.lower()
	if word not in book_dict:
		return 0
	return book_dict[word]