# You are building a diving board by placing a bunch of planks of wood end-to-end.
# There are two types of planks, one of length shorter and one of length longer. You must use
# exactly K planks of wood. Write a method to generate all possible lengths for the diving board. 

# note that the order of the planks do not matter so there will be N distinct sets of K number of planks
def divingBoard(k, shorter, longer):
	lengths = set()
	for num_plank in range(0,k+1):
		length = 0
		num_shorter = num_plank
		num_longer = k - num_shorter
		length += (num_shorter * shorter) + (num_longer * longer)
		lengths.add(length)
	return lengths