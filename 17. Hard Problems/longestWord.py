# Given a list of words, write a program to find the longest word made of other words
# in the list.
# EXAMPLE
# lnput:cat, banana, dog, nana, walk, walker, dogwalker
# Output: dogwalker 

def longestWord(words):
	words.sort(key=len, reverse=True) # sorts the list of words from longest to shortest length
	word_map = {} # dictionary for all the words
	for word in words:
		word_map[word] = True
	for word in words: # iterate from longest to shortest in which we can return the current word once we know it can be built from other words
		if canBuildWord(word, word, word_map):
			return word
	return False

def canBuildWord(word, original, word_map):
	if word in word_map and word != original: # base case where we make sure word != original because this will always be true on the very first call
		return word_map[word]
	for index in range(1,len(word)): # tries every possible substring for the left and right
		left = word[0:index]
		right = word[index:]
		if left in word_map and word_map[left] == True and canBuildWord(right, original, word_map): # if the left side is a word, then we recurse on the right
			return True
	word_map[word] = False # caches the fact that this word cannot be built from other words
	return False


	
