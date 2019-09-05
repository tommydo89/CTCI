# Design an algorithm to figure out if someone has won a game of tic-tac-toe. 

#Let's assume that this algorithm will work for any NxN board and that this board is represented by a nested array

def hasWon(player, board):
	if checkRows(player, 0, board) or checkColumns(player, 0, board) or checkDiagonals(player, board):
		return True
	return False

def checkRows(player, row, board):
	if row >= len(board):
		return False
	if board[row] == [player]*len(board):
		return True
	else:
		return checkRows(player, row + 1, board)

def checkColumns(player, col, board):
	if col >= len(board):
		return False
	num_rows = len(board)
	for row in range(num_rows):
		if board[row][col] != player:
			return checkColumns(player, col + 1, board)
	return True

def checkDiagonals(player, board):
	if checkTopDiagonal(player, board) or checkBottomDiagonal(player, board):
		return True
	return False

def checkTopDiagonal(player, board):
	max_len = len(board)
	for row_col in range(max_len):
		if board[row_col][row_col] != player:
			return False
	return True

def checkBottomDiagonal(player, board):
	max_row = len(board) - 1
	for row in range(max_row, -1, -1):
		col = max_row - row
		if board[row][col] != player:
			return False
	return True
