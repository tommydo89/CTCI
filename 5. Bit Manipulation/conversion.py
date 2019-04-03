# Write a function to determine the number of bits you would need to flip to convert
# integer A to integer B. 

def conversion(A, B):
	num  = A ^ B # we xor A and B in which the number of 1 bits in the resulting number will indicate the number of bits we need to flip to convert A to B
	bits_to_flip = 0
	while num != 0:
		if num & 1 == 1:
			bits_to_flip += 1
		num = num >> 1
	return bits_to_flip