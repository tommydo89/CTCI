# Write an algorithm which computes the number of trailing zeros in n factorial. 

# I realized that the number of trailing zeros increases by 1 for every factor of 5 that you encounter when you break each number 
# down into it's prime factorization. This is because every time we are able to multiply by 10, the trailing zeros increase by 1. Each pair of 5 and 2 will
# create a 10 but there are a lot more 2s than 5s so we care for only the number of 5s

def factorialZeros(n_factorial):
	zeros = 0
	for number in range(n_factorial, 4, -1): # we know that numbers below 5 will not have a 5 in their prime factorization so we only go down to 5
		current_num = number
		while (current_num % 5 == 0 and current_num >= 5):
			zeros += 1
			current_num /= 5
	return zeros