#  You are given two arrays, one shorter (with all distinct elements) and one
# longer. Find the shortest subarray in the longer array that contains all the elements in the shorter
# array. The items can appear in any order.
# EXAMPLE
# lnput:{1, 5, 9} I {7, 5, 9, 0, 2, 1, 3, 5, 7, 9. 1, 1, 5, 8, 8, 9, 7}
# Output: [ 7, 10] (the underlined portion above) 

def shortestSS(shorter, longer):
	num_to_index = dict() # maps each number to its most recent index 
	found = [] # stores the numbers in the order that they were found
	start_index = None # starting index of the shortest sub array
	end_index = None # ending index of the shortest sub array
	index = 0 # current index 
	shortest_length = None
	for num in longer:
		if num in shorter:
			num_to_index[num] = index
			if num not in found:
				found = [num] + found
			if len(found) == len(shorter):
				if (shortest_length == None): # initialization of values upon the first time finding all values
					start_index = 0
					end_index = index
					shortest_length = end_index - start_index + 1
				elif num == found[len(shorter) - 1]: # we can only shorten the subarray when we find the same number that begins the subarray 
					end = index
					removed = found.pop() # removes the first element of the subarray
					found = [removed] + found # appends the removed element to the end of the subarray
					last = found[len(found) - 1] # last index of found
					start = num_to_index[last] # finds the most recent index of first element of the subarray
					current_length = end - start + 1 
					if current_length < shortest_length:
						shortest_length = current_length
						start_index = start
						end_index = end
		index += 1
	return (start_index, end_index)




