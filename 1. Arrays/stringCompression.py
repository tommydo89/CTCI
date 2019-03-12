#  Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z). 

def stringCompression(string):
	charCountDict = countChar(string)
	compressedList = []
	returnOrg = True
	for key in charCountDict.keys():
		if charCountDict[key] > 1:
			returnOrg = False
		compressed = "%s%d" % (key, charCountDict[key]) 
		compressedList.append(compressed)
	if (returnOrg):
		return string
	else:
		return ''.join(compressedList)	


def countChar(string):
	thisdict = {}
	for char in string:
		thisdict[char] = thisdict.get(char, 0) + 1
	return thisdict
