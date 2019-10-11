# Write a function that adds two numbers. You should not use+ or any arithmetic
# operators. 

# Attempt

# def addWithoutPlus(num1, num2):
# 	if (num1 > num2):
# 		flip_mask = findFlips(num1, num2)
# 	else:
# 		flip_mask = findFlips(num2, num1)
# 	return (num1 | num2) ^ flip_mask


# def findFlips(bigger, smaller):
# 	carry_over = False
# 	flip_mask = 0
# 	curr_mask = 1
# 	while (bigger > 0 and smaller > 0):
# 		bigger_bit = bigger & 1
# 		smaller_bit = smaller & 1
# 		if (bigger_bit == 1 and smaller_bit == 1 and carry_over == False) or (bigger_bit ^ smaller_bit == 1 and carry_over == True):
# 			flip_mask = flip_mask | curr_mask
# 		if (bigger_bit == 1 and smaller_bit == 1) or (bigger_bit ^ smaller_bit == 1 and carry_over == True):
# 			carry_over = True
# 		else:
# 			carry_over = False
# 		bigger = bigger >> 1
# 		smaller = smaller >> 1
# 		curr_mask = curr_mask << 1
# 	while (carry_over == True):
# 		flip_mask = flip_mask | curr_mask
# 		curr_mask = curr_mask << 1
# 		if (bigger & 1 == 0):
# 			carry_over = False
# 		bigger = bigger >> 1
# 	return flip_mask

# Optimized Solution

def addWithoutPlus(num1, num2):
	while num2 != 0:
		sum_ = num1 ^ num2
		carry = (num1 & num2) << 1
		num1 = sum_
		num2 = carry
	return num1