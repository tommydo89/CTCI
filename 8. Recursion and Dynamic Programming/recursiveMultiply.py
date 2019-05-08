# Write a recursive function to multiply two positive integers without using the
# *operator.You can use addition, subtraction, and bit shifting, but you should minimize the number
# of those operations.

def multiply(int1, int2):
	if (int1 >= int2):
		bigger_int = int1
		smaller_int = int2
	else:
		bigger_int = int2
		smaller_int = int1
	return recursiveMultiply(bigger_int, bigger_int, smaller_int, 1)

def recursiveMultiply(result, big_int, small_int, two_multiple):
	if (two_multiple + (two_multiple >> 1)) < small_int: # we continue to multiply by 2 if the half point to the next two_multiple is still less than small_int
		return recursiveMultiply(result << 1, big_int, small_int, two_multiple << 1)
	# at this point, two_multiple is either less than small int which means we need to add, or it is greater than small int which means we need to subtract
	elif (two_multiple < small_int): 
		for loop in range(small_int-two_multiple):
			result += big_int
	elif(two_multiple > small_int):
		for lopp in range(two_multiple - small_int):
			result -= big_int
	return result