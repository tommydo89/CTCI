# Given an M x N matrix in which each row and each column is sorted in
# ascending order, write a method to find an element. 

# find the first number on the diagonal that is larger than the number you are looking for. This will be your pivot point
	# In order to find this number on the diagonal, you need to find the end of the diagonal using the start coordinate and end coordinate.
	# once you find the end of the diagonal, find the mid point of the diagonal and see if it is lower or higher than the number you are looking for. If it is higher, adjust your end to be the point just after this midpoint. Else adjust the start to be this midpoint - 1. Continue as long as start is before the end 
# After you find the pivot, calculate the start and end points of the lower left and upper right sub-matrices
# Recurse on these sub-matrices by passing in the original matrix, the new start, new end, and the number you are looking for
	# if either the start or end are out of bounds, return null
	# 
class Coordinate:
	def __init__(self, coord):
		self.row = coord[0]
		self.col = coord[1]

	def inBounds(self, matrix):
		return (0 <= self.coord[0] <= len(matrix) - 1) and (0 <= self.coord[1] <= len(matrix[0][0]) - 1)

	def setAverage(self, min_coord, max_coord):
		row = (min_coord.row + max_coord.row)//2
		col = (min_coord.row + max_coord.col)//2
		self.row = row
		self.col = col

	def isBefore(self, coord):
		return self.row < coord.row and self.col < coord.col

def findPivot(start, end, matrix):
	while (start.isBefore(end)):
		p = Coordinate((0,0))
		p.setAverage(start, end)
		if (x > matrix[p.row][p.col]):
			start.row = p.row + 1
			start.col = p.col + 1
		else:
			end.row = p.row - 1
			end.col = p.col - 1

def partitionAndRecurse(matrix, origin, dest, pivot, x):
	



