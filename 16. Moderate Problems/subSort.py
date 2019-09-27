# Given an array of integers, write a method to find indices m and n such that if you sorted
# elements m through n, the entire array would be sorted. Minimize n - m (that is, find the smallest
# such sequence). 

def subSort(arr):
	start_index = -1
	start_value = arr[0]
	end_index = -1
	max_value = arr[0]
	for index in range(0, len(arr)):
		curr = arr[index]
		if curr < max_value: # if a number is less than the max value seen so far, that means it is out of place and needs to be sorted
			if start_index == -1 or curr < start_value: # we only need to readjust the starting index of the sort if it has not been set yet or if it's less than the start
				start_index = findIndex(curr,arr)
			end_index = index # this number is out of place so the end of the sort must include it
		else: # this means that the number is greater than or equal to the max which means it is in order
			max_value = curr
	return (start_index, end_index)


def findIndex(num, arr): # finds the index of the of the smallest number that is bigger than the input number
	max_len = len(arr)
	for index in range(0, max_len):
		if arr[index] > num:
			return index