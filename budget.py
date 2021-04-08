class Budget:
	'''
	Takes in a category and instantiates a budget object
	'''

	def __init__(self, category):
		'''

		'''
		self.category = category
		self.planned_expense = 0
		self.actual_expense = 0

	def get_balance(self):
		'''
		Returns the balance of the budget instance
		'''
		return self.planned_expense - self.actual_expense

	def get_category(self):
		'''
		Returns the category of the budget instance
		'''
		return self.category

	def get_planned_expense(self):
		'''
		Returns the planned expense of the budget instance
		'''
		return self.planned_expense

	def get_actual_expense(self):
		'''
		Returns the actual expense of the budget instance
		'''
		return self.actual_expense

	def increase_planned_expense(self, amount):
		'''
		Takes in an amount and increases the planned expense
		of the instance by that amount
		'''
		self.planned_expense += amount
		return self.planned_expense

	def increase_actual_expense(self, amount):
		'''
		Takes in an amount and increases the actual expense 
		of the instance by that amount	
		'''
		self.actual_expense += amount
		return self.actual_expense

	def reduce_planned_expense(self, amount):
		'''
		Takes in an amount and reduces the planned expense
		of the instance by that amount
		'''
		if self.planned_expense >= amount:
			self.planned_expense -= amount
			return self.planned_expense
		else:
			return {'error': 'Amount too large'}

	def reduce_actual_expense(self, amount):
		'''
		Takes in an amount and reduces the actual expense 
		of the instance by that amount
		'''
		if self.actual_expense >= amount:
			self.actual_expense -= amount
			return self.actual_expense
		else:
			return {'error': 'Amount too large'}

	@staticmethod
	def transfer_balance(category_from, category_to, amount):
		'''
		Takes in two budget categories and an amount
		And transfers the amount from the first budget category to the second
		'''

		if category_from.get_balance() >= amount:
			# Increasing the planned expense increases the balance
			# While reducing the planned expense reduces the balance

			category_from_planned_expense = category_from.reduce_planned_expense(amount)
			category_to_planned_expense = category_to.increase_planned_expense(amount)

			return {'category_from_balance': category_from.get_balance(), 'category_to_balance': category_to.get_balance()}
		else:
			return {'error': 'Insufficient balance to transfer'}

	def __repr__(self):
		'''
		Returns the string representation of the Instantiated object
		'''
		return self.category
