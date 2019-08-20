# Write a function to swap a number in place (that is, without temporary variables). 

# if we can swap the bits, that means we can successfully swap the number 
# key concept: XORing a bit with 1 always flips the bit whereas XORing with 0 will never change it
# think about if x and y were just 1 bit. x ^ y will equal 1 if they are not equal, 0 if they are 

def numberSwapper(array, index1, index2):

	array[index1] = array[index1] ^ array[index2] # first check to see if the bits are different. array[index1] will equal 1 if the bits are different, 0 if not
	# If array[index1] and array[index2] were originally different, array[index2] will now equal array[index1] since array[index1] will equal 1 after the previous operation and
	# XORing a bit with 1 will always flip it
	array[index2] = array[index1] ^ array[index2] 
	# you may now repeat the process by XORing array[index2] with array[index1] which should produce the original array[index1].
	array[index1] = array[index1] ^ array[index2]
