# A majority element is an element that makes up more than half of the items in
# an array. Given a positive integers array, find the majority element. If there is no majority element,
# return-1. Do this inO(N) time and 0(1) space. 

# important concept to note: if there is a majority element, then at least one sub array will have a majority element. So start at the beginning of the
# the array and eliminate any sub-arrays that do not contain a majority element

def majorityElement(arr):
	possibleMajority = getPossibleMajority(arr)
	if validate(arr, possibleMajority):
		return possibleMajority
	return -1


def getPossibleMajority(arr): 
	majority = None
	countYes = 0
	countNo = 0
	for num in arr: # iterates through the array keeping track of the possible majority
		# indicates the start of a new subarray which means there is no majority element in all of the previous elements and so
		# we must look for a new candidate
		if countYes == 0: 
			majority = num
			countYes += 1
		else: 
			if num == majority: 
				countYes += 1
			else:
				countNo += 1
			# as long as countYes > countNo, that means there is a majority element in the current subarray. If they are equal, reset the counts to
			# start looking for a new candidate
			if countYes == countNo:
				countYes = 0
				countNo = 0
	return majority

def validate(arr, candidate): # validates if the candidate is actually the majority
	count = 0
	for num in arr:
		if num == candidate:
			count += 1
	return count > (len(arr) // 2)