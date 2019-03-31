# Given a real number between O and 1 (e.g., 0.72) that is passed in as a double, print
# the binary representation. If the number cannot be represented accurately in binary with at most 32
# characters, print "ERROR:' 

def binaryToString(num):
	if (num >= 1 or num <= 0):
		return 'ERROR: Input must be between 0 and 1'
	binary_array = []
	while (num > 0):
		if len(binary_array) > 32:
			return 'ERROR: Number cannot be represented accurately with at most 32 binary digits'
		num *= 2
		if (num >= 1):
			num = num - 1
			binary_array.append('1')
		else:
			binary_array.append('0')
	return ''.join(binary_array)

