# There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
 
def oneAway(string1, string2):
	if len(string1) ==  len(string2):
		return oneEditReplace(string1, string2)
	if (len(string1) == len(string2) + 1):
		return oneEditInsert(string1, string2)
	if (len(string1) + 1 == len(string2)):
		return oneEditInsert(string2, string1)
	return False

def oneEditReplace(string1, string2):
	differences = 0
	for char1, char2 in zip(string1, string2):
		if char1 != char2:
			differences += 1
		if differences > 1:
			return False
	return True

def oneEditInsert(string1, string2):
	differences = 0
	index1 = 0
	index2 = 0
	while index1 < len(string1) and index2 < len(string2):
		if (string1[index1] != string2[index2]):
			differences += 1
			index1+=1
		else:
			index1+=1
			index2+=1
	if differences <= 1:
		return True
	else:
		return False