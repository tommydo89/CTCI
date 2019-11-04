# An array A contains all the integers from Oto n, except for one number which
# is missing. In this problem, we cannot access an entire integer in A with a single operation. The
# elements of A are represented in binary, and the only operation we can use to access them is "fetch
# the jth bit of A[ i ],"which takes constant time. Write code to find the missing integer. Can you do
# it inO(n) time? 

# the least significant bit should alternate between 0 and 1 as the integers increase by 1 and so if we encounter 2 consecutive bits that are the same,
# we know that we have skipped an integer
def missingNumber(arr):
	num = 0
	for index in range(len(arr)):
		expected_bit = index % 2
		if arr[index] & 1 != expected_bit:
			return num
		num += 1