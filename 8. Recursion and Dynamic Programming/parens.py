# Implement an algorithm to print all valid (e.g., properly opened and closed) combinations
# of n pairs of parentheses. 

def parens(num_parens):
	results = []
	recursiveParens('', num_parens, num_parens, results)
	return results

def recursiveParens(parens, left_ct, right_ct, results):
	if (left_ct == 0): # if there are no more left parens, append the remaining rights and then return to end the recursion
		for right in range(right_ct):
			parens = parens + ')'
		results.append(parens)
		return
	recursiveParens(parens + '(', left_ct - 1, right_ct, results) # recurse by appending a left parens
	if (left_ct < right_ct):
		recursiveParens(parens + ')', left_ct, right_ct - 1, results) # recurse by appending a right parens only if there is a matching left parens available