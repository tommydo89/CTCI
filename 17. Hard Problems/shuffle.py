# Write a method to shuffle a deck of cards. It must be a perfect shuffle-in other words, each
# of the 52! permutations of the deck has to be equally likely. Assume that you are given a random
# number generator which is perfect. 
from random import randrange 

# if the first n-1 cards are shuffled, we just need to randomly insert the nth card to keep the deck shuffled. Therefore we can shuffle the deck by 
# iterating through the deck and randomly inserting the current card into any of the positions before it. 
def shuffle(deck):
	for curr_pos in range(len(deck)):
		swap_pos = randrange(curr_pos + 1)
		swap(deck, curr_pos, swap_pos)

def swap(deck, curr_pos, swap_pos):
	if curr_pos != swap_pos:
		temp = deck[swap_pos]
		deck[swap_pos] = deck[curr_pos]
		deck[curr_pos] = temp
