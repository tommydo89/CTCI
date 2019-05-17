# Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and
# pennies (1 cent), write code to calculate the number of ways of representing n cents.

def coins(cents):
	denominations = [25, 10, 5, 1]
	return recursivecoins(cents, denominations, 0)

def recursivecoins(cents, denominations, index):
	if index == len(denominations) - 1 or cents == 0: # we stop the recursion once the denomination is pennies or if we hve represented n cents
		return 1
	current_denomination = denominations[index]
	total = 0
	# we start with the biggest denomination which is quarters, and go down to pennies
	for next_cents in range(cents, -1, -current_denomination): 
		total += recursivecoins(next_cents, denominations, index + 1)
	return total

