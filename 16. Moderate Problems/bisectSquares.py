# Given two squares on a two-dimensional plane, find a line that would cut these two
# squares in half. Assume that the top and the bottom sides of the square run parallel to the x-axis. 

class Point:

	def __init__(self, x, y):
		self.x = x
		self.y = y

class Square:

	def __init__(self, p1, p2, p3, p4):
		self.bottomLeft = p1
		self.topLeft = p2
		self.topRight = p3
		self.bottomRight = p4

	def center(self):
		x = (self.bottomLeft.x + self.bottomRight.x) / 2
		y = (self.bottomLeft.y + self.topLeft.y) / 2
		return Point(x,y)

# note that in order for a line to cut the two squares in half, the line must go through both of their centers
def bisectSquares(sq1, sq2):
	sq1_center = sq1.center()
	sq2_center = sq2.center()
	m = slope(sq1_center, sq2_center)
	if m == 'Infinity':
		return 'x = ' + str(sq1_center.x)
	if m == 0:
		return 'y = ' + str(sq1_center.y)
	b = sq1_center.y - (m*sq1_center.x)
	return 'y = ' + str(m) + 'x + ' + str(b) 


def slope(p1, p2):
	if (p1.x == p2.x):
		return 'Infinity'
	return (p2.y - p1.y) / (p2.x - p1.x)

# Example
sq1 = Square(Point(0,0), Point(0,2), Point(2,2), Point(2,0))
sq2 = Square(Point(3,3), Point(3,5), Point(5,5), Point(5,3))
