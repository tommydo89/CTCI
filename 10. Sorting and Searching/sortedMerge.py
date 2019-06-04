def sortedMerge(A, B):
	A_index = find_last_index(A) # last index in A
	B_index = len(B) - 1 # last index in B
	end_index = A_index + B_index + 1 # last index of A and B merged
	for index in range(end_index, -1, -1): # iterate from the end index to the start index inserting the larger value between A and B
		if (B_index < 0): # B has been fully inserted into A so we can return A since we know that the rest of A is already sorted
			return A
		if (B[B_index] > A[A_index]): # insert value from B if it is greater
			A[index] = B[B_index]
			B_index -= 1 
		else: # insert value from A if it is greater
			A[index] = A[A_index]
			A_index -= 1


def find_last_index(array): # finds the last index of an array given that it has a buffer filled with Nones
	end = len(array) - 1
	while isinstance(array[end], int) == False:
		end -= 1
	return end
