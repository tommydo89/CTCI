# Write a method to randomly generate a set of m integers from an array of size n. Each
# element must have equal probability of being chosen.
from random import randrange
def randomSet(arr, m):
	result = arr[:m] # copies the first m elements in the resulting array

	# iterates through the remaining elements to determine if that element should be included in the set based on the random number produced
	# Think of this whole iterative process as base case and build
	# At each iteration, each number has an equal probability of being in the set either through either insertion or they were already in the set and had not been removed
	# By only inserting when the random number is less than m, we ensure that it has a m/n probability of being in the set which is the correct probability
	# By choosing a random number k from 0 to i we also ensure that the element chosen to be removed is random
	for i in range(m, len(arr)): 
		k = randrange(0, i)
		if k < m:
			result[k] = arr[i]
	return result