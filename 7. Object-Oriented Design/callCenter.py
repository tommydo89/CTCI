class Employee:
	__init__(self):

	def assignCall(self, call):

	def escalateAndReassign(self):

	def isFree(self):

	def getRank(self):
		return self.rank

class Director(Employee):
	__init__(self):
		self.rank = 'Director'

class Manager(Employee):
	__init__(self):
		self.rank = 'Manager'

class Respondent(Employee):
	__init__(self):
		self.rank = 'Respondent'

class Call:

	__init__(self, caller):
		self.caller = caller
		self.rank = None

	def setHandler(self, employee):

	def disconnect(self):

	def incrementRank(self):

	def setRank(self):

	def getRank(self):


class CallCenter:

	__init__(self, call_queues, employees):
		self.call_queues = call_queues
		self.employees = employees

	def dispatchCall(call):
		employee = getHandlerForCall(call)
		if employee != None:
			employee.assignCall(call)
		else:
			call_queues[call.getRank()].append(call)

	def getHandlerForCall(call):











