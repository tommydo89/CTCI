# Given an M x N matrix in which each row and each column is sorted in
# ascending order, write a method to find an element. 

# find the first number on the diagonal that is larger than the number you are looking for. This will be your pivot point
	# In order to find this number on the diagonal, you need to find the end of the diagonal using the start coordinate and end coordinate.
	# once you find the end of the diagonal, find the mid point of the diagonal and see if it is lower or higher than the number you are looking for. If it is higher, adjust your end to be the point just after this midpoint. Else adjust the start to be this midpoint - 1. Continue as long as start is before the end 
# After you find the pivot, calculate the start and end points of the lower left and upper right sub-matrices
# Recurse on these sub-matrices by passing in the original matrix, the new start, new end, and the number you are looking for
	# if either the start or end are out of bounds, return null

class Coordinate:
	def __init__(self, row, col):
		self.row = row
		self.col = col

	def inBounds(self, matrix):
		return (0 <= self.row <= len(matrix) - 1) and (0 <= self.col <= len(matrix[0]) - 1)

	def setAverage(self, min_coord, max_coord):
		row = (min_coord.row + max_coord.row)//2
		col = (min_coord.col + max_coord.col)//2
		self.row = row
		self.col = col

	def isBefore(self, coord):
		return self.row <= coord.row and self.col <= coord.col

	def isEqual(self, coord):
		return (self.row == coord.row) and (self.col == coord.col)

	def clone(self):
		return Coordinate(self.row, self.col)

def findElement(matrix, x):
	origin = Coordinate(0,0)
	dest_row = len(matrix) - 1
	dest_col = len(matrix[0]) - 1
	dest = Coordinate(dest_row, dest_col)
	return recursiveFind(matrix, origin, dest, x)

def recursiveFind(matrix, origin, dest, x):
	if (not origin.inBounds(matrix) or not dest.inBounds(matrix)): # return None if either origin or dest are out of bounds
		return None
	if (not origin.isBefore(dest)):
		return None
	if (origin.isEqual(dest)): 
		if matrix[origin.row][origin.col] == x:
			return origin
		else:
			return None
	diag_dist = min(dest.row - origin.row, dest.col - origin.col)
	end = Coordinate(origin.row + diag_dist, origin.col + diag_dist) # end of the diaganol
	start = origin.clone()
	pivot = findPivot(start, end, matrix, x) # finds the first number on the diagonal that is greater than x
	if matrix[pivot.row][pivot.col] == x: # return the pivot if it is the number you are searching for
		return pivot
	if matrix[pivot.row][pivot.col] < x: # pivot is less than x which means the pivot is at the end of the diaganol so recurse on everything below or to the right of the pivot
		bottom_origin = Coordinate(pivot.row + 1, origin.col)
		right_origin = Coordinate(origin.row, pivot.col + 1)
		recurse_bottom = recursiveFind(matrix, bottom_origin, dest, x)
		if recurse_bottom == None:
			return recursiveFind(matrix, right_origin, dest, x)
		else:
			return recurse_bottom
	else: # else partition and recurse off the pivot
		return partitionAndRecurse(matrix, origin, dest, pivot, x)

def findPivot(start, end, matrix, x):
	while (start.isBefore(end) and (not start.isEqual(end))):
		coord = Coordinate(0, 0)
		coord.setAverage(start, end)
		if (x > matrix[coord.row][coord.col]):
			start.row = coord.row + 1
			start.col = coord.col + 1
		else:
			end.row = coord.row - 1
			end.col = coord.col - 1
	return start

def partitionAndRecurse(matrix, origin, dest, pivot, x):
	lowerLeftOrigin = Coordinate(pivot.row, origin.col)
	lowerLeftDest = Coordinate(dest.row, pivot.col - 1)
	upperRightOrigin = Coordinate(origin.row, pivot.col)
	upperRightDest = Coordinate(pivot.row - 1, dest.col)
	recurseLowerLeft = recursiveFind(matrix, lowerLeftOrigin, lowerLeftDest, x) # recurse on the lower left
	recurseUpperRight = recursiveFind(matrix, upperRightOrigin, upperRightDest, x) # recurse on the upper right
	if recurseLowerLeft != None:
		return recurseLowerLeft
	if recurseUpperRight != None:
		return recurseUpperRight


