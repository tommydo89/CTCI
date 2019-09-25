# The Game of Master Mind is played as follows:
# The computer has four slots, and each slot will contain a ball that is red (R). yellow (Y). green (G) or
# blue (B). For example, the computer might have RGGB (Slot #1 is red, Slots #2 and #3 are green, Slot
# #4 is blue).
# You, the user, are trying to guess the solution. You might, for example, guess YRGB.
# When you guess the correct color for the correct slot, you get a "hit:' If you guess a color that exists
# but is in the wrong slot, you get a "pseudo-hit:' Note that a slot that is a hit can never count as a
# pseudo-hit.
# For example, if the actual solution is RGBY and you guess GGRR, you have one hit and one pseudo-hit.
# Write a method that, given a guess and a solution, returns the number of hits and pseudo-hits.

def masterMind(solution, guesses):
	pseudo_hits = {}
	hits = 0
	for slot, guess in zip(solution, guesses):
		if guess == slot:
			hits += 1
		# we can calculate the number of pseudo hits for a ball based on the number of times it appeared in the solution without a correct guess
		# and the number of times it was guessed without being correct. We take the minimum of these two numbers to get the pseudo hits
		else:
			if slot not in pseudo_hits: # maps a ball to the maximum number of pseudo hits it can have
				pseudo_hits[slot] = [0,0]
			pseudo_hits[slot][0] += 1
			if guess not in pseudo_hits: # maps a ball to the number of times it was not guessed correctly
				pseudo_hits[guess] = [0,0]
			pseudo_hits[guess][1] += 1
	pseudo_hit_ct = 0
	for pair in pseudo_hits.values():
		pseudo_hit_ct += min(pair)
	return 'pseudo_hits: ' + str(pseudo_hit_ct) + ' hits: ' + str(hits)
