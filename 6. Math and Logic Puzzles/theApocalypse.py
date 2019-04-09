# In the new post-apocalyptic world, the world queen is desperately concerned
# about the birth rate. Therefore, she decrees that all families should ensure that they have one girl or
# else they face massive fines. If all families abide by this policy-that is, they have continue to have
# children until they have one girl, at which point they immediately stop-what will the gender ratio
# of the new generation be? (Assume that the odds of someone having a boy or a girl on any given
# pregnancy is equal.) Solve this out logically and then write a computer simulation of it. 

import random

def nextGeneration(families):
	nextGeneration = [0,0] # first index is for girls, second is for boys
	for family in range(0, families):
		giveBirth(nextGeneration)
	return nextGeneration

def giveBirth(array):
	gender = random.uniform(0,1)
	while (gender > 0.5):
		array[1] += 1
		gender = random.uniform(0,1)
	array[0] += 1