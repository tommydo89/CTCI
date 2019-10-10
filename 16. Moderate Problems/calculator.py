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
	num_stack = Stack() # stack to keep track of numbers
	op_stack = Stack() # stack to keep track of operations
	int_str = ''
	for char in equation:
		if isOperator(char): 
			# when we encounter an operation, push the integer onto the stack and reset it
			num_stack.push(int(int_str))
			int_str = ''

			curr_op = char
			if not op_stack.isEmpty():
				prev_op = op_stack.peek()
				if (higherOrder(prev_op, curr_op)): # performs the previous operation only if its order is greater than or equal to the next operation
					compute(num_stack, op_stack)
			op_stack.push(curr_op)
		else:
			int_str += char
	num_stack.push(int(int_str)) # pushes the last integer onto the stack since the last integer will not have an operation after it to trigger it's push
	while not op_stack.isEmpty(): 
		compute(num_stack, op_stack)
	return num_stack.pop()

def isOperator(char): # checks to see if the character is an operation
	if char == '+' or char == '-' or char == '*' or char == '/':
		return True
	return False

def higherOrder(prevOp, currOp): # checks to see if the previous operation is an order that is equal to or greater than the next operation
	if (prevOp == '-' or prevOp == '+') and (currOp == '*' or currOp == '/'):
		return False
	return True 

def compute(num_stack, op_stack): # applies the previous operation to the previous two numbers
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
