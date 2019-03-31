# You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to
# find the length of the longest sequence of ls you could create. 

def flipBitToWin(num):
	# keeps track of the numbers of 1s that have occured after the last 0
	ones_after_zero = 0
	# boolean for whether a bit has been flipped yet
	bit_flipped = False
	# longest length of 1s so far
	longest_seq = 0
	# current length of 1s
	current_seq = 0

	# if we repeatedly right shift num, then after the last binary digit has been right shifted(last digit should be 1), num will equal 0 so we end the loop
	while (num > 0):
		# extracts the right-most binary digit
		binary_digit = num & 1
		if binary_digit == 1:
			if bit_flipped:
				ones_after_zero+=1
			current_seq += 1
		else:
			if bit_flipped:
				if current_seq > longest_seq:
					longest_seq = current_seq
				# at this point, we have encountered a second 0 in which if we flip this bit, then the current sequence of 1s is the sequences of 1s after the last 0 in addition to the bit we just flipped
				current_seq = ones_after_zero + 1
				# we then reset this variable to 0
				ones_after_zero = 0
			else:
				# we have encountered a 0 but bit_flipped is False, so we flip the bit and increment the current sequence of 1s
				bit_flipped = True
				current_seq += 1
		# right shift the number to get the next bit
		num = num >> 1
	# one last comparison of the current seq to the longest seq 
	if current_seq > longest_seq:
		longest_seq = current_seq
	return longest_seq