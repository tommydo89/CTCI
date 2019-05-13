# Write a method to compute all permutations of a string of unique
# characters.

def permutations(string):
	results = []
	recursivePermutation(list(string), [], results)
	return results

def recursivePermutation(remaining, permutation, results):
	if len(permutation) > 0:
		results.append(permutation)
	if len(remaining) == 0:
		return
	for char in remaining:
		copy_remaining = remaining[:]
		copy_remaining.remove(char)
		recursivePermutation(copy_remaining, permutation[:] + [char], results)

