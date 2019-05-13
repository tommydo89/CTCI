# Write a method to compute all permutations of a string whose characters are not necessarily unique. The list of permutations should not have duplicates. 

def permutations(string):
	results = []
	recursivePermutation(list(set(string)), [], results)
	return results

def recursivePermutation(remaining, permutation, results):
	if len(permutation) > 0:
		results.append(permutation)
	if len(remaining) == 0: # if there are no more letters, end the recursion
		return
	for char in remaining:
		copy_remaining = remaining[:]
		copy_remaining.remove(char) # remove the current character from the copy
		recursivePermutation(copy_remaining, permutation[:] + [char], results)



