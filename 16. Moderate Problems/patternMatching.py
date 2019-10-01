# You are given two strings, pattern and value. The pattern string consists of
# just the letters a and b, describing a pattern within a string. For example, the string catcatgocatgo
# matches the pattern aabab (where cat is a and go is b). It also matches patterns like a, ab, and b.
# Write a method to determine if value matches pattern. 

def patternMatching(pattern, value):
	if pattern == 'a' or pattern == 'b':
		return True
	for first_index in range(1, len(value)+1):
		for second_index in range(first_index+1, len(value)+1):
			first_pattern = value[:first_index]
			second_pattern = value[first_index:second_index]
			if matches(pattern, value, first_pattern, second_pattern):
				return True
	return False




def matches(pattern, value, first, second):
	result = ""
	start_pattern = pattern[0]
	for char in pattern:
		if char == start_pattern:
			result += first
		else:
			result += second
	if result == value:
		return True
	return False