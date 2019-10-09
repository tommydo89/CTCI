# Given an arithmetic equation consisting of positive integers,+,-,* and/ (no parentheses),
# compute the result. 

class Stack:

	def __init__(self):
		self.items = []

	def push(self, val):
		self.items.append(val)

	def pop(self):
		return self.items.pop()

	def isEmpty(self):
		return len(self.items) == 0

	def peek(self):
		last_index = len(self.items) - 1
		return self.items[last_index]


def calculator(equation):
	num_stack = Stack()
	op_stack = Stack()
	int_str = ''
	for char in equation:
		if isOperator(char):
			num_stack.push(int(int_str))
			int_str = ''
			curr_op = char
			if not op_stack.isEmpty():
				prev_op = op_stack.peek()
				if (higherOrder(prev_op, curr_op)):
					compute(num_stack, op_stack)
			op_stack.push(curr_op)
		else:
			int_str += char
	num_stack.push(int(int_str))
	while not op_stack.isEmpty():
		compute(num_stack, op_stack)
	return num_stack.pop()

def isOperator(char):
	if char == '+' or char == '-' or char == '*' or char == '/':
		return True
	return False

def higherOrder(prevOp, currOp):
	if (prevOp == '-' or prevOp == '+') and (currOp == '*' or currOp == '/'):
		return False
	return True 

def compute(num_stack, op_stack):
	operation = op_stack.pop()
	num2 = num_stack.pop()
	num1 = num_stack.pop()
	if operation == '+':
		num_stack.push(num1 + num2)
	if operation == '-':
		num_stack.push(num1 - num2)
	if operation == '*':
		num_stack.push(num1 * num2)
	if operation == '/':
		num_stack.push(num1 / num2)
