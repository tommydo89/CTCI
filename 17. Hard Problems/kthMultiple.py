# Design an algorithm to find the kth number such that the only prime factors are 3, 5,
# and 7. Note that 3, 5, and 7 do not have to be factors, but it should not have any other prime factors.
# For example, the first several multiples would be (in order) 1, 3, 5, 7, 9, 15, 21, 25, 27, 35, 45, 49. 

# note that the multiples repeat based on 3, 5, and 7 because if the only prime factors allowed are 3, 5, and 7 then even numbers are not valid. And if
# even numbers are not valid, all factors have to be odd or else the number will be even. Therefore 
def kthMultiple(k):
	if k == 1:
		return 1
	else:
		indexes = {3:0, 5:0, 7:0} # maps each base to the next smallest possible number in the numbers thus far that they can be multipled by
		multiple_to_base = {3:3, 5:5, 7:7} # maps each of the next possible numbers to the base that they are derived from
		multiples = [1] # the list of multiples in order
		for iteration in range(1,k): # iterates and creates an array of the k multiples
			lowest = min(multiple_to_base.keys()) # add the lowest possible multiple to the array
			multiples.append(lowest)
			base = multiple_to_base[lowest] # determine the base of the multiple that was added to the array 
			next_index = indexes[base]
			while True: # iterate and find the next smallest possible multiple for that base
				next_num = multiples[next_index] * base
				if next_num in multiple_to_base.keys():
					next_index += 1
				else:
					break
			# updates the mapping after finding the next possible multiple for that base
			del multiple_to_base[lowest] 
			multiple_to_base[next_num] = base
			# updates the index of the next possible number for the base to be multiplied with
			indexes[base] = next_index
		return multiples.pop()
