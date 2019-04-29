# Write a method to return all subsets of a set.

def powerSet(number_set):
	results = []
	recursivePowerSet(number_set, results)
	return results


# def recursivePowerSet(remaining_set, results, subset=set()):
# 	if len(remaining_set) == 0:
# 		return
# 	for number in remaining_set:
# 		subset_copy = subset.copy()
# 		subset_copy.add(number)
# 		results.add(frozenset(subset_copy))
# 		remaining_copy = remaining_set.copy()
# 		remaining_copy.remove(number)
# 		recursivePowerSet(remaining_copy, results, subset_copy)

def recursivePowerSet(remaining_set, results, current_set = set()):
	if len(remaining_set) == 0: 
		if len(current_set) > 0: # we only want to append the set if it is not empty
			results.append(current_set)
		return
	number = remaining_set.pop()
	add_set = current_set.copy()
	add_set.add(number)
	recursivePowerSet(remaining_set.copy(), results, add_set) # add the number to the set and recurse
	recursivePowerSet(remaining_set.copy(), results, current_set.copy()) # do not add the number and recurse