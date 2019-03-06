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
