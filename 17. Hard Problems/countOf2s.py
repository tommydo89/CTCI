def countOf2s(num):
	num_str = str(num)
	base_10 = 10**(len(num_str)-1)
	total = 0
	for index in range(0, len(num_str)):
		if index == 0: # handles the first digit
			if int(num_str[index]) == 2:
				total += int(num_str[index+1:]) + 1
			elif int(num_str[index]) > 2:
				total += base_10
		elif index == len(num_str) - 1: # handles the last digit
			if int(num_str[index]) >= 2:
				total += int(num_str[:index]) + 1
			else:
				total += int(num_str[:index])
		else: # handles every digit besides the first and last
			if int(num_str[index]) == 2:
				total += (int(num_str[:index]) * base_10) + (num_str[index+1:] + 1)
			elif int(num_str[index]) > 2:
				total += (int(num_str[:index]) + 1) * base_10
			else:
				total += int(num_str[:index]) * base_10
		base_10 /= 10
	return total
