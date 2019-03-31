# Given a real number between O and 1 (e.g., 0.72) that is passed in as a double, print
# the binary representation. If the number cannot be represented accurately in binary with at most 32
# characters, print "ERROR:' 

def binaryToString(num):
	# input must be between 0 and 1
	if (num >= 1 or num <= 0):
		return 'ERROR: Input must be between 0 and 1'
	#array to store binary digits
	binary_array = []

	#the loop ends when num equals 0 because the last binary digit of the num must be a 1. And 0.1 in binary equals 0.5 as a decimal which will equal 0 after multiplying it by 2 and subtracting 1
	while (num > 0):
		if len(binary_array) > 32:
			return 'ERROR: Number cannot be represented accurately with at most 32 binary digits'
		num *= 2
		# if num >= 1, then we know that there must have been a 1 right after the decimal point. We must then also subtract 1 to bring the number back to less than 1 so that we may repeat the process for identifying the next bit
		if (num >= 1):
			num = num - 1
			binary_array.append('1')
		# if num < 1 then we know that there must have been a 0 right after the decimal point. We do not need to subtract 1 because the logic for identifying the next bit will still work since num is between 0 and 1
		else:
			binary_array.append('0')
	# joins the array to create the binary string representation
	return ''.join(binary_array)

