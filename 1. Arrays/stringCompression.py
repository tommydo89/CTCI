#  Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z). 

def stringCompression(string):
	count = 0
	prevChar = None
	result = []
	for char in string:
		if (prevChar == None): # we are at the first char in the iteration so we append it and increment count
			result.append(char)
			count += 1
			prevChar = char
		elif (char != prevChar): # we encounter a different character so we append the current count and then current character and then set count to 1
			result.append(str(count))
			result.append(char)
			count = 1
			prevChar = char
		else: # we encounter the same character so we just increment count by 1
			count += 1
	result.append(str(count)) # the count for the last char will not be appended with the loop so we do it here
	result_string = ''.join(result) 
	if len(result_string) > len(string): # if the result is longer than the original string, return the original
		return string
	else:
		return result_string