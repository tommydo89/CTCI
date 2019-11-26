# A popular masseuse receives a sequence of back-to-back appointment requests
# and is debating which ones to accept. She needs a 15-minute break between appointments and
# therefore she cannot accept any adjacent requests. Given a sequence of back-to-back appointment requests (all multiples of 15 minutes, none overlap, and none can be moved), find the optimal
# (highest total booked minutes) set the masseuse can honor. Return the number of minutes.
# EXAMPLE
# Input: {30, 15, 60, 75, 45, 15, 15, 45}
# Output180 minutes ({30, 60, 45, 45}). 

def theMasseuse(appointments):
	highest = [None]
	# begin recursion on the first and second element. It would not be optimal to start at the 3rd element or higher bcause at that point you could have
	# included the 1st.
	recurseAdd(0, 0, appointments, highest) # select the first appointment and then recurses on all the different possibilities after
	recurseAdd(1, 0, appointments, highest) # select the second appointment and then recurses on all the different possibilities after
	return highest[0]



def recurseAdd(curr_index, curr_minutes, appointments, highest):
	if curr_index >= len(appointments): # base case 
		if highest[0] == None or curr_minutes > highest[0]:
			highest[0] = curr_minutes
		return
	curr_minutes += appointments[curr_index]
	# we have to skip either one or two elements which would lead us to pick either 2 or 3 elements down. There would be no point in skipping to the 4th element
	# down because at that point you could have also included the 2nd element.
	recurseAdd(curr_index + 2, curr_minutes, appointments, highest) # skips one appointment to select 2nd
	recurseAdd(curr_index + 3, curr_minutes, appointments, highest) # skips two appointments to select 3rd
