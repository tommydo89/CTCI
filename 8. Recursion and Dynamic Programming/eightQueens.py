# Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board
# so that none of them share the same row, col, or diagonal. In this case, "diagonal" means all
# diagonals, not just the two that bisect the board. 
import copy

def eightQueens(board):
	results = []
	recursiveEightQueens(board, 0, [], results)
	return results

def recursiveEightQueens(board, row, positions, results):
	if row == 8:
		results.append(positions)
		return
	available_cols = board[row]
	if len(available_cols) == 0:
		return
	for col in available_cols:
		board_copy = copy.deepcopy(board)
		board_copy[row].remove(col)
		positions_copy = copy.copy(positions)
		positions_copy.append(col)
		clearSpace(board_copy, row, col)
		recursiveEightQueens(board_copy, row + 1, positions_copy, results)

def clearSpace(board, row, col):
	clearColumn(board, col)
	clearDiagonals(board, row, col)

def clearColumn(board, col):
	for row in board:
		if col in row:
			row.remove(col)

def clearDiagonals(board, row, col):
	clearTopDiagonals(board, row, col)
	clearBottomDiagonals(board, row, col)

def clearTopDiagonals(board, row, col):
	left = col - 1
	right = col + 1
	for row in range(row - 1, -1, -1):
		if (left >= 0 and left in board[row]):
			board[row].remove(left)
		if (right <= 7 and right in board[row]):
			board[row].remove(right)
		left -= 1
		right += 1

def clearBottomDiagonals(board, row, col):
	left = col - 1
	right = col + 1
	for row in range(row + 1, 8):
		if (left >= 0 and left in board[row]):
			board[row].remove(left)
		if (right <= 7 and right in board[row]):
			board[row].remove(right)
		left -= 1
		right += 1