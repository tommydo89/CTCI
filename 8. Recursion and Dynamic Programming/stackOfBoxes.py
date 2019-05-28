# You have a stack of n boxes, with widths wi
# , heights hi
# , and depths di
# . The boxes
# cannot be rotated and can only be stacked on top of one another if each box in the stack is strictly
# larger than the box above it in width, height, and depth. Implement a method to compute the
# height of the tallest possible stack. The height of a stack is the sum of the heights of each box. 

def stackofBoxes(boxes):
	results = []
	recursiveBoxes(0, boxes, results)
	return max(results)


def recursiveBoxes(height, remaining_boxes, results):
	if len(remaining_boxes) == 0: # base case where are no more remaining boxes
		results.append(height)
		return
	for box in remaining_boxes: # recurse on each remaining box
		recursiveBoxes(height+box[1], remainingPossibleBoxes(box, remaining_boxes), results)


def remainingPossibleBoxes(top_box, remaining_boxes): # returns a list of the remaining possible boxes
	remaining_possible = []
	for box in remaining_boxes:
		if (box[0] < top_box[0] and box[1] < top_box[1] and box[2] < top_box[2]):
			remaining_possible.append(box)
	return remaining_possible