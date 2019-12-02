# Given a string b and an array of smaller strings T, design a method to search b for
# each small string in T. 



def multiSearch(big_string, strings):
	map_result = dict() # maps each found string to it's starting index in the big string
	trie_root = createTrie(strings) # create a trie from the smaller strings
	for index in range(0, len(big_string)): # iterates through each of the possible starting points when traversing the tree
		searchTrie(big_string, index, trie_root, map_result) 
	return map_result


def searchTrie(big_string,start_index, trie_root, map_result):
	found = [] # stores the list of smaller strings that were found
	root = trie_root
	for curr_index in range(start_index, len(big_string)):
		letter = big_string[curr_index]
		if letter not in root: # end trie traversal if this letter cannot be found
			break
		else:
			root = root[letter] 
			if terminates(root): # stores the current substring if it has been found in the tree
				found.append(big_string[start_index:curr_index + 1])
	if len(found) != 0:
		insertIntoMAP(found, start_index, map_result)

def insertIntoMAP(strings, location_index, map_result): # inserts all the found strings into a dictionary that maps each string to it's starting index in the big string
	for word in strings:
		map_result[word] = location_index

def terminates(root): # checks to see if there is a termination which means we found a word
	if '_end' in root:
		return True
	return False

def createTrie(strings): # creates a trie from the smaller strings
	root = dict()
	for word in strings:
		current_dict = root
		for letter in word:
			current_dict = current_dict.setdefault(letter, {}) # if letter is not in the dict, it will set {} as it's default value and also return it's value which is {}
		current_dict['_end'] = '_end' # termination of the trie path
	return root
