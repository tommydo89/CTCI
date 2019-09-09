# Given two arrays of integers, compute the pair of values (one value in each
# array) with the smallest_diff (non-negative) difference. Return the difference. 


def smallestDifference(array1, array2):
	array1.sort()
	array2.sort()
	max1 = len(array1)
	max2 = len(array2)
	smallest_diff = -1
	arr_one_index = 0
	arr_two_index = 0
	while (arr_one_index < max1 and arr_two_index < max2):
		arr1 = array1[arr_one_index]
		arr2 = array2[arr_two_index]
		difference = abs(arr1 - arr2)
		if (difference < smallest_diff or smallest_diff == -1):
			smallest_diff = difference
		if arr1 < arr2:
			arr_one_index += 1
		else:
			arr_two_index += 1
	return smallest_diff

# Example
array1 = [-4, 5, 2, 1, 3]
array2 = [15, 13, 11, -3, 7]
# Answer should be 1 as a result of (-3 - (-4))
