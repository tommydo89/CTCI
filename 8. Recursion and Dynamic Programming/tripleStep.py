# A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
# steps at a time. Implement a method to count how many possible ways the child can run up the
# stairs. 

def tripleStep(stair_length):
	if stair_length == 0:
		return 1
	if stair_length < 0:
		return 0
	return tripleStep(stair_length - 1) + tripleStep(stair_length - 2) + tripleStep(stair_length - 3)
