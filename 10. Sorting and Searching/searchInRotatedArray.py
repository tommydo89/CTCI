# Given a sorted array of n integers that has been rotated an unknown
# number of times, write code to find an element in the array. You may assume that the array was
# originally sorted in increasing order.

def search(target, array):
	low = 0
	high = len(array) - 1
	mid = high//2
	return recursiveSearch(target, array, low, mid, high)

def recursiveSearch(target, array, low, mid, high):
	if array[low] == target:
		return low
	if array[high] == target:
		return high
	if array[mid] == target:
		return mid
	if array[low] < array[mid]: # if low < mid, that means all the numbers between them are sorted and so if the target is between low and mid, recurse between them, else recurse on other half
		if target > array[low] and target < array[mid]:
			return recursiveSearch(target, array, low+1, (low+mid)//2, mid-1)
		else:
			return recursiveSearch(target, array, mid+1, (mid+high)//2, high-1)
	elif array[mid] < array[high]: # if mid < high, that means all the numbers between them are sorted and so if the target is between mid and high, recurse between them, else recurse on other half
		if target > array[mid] and target < array[high]:
			return recursiveSearch(target, array, mid+1, (mid+high)//2, high-1)
		else:
			return recursiveSearch(target, array, low+1, (low+mid)//2, mid-1)