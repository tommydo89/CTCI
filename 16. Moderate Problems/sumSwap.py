# Given two arrays of integers, find a pair of values (one value from each array) that you
# can swap to give the two arrays the same sum. 

def sumSwap(arr1, arr2):
	arr1_sum = sum(arr1)
	arr2_sum = sum(arr2)
	if arr2_sum > arr1_sum:
		bigger = arr2
		smaller = arr1
	else:
		bigger = arr1
		smaller = arr2
	diff = abs(arr1_sum - arr2_sum)
	if diff % 2 != 0:
		return False
	target = (diff) // 2
	for num1 in bigger:
		for num2 in smaller:
			if (num1 - num2) == target:
				if arr1 == bigger:
					return (num1, num2)
				else:
					return (num2, num1)