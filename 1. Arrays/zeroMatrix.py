# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0. 

def zeroMatrix(matrix):
	columns = len(matrix[0])
	rows = len(matrix)
	rowList = []
	columnList = []
	for row in range(0, rows):
		for column in range(0, columns):
			if matrix[row][column] == 0:
				rowList.append(row)
				columnList.append(column)
	zeroRow(matrix, rowList)
	zeroCol(matrix, columnList)
	return matrix


def zeroRow(matrix, rowList):
	columns = len(matrix[0])
	zeros = [0] * columns
	for row in rowList:
		matrix[row] = zeros

def zeroCol(matrix, columnList):
	rows = len(matrix)
	for row in range(0, rows):
		for col in columnList:
			matrix[row][col] = 0
