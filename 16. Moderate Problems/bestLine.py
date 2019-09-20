# Given a two-dimensional graph with points on it, find a line which passes the most
# number of points. 

class Point:

	def __init__(self, x, y):
		self.x = x
		self.y = y


def bestLine(points):
	lines = {}
	vertical_lines = {}
	for point_1 in points:
		for point_2 in points:
			if point_2 != point_1:
				slope = calc_slope(point_1, point_2)
				intercept = y_intercept(point_1, float(slope))
				if slope == 'Infinity':
					vertical_lines[str(point_1.x)] = vertical_lines.get(str(point_1.x), 0) + 1
				else:
					if slope not in lines:
						lines[slope] = {intercept:1}
					else:
						lines[slope][intercept] = lines.get(slope).get(intercept, 0) + 1
	highest = 0
	bestLine = -1
	for slope in lines.keys():
		for intercept, count in lines[slope].items():
			if count > highest:
				highest = count
				bestLine = 'y = ' + slope + 'x + ' + intercept
	for x_intercept, count in vertical_lines.items():
		if count > highest:
			highest = count
			bestLine = 'x = ' + x_intercept
	return bestLine







def calc_slope(p1, p2):
	if (p1.x == p2.x):
		return 'Infinity'
	return str((p2.y - p1.y) / (p2.x - p1.x))


def y_intercept(point, slope):
	return str(point.y - (slope*point.x))

