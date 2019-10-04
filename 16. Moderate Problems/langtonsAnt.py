import random as r

# An ant is sitting on an infinite grid of white and black squares. It initially faces right.
# At each step, it does the following:
# (1) At a white square, flip the color of the square, turn 90 degrees right (clockwise), and move forward
# one unit.
# (2) At a black square, flip the color of the square, turn 90 degrees left (counter-clockwise), and move
# forward one unit.
# Write a program to simulate the first K moves that the ant makes and print the final board as a grid.
# Note that you are not provided with the data structure to represent the grid. This is something you
# must design yourself. The only input to your method is K. You should print the final grid and return
# nothing. The method signature might be something like void printKMoves ( int K).

def langtonsAnt(k):
	board = randomizeBoard(k) # initializes the board
	# prints the starting board
	for row in board:
		print(row)
	print() # line separator between starting board and ending board
	mid = len(board) // 2 # used to start the ant in the middle of the board
	curr_row = mid
	curr_col = mid
	direction = { # maps a number to a direction
		1: 'north',
		2: 'east',
		3: 'south',
		4: 'west'
	}
	curr_direction = 2 # represents a starting direction of East or right
	moves = { # maps each color of the square and current direction of the ant to how it should move on the board
		'w': {
			1: (0, 1),
			2: (1, 0),
			3: (0, -1),
			4: (-1, 0)
		},
		'b': {
			1: (0, -1),
			2: (-1, 0),
			3: (0, 1),
			4: (1, 0)		
		}
	}
	# execute k moves where each move we first flip the color of the square, move the ant, and then update it's new position and direction
	for k in range(k):
		curr_color = board[curr_row][curr_col] 
		flip(board, curr_row, curr_col)
		move = moves[curr_color][curr_direction]
		curr_row += move[0]
		curr_col += move[1]
		curr_direction = changeDirection(curr_color, curr_direction)

	# print the ending board
	for row in board:
		print(row)



# intializes a random board
def randomizeBoard(k):
	board_length = 1 + ((k // 2 + 1) * 2)
	board = [[0 for x in range (board_length)] for y in range(board_length)]
	for row in range(board_length):
		for col in range(board_length):
			if (r.random() < 0.5):
				board[row][col] = 'w'
			else:
				board[row][col] = 'b'
	return board

# flips the color of the square
def flip(board, row, col):
	if board[row][col] == 'w':
		board[row][col] = 'b'
	else:
		board[row][col] = 'w'

# updates the direction of the ant after a move occurs
def changeDirection(color, curr_direction):
	if color == 'w':
		if curr_direction == 4:
			return 1
		else:
			return curr_direction + 1
	else:
		if curr_direction == 1:
			return 4
		else:
			return curr_direction - 1
	

