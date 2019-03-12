#  Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

def palindromePermutation(string):
	thisdict = {}
	for char in string:
		if char != ' ':
			thisdict[char] = thisdict.get(char, 0) + 1
	odd_char_cts = 0
	for key in thisdict.keys():
		if thisdict[key] % 2 == 1:
			odd_char_cts += 1
	if odd_char_cts > 1:
		return False
	else:
		return True
