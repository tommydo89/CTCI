# Given two words of equal length that are in a dictionary, write a method to
# transform one word into another word by changing only one letter at a time. The new word you get
# in each step must be in the dictionary.




def wordTransformer(start_word, stop_word, dictionary): 
	visited = set() # keeps track of the words that you have already visited
	wildcard_dict = createWildCardMap(dictionary)
	return recurseWordTransformer(start_word, stop_word, wildcard_dict, visited)



def recurseWordTransformer(start_word, stop_word, wildcard_dict, visited):
	if start_word == stop_word: # base case
		return [start_word]
	nextWords = getValidWords(start_word, wildcard_dict, visited) # the list of next possible words
	else:
		for word in nextWords: # recurse on each possible next word
			path = recurseWordTransformer(word, stop_word, wildcard_dict, visited) 
			if path != None: # we have found a path
				return [start_word] + path
		return None # we could not find any path from this start_word



def getValidWords(start_word, wildcard_dict, visited): # gets the list of valid words from the current word
	valid_words = []
	for i in range(len(start_word)):
		wildcard = start_word[0:i] + '_' + start_word[i+1:]
		if wildcard not in visited and wildcard in wildcard_dict:
			visited.add(wildcard)
			valid_words = valid_words + wildcard_dict[wildcard]
	return valid_words



def createWildCardMap(words): # creates the mapping of every wild card to all of its possibles strings
	wildcard_dict = dict()
	for word in words:
		getWildCards(word, wildcard_dict)
	return wildcard_dict

def getWildCards(string, wildcard_dict): # produces every wild card for a given string and maps that wildcard to a list of its possible strings
	for i in range(len(string)):
		wild_card = string[0:i] + '_' + string[i+1:]
		wildcard_dict[wild_card] = wildcard_dict.get(wild_card, []) + [string]