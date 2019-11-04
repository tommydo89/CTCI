# Given a boolean expression consisting of the symbols 0 (false), 1 (true), &
# (AND), I (OR), and /\ (XOR), and a desired boolean result value result, implement a function to
# count the number of ways of parenthesizing the expression such that it evaluates to result. 
	

def recursiveEvaluate(expression, result):
	if len(expression) == 1: # base case
		if toBool(expression) == result:
			return 1
		return 0
	ways = 0
	for operator_index in range(1, len(expression), 2): # recursively place a parenthesis around everything on the left and the right of an operator 
		left_true = recursiveEvaluate(expression[0:operator_index], True)
		left_false = recursiveEvaluate(expression[0:operator_index], False)
		right_true = recursiveEvaluate(expression[operator_index+1:], True)
		right_false = recursiveEvaluate(expression[operator_index+1:], False)
		total = (left_true + left_false) * (right_true + right_false)
		total_true = 0
		operator = expression[operator_index]
		if operator == '^':
			total_true += (left_true*right_false) + (left_false*right_true)
		if operator == '&':
			total_true += (left_true*right_true)
		if operator == '|':
			total_true += (left_true*right_true) + (left_true*right_false) + (left_false*right_true)
		if result == True:
			ways += total_true
		else: # we subtract total_true from ways in order to get the possible ways to get False as a result
			ways += total - total_true
	return ways


def toBool(char):
	return char == '1'