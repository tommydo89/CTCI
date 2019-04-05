# A monochrome screen is stored as a single array of bytes, allowing eight consecutive
# pixels to be stored in one byte. The screen has width w, where w is divisible by 8 (that is, no byte will
# be split across rows). The height of the screen, of course, can be derived from the length of the array
# and the width. Implement a function that draws a horizontal line from ( xl, y) to ( x2, y).
# The method signature should look something like:

screen = bytearray([0] * 25) # example screen of 25 bytes

def drawLine(screen, width, x1, x2, y):
	start_byte = ((y * width) + x1) // 8
	start_bit_index = ((y * width) + x1) % 8
	end_byte = ((y * width) + x2) // 8
	end_bit_index = ((y * width) + x2) % 8
	if (start_bit_index != 0): # if the starting bit isnt the beginning of the byte, we cannot flip the entire byte with setBytes
		setStartByte(screen, start_byte, start_bit_index)
		start_byte += 1 # increment start_byte because we have already correctly changed the first byte
	if (end_bit_index != 7): # if the starting bit isnt the end of the byte, we cannot flip the entire byte with setBytes
		setEndByte(screen, end_byte, end_bit_index) 
		end_byte -= 1 # decrement end_byte because we have already correctly changed the last byte
	setBytes(screen, start_byte, end_byte) # flips the remaining bytes



def setStartByte(screen, byte_num, starting_bit): # flips the bits in a byte starting from the starting_bit to the end
	newByte = 255 >> starting_bit
	screen[byte_num] = newByte

def setEndByte(screen, byte_num, starting_bit): # flips the bits in a byte starting from the starting_bit to the beginning
	newByte = 255 << (8 - (starting_bit + 1))
	screen[byte_num] = newByte

def setBytes(screen, start_byte, end_byte): # flips all bytes in a range indicated by start_byte and end_byte
	for byte in range(start_byte, end_byte + 1):
		screen[byte] = 255

