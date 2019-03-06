def checkPermutation(string_one, string_two):
	char_counts = {}
	if (len(string_one) != len(string_two)):
		return False
	for char in string_one:
		char_counts[char] = char_counts.get(char, 0) + 1
	for char in string_two:
		char_counts[char] = char_counts.get(char, 0) - 1
	for key in char_counts.keys():
		if char_counts[key] > 0:
			return False
	return True
