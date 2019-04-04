# Write a program to swap odd and even bits in an integer with as few instructions as
# possible (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on). 
def pairwiseSwap(num):
	num_bits = 0
	temp = num
	while (temp > 0): # figures out how many bits represent the number
		temp = temp >> 1
		num_bits += 1
	shifts = (num_bits // 2) + 1 # the number of 10s we need to create a mask for the odd and even bits
	odd_mask = 0 # we start off with a binary mask of 0
	for loop in range(0, shifts):
		odd_mask = ((odd_mask << 1) + 1) << 1 # this will basically append another 10 to the end of the mask. Ex: 10 becomes 1010
	even_mask = ~odd_mask 
	shift_odds = (num & odd_mask) >> 1 # shift odd bits one place to the left
	shift_evens = (num & even_mask) << 1 # shift even bits one place to the right
	return shift_odds | shift_evens #combines the odd and even bits for the result

