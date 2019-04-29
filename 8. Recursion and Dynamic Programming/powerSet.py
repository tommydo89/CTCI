# Write a method to return all subsets of a set.

def powerSet(number_set):
	results = set()
	recursivePowerSet(number_set, results)
	return results


def recursivePowerSet(remaining_set, results, subset=set()):
	if len(remaining_set) == 0:
		return
	for number in remaining_set:
		subset_copy = subset.copy()
		subset_copy.add(number)
		results.add(frozenset(subset_copy))
		remaining_copy = remaining_set.copy()
		remaining_copy.remove(number)
		recursivePowerSet(remaining_copy, results, subset_copy)
