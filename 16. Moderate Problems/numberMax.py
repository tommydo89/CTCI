def numberMax(a, b):
	sa = sign(a) 
	sb = sign(b)
	sc = sign(a-b)

	# if a and b have different signs, then we use the sign of a for k in order to account for the case of overflow. 
	# note that if a is - and b is +, k would be - which is the sign of a. And if a is + and b is -, k would be + which is also the sign of a
	# If they are same signs, then we can use the sign of a-b
	use_sign_a = sa ^ sb
	use_sign_c = use_sign_a ^ 1

	k = sa * use_sign_a + sc * use_sign_c
	inverse_k = k ^ 1
	return a * k + b * inverse_k

# this function needs to return 1 for a positive sign, and 0 for negative
def sign(num):
	return flip((num >> 31) & 1)

def flip(num):
	return num^1
