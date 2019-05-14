# Implement the "paint fill" function that one might see on many image editing programs.
# That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color,
# fill in the surrounding area until the color changes from the original color
screen = [['white' for row in range(4)] for col in range(4)]
screen[1][1] = 'black'
screen[1][2] = 'black'
screen[2][1] = 'black'
screen[2][2] = 'black'
# visual of screen
	# wwww
	# wbbw
	# wbbw
	# wwww
def paintFill(screen, point, new_color):
	x_coord = point[0]
	y_coord = point[1]
	start_color = screen[y_coord][x_coord]
	max_x = len(screen[0])
	max_y = len(screen)
	recursiveFill(screen, max_x, max_y, point, start_color, new_color)


def recursiveFill(screen, max_x, max_y, point, start_color, new_color):
	x_coord = point[0]
	y_coord = point[1]
	if ((x_coord in range(0,max_x)) and (y_coord in range(0, max_y)) and screen[y_coord][x_coord] == start_color):
		screen[y_coord][x_coord] = new_color
		recursiveFill(screen, max_x, max_y, [point[0]] + [point[1] - 1], start_color, new_color) # Up
		recursiveFill(screen, max_x, max_y, [point[0] + 1] + [point[1]], start_color, new_color) # Right
		recursiveFill(screen, max_x, max_y, [point[0]] + [point[1] + 1], start_color, new_color) # Down
		recursiveFill(screen, max_x, max_y, [point[0] - 1] + [point[1]], start_color, new_color) # Left