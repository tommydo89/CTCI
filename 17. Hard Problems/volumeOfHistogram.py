# Imagine a histogram (bar graph). Design an algorithm to compute the
# volume of water it could hold if someone poured water across the top. You can assume that each
# histogram bar has width 1.
# EXAMPLE (Black bars are the histogram. Gray is water.)
# lnput:{0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0} 

# key concept: if you find the tallest bar in the array, you can only fill water up to the next tallest bar on its left and right. 
def volumeOfHistogram(arr):
	return search(arr)
	

def search(arr):
	index_high = findHighIndex(arr)
	return searchLeft(arr[:index_high]) + searchRight(arr, index_high+1)

def searchLeft(arr):
	if len(arr) <= 1: # base case
		return 0
	index_high = findHighIndex(arr)
	highest = arr[index_high]
	water_volume = sumWaterVolume(arr, index_high, 'left') # calculates the volume of water to the right of this bar (incl. any bars)
	bar_volume = sumBarVolume(arr, index_high, 'left') # calculates the volume of bars to the right of this bar
	actual_volume = water_volume - bar_volume # calculates the actual volume of water when excluding the volume of bars
	return actual_volume + searchLeft(arr[:index_high]) # recurse on everything to the left of the tallest bar

def searchRight(arr, index):
	if index >= len(arr) or len(arr[index:]) == 1: # base case
		return 0
	arr = arr[index:]
	index_high = findHighIndex(arr)
	highest = arr[index_high]
	water_volume = sumWaterVolume(arr, index_high, 'right') # calculates the volume of water to the left of this bar (incl. any bars)
	bar_volume = sumBarVolume(arr, index_high, 'right') # calculates the volume of bars to the left of this bar
	actual_volume = water_volume - bar_volume # calculates the actual volume of water when excluding the volume of bars
	return actual_volume + searchRight(arr, index_high + 1) # recurse on everything to the right of the tallest bar

def sumWaterVolume(arr, index, side): # sums the volume of water(including bars)
	highest = arr[index]
	if side == 'left':
		if index == len(arr) - 1:
			return 0
		else:
			return highest * len(arr[index+1:])
	else:
		return highest * len(arr[:index])

def sumBarVolume(arr, index, side): # sums the volume of the bars
	if side == 'left':
		if index == len(arr) - 1:
			return 0
		else:
			return sum(arr[index+1:])
	else:
		return sum(arr[:index])


def findHighIndex(arr): # returns the index of the tallest bar in the array
	index = 0 
	highest_index = -1
	greatest = -1
	for num in arr:
		if greatest == -1 or num > greatest:
			greatest = num
			highest_index = index
		index += 1
	return highest_index