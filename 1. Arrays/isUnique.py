
def isUnique(string):
	thisdict = {}
	for char in string:
		thisdict[char] = thisdict.get(char, 0) + 1
		if (thisdict[char] > 1):
			return False
	return True