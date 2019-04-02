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
	replaced = 0
	for char1, char2 in zip(string1, string2):
		if char1 != char2:
			if replaced:
				return False
			else:
				replaced = 1
	return True

def oneEditInsert(longer_str, shorter_str):
	removed = False
	longer_index = 0
	shorter_index = 0
	while longer_index < len(longer_str) and shorter_index < len(shorter_str):
		if (longer_str[longer_index] != shorter_str[shorter_index]):
			if removed:
				return False
			else:
				removed = True
				longer_index+=1
		else:
			longer_index+=1
			shorter_index+=1
	return True