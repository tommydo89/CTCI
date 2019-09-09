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
	while (arr_one_index < max1 and arr_two_index < max2): # make sure neither arrays are at their end
		# we always subtract smaller value from larger so that the difference is non-negative
		if (array1[arr_one_index] >= array2[arr_two_index]):
			difference = array1[arr_one_index] - array2[arr_two_index]
			arr_two_index += 1
		else:
			difference = array2[arr_two_index] - array1[arr_one_index]
			arr_one_index += 1
		if difference < smallest_diff or smallest_diff == -1:
				smallest_diff = difference

	# either array one has reached its end or array two has reached its end at this point in time. Iterate through this array until we reach a value that
	# is larger than the last value of the other array because if the other array has run out of values, then iterating on larger values can only
	# increase the difference 

	while(arr_one_index < max1):
		arr1 = array1[arr_one_index]
		arr2 = array2[arr_two_index - 1]
		if (arr1 > arr2):
			difference = arr1 - arr2
			if difference < smallest_diff or smallest_diff == -1:
				smallest_diff = difference
			break
		else:
			difference = arr2 - arr1
			if difference < smallest_diff or smallest_diff == -1:
				smallest_diff = difference
		arr_one_index += 1

	while(arr_two_index < max2):
		arr1 = array1[arr_one_index - 1]
		arr2 = array2[arr_two_index]
		if (arr2 > arr1):
			difference = arr2 - arr1
			if difference < smallest_diff or smallest_diff == -1:
				smallest_diff = difference
			break
		else:
			difference = arr1 - arr2
			if difference < smallest_diff or smallest_diff == -1:
				smallest_diff = difference
		arr_two_index += 1

	return smallest_diff

# Example
array1 = [-4, 5, 2, 1, 3]
array2 = [15, 13, 11, -3, 7]
# Answer should be 1 as a result of (-3 - (-4))
