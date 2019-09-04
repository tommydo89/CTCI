class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Line:
	def __init__(self, a, b):
		if a.x <= b.x:
			self.start = a
			self.end = b
		else:
			self.start = b
			self.end = a

	def slope(self):
		if self.start.x == self.end.x:
			return 'Infinity'
		return (self.end.y - self.start.y)/(self.end.x - self.start.x)

	def y_intercept(self):
		return (self.start.y - (self.slope()*self.start.x))

	def intersects(self, line):
		if self.slope() == 'Infinity' or line.slope() == 'Infinity':
			if self.slope() == 'Infinity' and line.slope() == 'Infinity' and self.start.x == line.start.x:
				if (line.start.y <= self.start.y <= line.end.y):
					return self.start
				if (self.start.y <= line.start.y <= self.end.y):
					return line.start
			if self.slope() == 'Infinity':
				y = line.slope()*self.start.x + line.y_intercept()
				if self.start.y <= y <= self.end.y:
					return (self.start.x, y)
			else:
				y = self.slope()*line.start.x + self.y_intercept()
				if line.start.y <= y <= line.end.y:
					return (line.start.x, y)
			return False
		if self.slope() == line.slope() and self.y_intercept() == line.y_intercept():
			if (line.start.x <= self.start.x <= line.end.x):
				return self.start
			if (self.start.x <= line.start.x <= self.end.x):
				return line.start
			return False
		elif self.slope() != line.slope():
			x_intersect = (self.y_intercept() - line.y_intercept())/(line.slope() - self.slope())
			if (self.start.x <= x_intersect <= self.end.x) and (line.start.x <= x_intersect <= line.end.x):
				y_intersect = (self.slope()*x_intersect) + self.y_intercept()
				return (x_intersect, y_intersect)
		return False

#example

#1
# L1Start = Point(0,0)
# L1End = Point(0,2)

# L2Start = Point(-1,1)
# L2End = Point(1,1)

#2
# L1Start = Point(0,0)
# L1End = Point(0,2)

# L2Start = Point(1,1)
# L2End = Point(-3,-3)

#3
L1Start = Point(-10,5)
L1End = Point(5,5)

L2Start = Point(-5,-11)
L2End = Point(5,9)

L1 = Line(L1Start, L1End)
L2 = Line(L2Start, L2End)





