# Given a list of people with their birth and death years, implement a method to
# compute the year with the most number of people alive. You may assume that all people were born
# between 1900 and 2000 (inclusive). If a person was alive during any portion of that year, they should
# be included in that year's count. For example, Person (birth= 1908, death= 1909) is included in the
# counts for both 1908 and 1909.

def livingPeople(person_list):
	year_arr = [0] * 101 # initialize an array of 101 values(the number of people alive each year) for each year between 1900 and 2000
	for person in person_list:
		year_arr[person['birth']-1900] += 1
		if person['death'] != 2000: # index out of bounds if year of death == 2000
			year_arr[(person['death']-1900) + 1] -= 1 # we subtract from the next year since they were alive for the duration of their death year
	year_most_alive = -1
	highest_number_alive = -1
	current_number_alive = 0
	current_year = 1900
	for alive in year_arr:
		current_number_alive += alive
		if current_number_alive > highest_number_alive:
			highest_number_alive = current_number_alive
			year_most_alive = current_year
		current_year += 1
	return year_most_alive

# Example
# 1900 - 2 alive
# 1901 - 3 alive
# 1902 - 4 alive
# answer - 1902
person_list = [{'birth':1900, 'death':1901}, {'birth':1900, 'death':1901}, {'birth':1901, 'death':1902}, {'birth':1902, 'death':1902}, {'birth':1902, 'death':1902}, {'birth':1902, 'death':1902}]