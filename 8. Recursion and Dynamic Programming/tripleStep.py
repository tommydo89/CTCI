# A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
# steps at a time. Implement a method to count how many possible ways the child can run up the
# stairs. 

def tripleStep(stair_length, stored_results):
	if stair_length == 0: # if stair_length is 0, that means the series of steps we took works 
		return 1
	if stair_length < 0:
		return 0
	if stair_length in stored_results: # checks the dictionary to see if we already have the stored answer for this recursive call
		return stored_results[stair_length]
	one_step = tripleStep(stair_length - 1, stored_results)
	two_step = tripleStep(stair_length - 2, stored_results)
	three_step = tripleStep(stair_length - 3, stored_results)
	stored_results[stair_length] = one_step + two_step + three_step # store the solution to the recursive call so that further identical recursive calls will be solved with a O(1) look up
	return one_step + two_step + three_step
