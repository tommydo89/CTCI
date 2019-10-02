# On old cell phones, users typed on a numeric keypad and the phone would provide a list of
# words that matched these numbers. Each digit mapped to a set of O - 4 letters. Implement an algorithm to return a list of matching words, given a sequence of digits. You are provided a list of valid
# words (provided in whatever data structure you'd like). The mapping is shown in the diagram below:

def T9(number_pad, digits, word_list):
	results = [] # stores the list of possible words
	recursive_T9('', number_pad, 0, digits, word_list, results)
	return results

def recursive_T9(word, number_pad, index, digits, word_list, results): # recursively builds each possible word given the digits
	if (index > len(digits) - 1) and (word in word_list): # if there are no more digits to retrieve a letter and the word is in the list, then add it to the results
		results.append(word)
	elif index < len(digits):
		digit = digits[index]
		for letter in number_pad[digit]: # recurse on each possible letter given the current digit
			recursive_T9(word + letter, number_pad, index + 1, digits, word_list, results)


number_pad = {'1':[],'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z'],'0':[]}