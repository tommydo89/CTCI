# Design an algorithm to find all pairs of integers within an array which sum to a
# specified value. 

def pairsWithSum(arr, target_sum):
	already_used = set()
	results = []
	for num in arr:
		if num not in already_used:	
			target = target_sum - num
			if target in arr:
				already_used.add(num)
				already_used.add(target)
				results.append((num, target))
	return results