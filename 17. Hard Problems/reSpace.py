# Oh, no! You have accidentally removed all spaces, punctuation, and capitalization in a
# lengthy document. A sentence like "I reset the computer. It still didn't boot!"
# became "iresetthecomputeritstilldidntboot''. You'll deal with the punctuation and capitalization later; right now you need to re-insert the spaces. Most of the words are in a dictionary but
# a few are not. Given a dictionary (a list of strings) and the document (a string), design an algorithm
# to unconcatenate the document in a way that minimizes the number of unrecognized characters.
# EXAMPLE:
# Input: jesslookedjustliketimherbrother
# Output: jess looked just like tim her brother (7 unrecognized characters) 

def reSpace(dictionary, sentence):
	result = [None, ''] # stores the lowest unrecognized count and its associated sentence
	recursereSpace(dictionary, sentence[0], sentence, 1, result)
	return result[1]


def recursereSpace(dictionary, curr_sentence, org_sentence, index, result):
	if index == len(org_sentence): # base case when we have iterated over the entire sentence
		ct_unrecognized = eval_unrecognized(curr_sentence, dictionary)
		if result[0] == None or ct_unrecognized < result[0]: # update result is current sentence has fewer unrecognized characters
			result[0] = ct_unrecognized
			result[1] = curr_sentence
		return
	recursereSpace(dictionary, curr_sentence + org_sentence[index], org_sentence, index + 1, result) # adds the next char
	recursereSpace(dictionary, curr_sentence + ' ' + org_sentence[index], org_sentence, index + 1, result) # add a space and then the next char


def eval_unrecognized(sentence, dictionary): # evaluates the number of unrecognized characters in a sentence
	ct_unrecognized = 0
	words = sentence.split(' ')
	for word in words:
		if word not in dictionary:
			ct_unrecognized += len(word)
	return ct_unrecognized
