#  Given an input file with four billion non-negative integers, provide an algorithm to
# generate an integer that is not contained in the file. Assume you have 1 GB of memory available for
# this task.

def missingInt(file):
	num_ints = 4000000000 # number of possible integers in the file
	byte_array = bytearray(num_ints//8 + 1) # bit vector 
	file = open("testfile.txt", 'r')
	for number in file: # maps each number to a specific bit
		number = int(number)
		byte_index = number//8
		bit_index = number % 8
		byte_array[byte_index] |= 1 << bit_index
	for byte_index in range(0, len(byte_array)): # iterates over the bit vector to look for the first 0 which indicates the first missing int
		for bit_index in range(0,8):
			if (byte_array[byte_index] & (1 << bit_index)) == 0:
				return byte_index * 8 + bit_index