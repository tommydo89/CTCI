# You are given two 32-bit numbers, N and M, and two bit positions, i and
# j. Write a method to insert M into N such that M starts at bit j and ends at bit i. You
# can assume that the bits j through i have enough space to fit all of M. That is, if
# M = 10011, you can assume that there are at least 5 bits between j and i. You would not, for
# example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2.

def insertion(outer, inner, start_index, end_index):
	outer = int(outer, 2)
	inner = int(inner, 2)
	mask = ~((((1<<(end_index - start_index + 1)) - 1) or inner) << start_index) # creates a mask that will allow us to clear the bits from start index to end index
	outer = outer & mask # clears the bits from start index to end index
	outer = outer | (inner << start_index) # copies the inner bits to start to end
	return bin(outer)