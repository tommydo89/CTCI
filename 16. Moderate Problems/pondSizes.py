# You have an integer matrix representing a plot of land, where the value at that location represents the height above sea level. A value of zero indicates water. A pond is a region of
# water connected vertically, horizontally, or diagonally. The size of the pond is the total number of
# connected water cells. Write a method to compute the sizes of all ponds in the matrix. 

def pondSizes(matrix):
	width = len(matrix[0])
	height = len(matrix)
	traversed = [[0 for x in range(width)] for y in range(height)] # create a copy of the matrix that will be used to mark the traversed cells
	pond_sizes = []
	for y in range(height):
		for x in range(width):
			if (traversed[y][x] != 1) and (matrix[y][x] == 0): # only search a cell if it hasn't been traversed and if it is a pond cell
				pond_sizes.append(BFS(matrix, traversed, y, x))
	return pond_sizes


def BFS(matrix, traversed, y, x):
	# if the cell is out of bounds, has been traversed, or if it's not a pound then return 0
	if (y < 0) or (y >= len(matrix)) or (x < 0) or (x >= len(matrix[0])) or (traversed[y][x] == 1) or (matrix[y][x] != 0):
		return 0
	else:
		traversed[y][x] = 1 # mark the cell as having been traversed

		# recursively breadth-first search all cells surrounding the current cell
		BFS_top_left = BFS(matrix, traversed, y - 1, x - 1)
		BFS_top = BFS(matrix, traversed, y - 1, x)
		BFS_top_right = BFS(matrix, traversed, y - 1, x + 1)
		BFS_right = BFS(matrix, traversed, y, x + 1)
		BFS_bottom_right = BFS(matrix, traversed, y + 1, x + 1)
		BFS_bottom = BFS(matrix, traversed, y + 1, x) 	
		BFS_bottom_left = BFS(matrix, traversed, y + 1, x - 1)
		BFS_left = BFS(matrix, traversed, y, x - 1)

		return 1 + BFS_top_left + BFS_top + BFS_top_right + BFS_right + BFS_bottom_right + BFS_bottom + BFS_bottom_left + BFS_left
 