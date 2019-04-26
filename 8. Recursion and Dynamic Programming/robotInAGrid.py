
def robotInAGrid(rows, columns):
	grid = [[0 for col in range(columns)] for row in range(rows)]
	# only path is all the way down and then all the way right
	setFirstColumn(grid)
	setLastRow(grid)
	path = [] # stores the points for the first successful path found
	failed = [] # stores list of failed points
	# we start the recursion from the end point
	ending_row = rows - 1
	ending_col = columns - 1
	findPath(grid, ending_row, ending_col, path, failed)
	return path


def findPath(grid, row, column, path, failed):
	if (column, row) in failed: # if this point is in our list of failed points, then just return False
		return False
	if grid[row][column] == 0: # if this point is blocked, then add it to the list of failed points
		failed.append((column, row))
		return False
	atOrigin = (row == 0 and column == 0)
	if (atOrigin or findPath(grid, row - 1, column, path, failed) or findPath(grid, row, column - 1, path, failed)): # if we are not at the origin, then recurse to the left and then right
		path.append((column, row))
		return True
	failed.append((column, row)) # if the above if statement does not execute, that means there was no path from this point to the origin so append the point to the list of failed points
	return False


def setFirstColumn(grid):
	for row in range(len(grid)):
		grid[row][0] = 1

def setLastRow(grid):
	lastRow = len(grid) - 1
	row_length = len(grid[0])
	grid[lastRow] = [1] * row_length