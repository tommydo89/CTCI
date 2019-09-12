# Given any integer, print an English phrase that describes the integer (e.g., "One Thousand, Two Hundred Thirty Four").
def englishInt(number):
	number_scale = ['', 'Thousand', 'Million' , 'Billion', 'Trillion', 'Quadrillion', 'Quintillion', 'Sextillion', 'Septillion']
	result_string = ''
	num_string = format(number, ',d')
	if num_string[0] == '-':
		result_string += 'Negative'
		num_string = num_string[1:]
	num_array = num_string.split(',')
	max_index = len(num_array) - 1
	for index in range(max_index + 1):
		result_string += parse(num_array[index]) + ' ' + number_scale[max_index - index] + ' '
	return result_string




def parse(number):
	return parse_digit_3(number) + parse_digit_2(number) + parse_digit_1(number)

def parse_digit_3(number):
	if len(number) != 3:
		return ''
	digit = number[0]
	number_map = {
		'1': 'One Hundred ',
		'2': 'Two Hundred ',
		'3': 'Three Hundred ',
		'4': 'Four Hundred ',
		'5': 'Five Hundred ',
		'6': 'Six Hundred ',
		'7': 'Seven Hundred ',
		'8': 'Eight Hundred ',
		'9': 'Nine Hundred '
	}
	return number_map.get(digit)

def parse_digit_2(number):
	if len(number) == 3:
		digit = number[1]
	if len(number) == 2:
		digit = number[0]
	if  len(number) == 1:
		return ''
	number_map = {
		'1': '',
		'2': 'Twenty ',
		'3': 'Thirty ',
		'4': 'Fourty ',
		'5': 'Fifty ',
		'6': 'Sixty ',
		'7': 'Seventy ',
		'8': 'Eighty ',
		'9': 'Ninety '
	}
	return number_map.get(digit)

def parse_digit_1(number):
	if len(number) == 3:
		digit_2 = number[1]
		digit = number[2]
	if len(number) == 2:
		digit_2 = number[0]
		digit = number[1]
	if len(number) == 1:
		digit_2 = None
		digit = number[0]
	if (digit_2 == '1'):
		number_map = {
			'0': 'Ten',
			'1': 'Eleven',
			'2': 'Twelve',
			'3': 'Thirteen',
			'4': 'Fourteen',
			'5': 'Fifteen',
			'6': 'Sixteen',
			'7': 'Seventeen',
			'8': 'Eighteen',
			'9': 'Nineteen',
		}
	else:
		number_map = {
		'0': '',
		'1': 'One',
		'2': 'Two',
		'3': 'Three',
		'4': 'Four',
		'5': 'Five',
		'6': 'Six',
		'7': 'Seven',
		'8': 'Eight',
		'9': 'Nine'
		}
	return number_map.get(digit)
