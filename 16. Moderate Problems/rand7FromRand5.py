# Implement a method rand7() given rand5( ). That is, given a method that
# generates a random number between O and 4 (inclusive), write a method that generates a random
# number between O and 6 (inclusive).

import random

def rand7():
	return rand5() + 0.5*rand5()

def rand5():
	return random.uniform(0,4)
