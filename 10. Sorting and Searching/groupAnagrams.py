# Write a method to sort an array of strings so that all the anagrams are next to
# each other.

def groupAnagrams(words):
	sorted_words = words
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	# performing a radix sort on the array of words using letter counts
	for letter in alphabet: # iterate over each letter of the alphabet
		ct_dict = {} # dictionary that maps letter count to words
		sorted_bucket = [] # array that will store the sorted words from one iteration of the radix sort
		for string in sorted_words: # iterate over the words and bucket them by their counts for a specific letter in the alphabet
			count = countChar(letter, string)
			ct_dict[count] = ct_dict.get(count, [])
			ct_dict[count].append(string)
		for count in sorted(ct_dict): # combine the buckets in ascending order of lowest letter count to highest
			sorted_bucket += ct_dict[count]
		sorted_words = sorted_bucket
	return sorted_words



def countChar(char, string): # function to count the number of times a specific letter occurs in a word
	count = 0 
	for letter in string:
		if letter == char:
			count += 1
	return count
