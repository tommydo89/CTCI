# Write methods to implement the multiply, subtract, and divide operations for integers.
# The results of all of these are integers. Use only the add operator. 

def subtract(a, b):
	length = 0
	temp_b = b
	while temp_b > 0:
		temp_b = temp_b >> 1
		length += 1
	mask = (1 << length) - 1
	complement = (b ^ mask) + 1
	negative_b = (-1 << length) | complement
	return a + negative_b

def multiply(a, b):
	temp_a = a
	temp_b = b
	has_multiplied = 1
	while temp_b > 1:
		temp_b = temp_b >> 1
		temp_a = temp_a << 1
		has_multiplied = has_multiplied << 1
	remaining_multiply = subtract(b, has_multiplied)
	for loop in range(remaining_multiply):
		temp_a += a
	return temp_a

def divide(a, b):
	result = 0
	while a >= b:
		a = subtract(a, b)
		result += 1
	return result