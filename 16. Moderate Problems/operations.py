# Write methods to implement the multiply, subtract, and divide operations for integers.
# The results of all of these are integers. Use only the add operator. 

def subtract(a, b):
	return a + flip_sign(b)

def multiply(a, b):
	if (abs_val(a) < abs_val(b)): # makes the algorithm faster if a < b
		return multiply(b, a)
	total = 0
	for loop in range(abs_val(b)): # adds a to 0 b times
		total += a
	if signs(b) == 0: # if b is negative, we must flip the sign
		total = flip_sign(total)
	return total


def divide(a, b):
	opposite_signs = signs(a) ^ signs(b) # check to see if a and b are opposite signs
	result = 0
	a = abs_val(a)
	b = abs_val(b)
	while a >= b:
		a = subtract(a, b)
		result += 1
	if opposite_signs: # if they are opposite signs, our result must be negative
		result = flip_sign(result)
	return result

# returns 1 if the number is positive, 0 if negative
def signs(num):
	return flip((num >> 31) & 1)

def flip(num):
	return num^1

# flips the sign of the number
def flip_sign(num):
	return (num ^ -1) + 1

# returns absolute value of number
def abs_val(num):
	if signs(num) == 0:
		return flip_sign(num)
	return num