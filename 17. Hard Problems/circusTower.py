# A circus is designing a tower routine consisting of people standing atop one another's shoulders. For practical and aesthetic reasons, each person must be both shorter and lighter
# than the person below him or her. Given the heights and weights of each person in the circus, write
# a method to compute the largest possible number of people in such a tower. 

def circusTower(pairs):
	pairs.sort() # sorts pairs of height and weight by the 1st element(height)
	longest_subseqs = [] # keeps track of all the longest possible subsequences
	longest_seq = None
	minimum = None
	for pair in pairs:
		if longest_seq == None: # initializes all the important variables at the start of the loop
			longest_subseqs.append([pair])
			minimum = pair[1]
			longest_seq = [pair]
		elif pair[1] < minimum: # adds a new subsequence if this number cannot be added to any of the subsequences thus far
			longest_subseqs.append([pair])
			minimum = pair[1]
		else:
			for seq in longest_subseqs: # iterates through each subsequence and appends the pair to the subsequence if valid
				last_num = seq[len(seq) - 1][1]
				if pair[1] > last_num:
					seq.append(pair)
					if len(seq) > len(longest_seq): # updates the longest sequence if one occurs
						longest_seq = seq
	return longest_seq

