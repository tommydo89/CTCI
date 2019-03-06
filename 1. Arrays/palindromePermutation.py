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
