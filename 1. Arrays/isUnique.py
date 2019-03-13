# Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures? 

def isUnique(string):
	thisdict = {}
	for char in string:
		thisdict[char] = thisdict.get(char, 0) + 1
		if (thisdict[char] > 1):
			return False
	return True