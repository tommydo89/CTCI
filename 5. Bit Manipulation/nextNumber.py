
def nextNumbers(num):
	nextSmallest = getNextSmallest(num)
	nextLargest = getNextLargest(num)
	return (nextSmallest, nextLargest)

def getNextLargest(num):
	bitMask = getLargeMask(num)
	if not bitMask: # return num if there is no number larger than num with an equal amount of 1s
		return num
	num = num | bitMask # flips the bit from 0 to 1
	shiftMask = bitMask - 1
	num = shiftLarge(num, shiftMask)
	return num

def getNextSmallest(num):
	bitMask = getSmallMask(num)
	if not bitMask: # return num if there is no number smaller than num with an equal amount of 1s
		return num
	num = num & (~bitMask) # flips the bit from 1 to 0 
	shiftMask = bitMask - 1
	num = shiftSmall(num, shiftMask)
	return num


def getLargeMask(num):
	shift = 1 #shift starts at 1 because we are only looking at the 2nd binary digit and onwards
	while (num != 0):
		if num & 3 == 1: # 3 is '11' in binary. We are looking for '01' in num which will equal 1 when & with 3
			break
		num = num >> 1
		shift += 1
	if num == 0: # we return False if we can't find the patten of '01'
		return False
	return (1 << shift)

def getSmallMask(num):
	shift = 1 #shift starts at 1 because we are only looking at the 2nd binary digit and onwards
	while (num != 0):
		if num & 3 == 2: # 3 is '11' in binary. We are looking for '10' in num which will equal 2 when & with 3
			break
		num = num >> 1
		shift += 1
	if num == 0: # we return False if we can't find the pattern of '10'
		return False
	return (1 << shift)

def shiftLarge(num, mask):
	shiftedbits = num & mask # mask is a mask for the bits we want to shift. shiftedbits is a copy of those bits
	while shiftedbits != 0: # repeatedly shifts right until a 1 is cut out
		if shiftedbits & 1 == 1:
			shiftedbits = shiftedbits >> 1
			break
		shiftedbits = shiftedbits >> 1
	num = num & ~(mask) # clears the bits that we were shifting
	num = num | shiftedbits # copies over the newly shifted bits
	return num

def shiftSmall(num, mask):
	bitmask = (mask + 1) >> 1 # a mask for the bit that comes right after the bit we flipped
	shiftedbits = num & mask # mask is a mask for the bits we want to shift. shiftedbits is a copy of those bits
	# we want to append a 1 so if there is already a 1 in the right-most position, we shift left first. Else we can just add 1
	if (shiftedbits & 1 == 1):
		shiftedbits = shiftedbits << 1
	shiftedbits += 1
	while (bitmask & shiftedbits != bitmask): # we know that we have shifted the 1s as far left as they can once bitmask & shiftedbits = bitmask. Ex: 100 & 110 = 100 while 100 & 011 = 0
		shiftedbits = shiftedbits << 1
	num = num & ~(mask) # clears the bits that we were shifting
	num = num | shiftedbits # copies over the newly shifted bits
	return num
