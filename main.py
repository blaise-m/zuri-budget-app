from budget import Budget
from datetime import datetime
from os import system, name


categories = []


def clear():
	'''
	Clears screen for windows and linux
	Else does nothing
	'''
	try:
		if name == 'nt':
			system('cls')
		else:
			system('clear')
	except:
		pass


def amount_to_spend(budget_categories):
	'''
	Takes in a list of budget categories
	And returns the total balance for all the categories
	'''
	amount_to_spend = 0
	
	for category in budget_categories:
		amount_to_spend += category.get_balance()

	return amount_to_spend


def display_categories(budget_categories):
	'''
	Takes in a list of budget categories and displays them in a table
	'''
	print("\n\nNo.".ljust(9, " ") +
		"Budget Category".ljust(25, " ") +
		"Planned Expense".ljust(20, " ") +
		"Actual Expense".ljust(20, " ") +
		"Balance")
	print("".ljust(85, "-"))
	for index, category in enumerate(budget_categories):
		print(f"{index+1}".ljust(7, " ") +
			f"{category.get_category()}".ljust(25, " ") +
			f"{category.get_planned_expense():,.2f}".ljust(20, " ") +
			f"{category.get_actual_expense():,.2f}".ljust(20, " ") +
			f"{category.get_balance():,.2f}")


def init(budget_categories):
	'''
	Initializes the budget app
	'''
	clear()
	print("\nWELCOME TO ZURI BUDGET APP")
	print("***************************\n")

	print(f"{datetime.now().strftime('%c')}")
	print(f"${amount_to_spend(budget_categories):,.2f} available for Spending")

	display_categories(budget_categories)

	print("\n\nAllowed Actions:")
	print("\n1. Add a budget category".ljust(36, " ") + "2. Increase planned expense")
	print("3. Reduce planned expense".ljust(35, " ") + "4. Add a category expense")
	print("5. Reduce a category expense".ljust(35, " ") + "6. Transfer category balances")
	print("7. Exit")

	response = input("\nPlease select an option to proceed: ")

	if response == "1":
		add_category()
		init(budget_categories)
	elif response == "2":
		increase_planned_expense(budget_categories)
	elif response == "3":
		reduce_planned_expense(budget_categories)
	elif response == "4":
		add_expense(budget_categories)
	elif response == "5":
		reduce_expense(budget_categories)
	elif response == "6":
		transfer_balance(budget_categories)
	elif response == "7":
		exit()
	else:
		print("Invalid input!!")


def add_category():
	response = input("Enter the Category Name: ")
	category = Budget(f"{response.title()}")
	categories.append(category)


def increase_planned_expense(budget_categories):
	try:
		index = int(input("Enter the Category number: "))
		amount = float(input("Enter the amount: "))
	except:
		print("\nInvalid input!! Enter a valid number or amount")
		increase_planned_expense(budget_categories)

	if index in range(1, len(budget_categories)+1):
		budget_categories[index-1].increase_planned_expense(amount)
		init(budget_categories)
	else:
		print("\nInvalid input!! Enter a valid number")
		increase_planned_expense(budget_categories)


def reduce_planned_expense(budget_categories):
	try:
		index = int(input("Enter the Category number: "))
		amount = float(input("Enter the amount: "))
	except:
		print("\nInvalid input!! Enter a valid number or amount")
		reduce_planned_expense(budget_categories)

	if index in range(1, len(budget_categories)+1):
		budget_categories[index-1].reduce_planned_expense(amount)
		init(budget_categories)
	else:
		print("\nInvalid input!! Enter a valid number")
		reduce_planned_expense(budget_categories)


def add_expense(budget_categories):
	try:
		index = int(input("Enter the Category number: "))
		amount = float(input("Enter the amount: "))
	except:
		print("\nInvalid input!! Enter a valid number or amount")
		add_expense(budget_categories)

	if index in range(1, len(budget_categories)+1):
		budget_categories[index-1].increase_actual_expense(amount)
		init(budget_categories)
	else:
		print("\nInvalid input!! Enter a valid number")
		increase_planned_expense(budget_categories)


def reduce_expense(budget_categories):
	try:
		index = int(input("Enter the Category number: "))
		amount = float(input("Enter the amount: "))
	except:
		print("\nInvalid input!! Enter a valid number or amount")
		reduce_planned_expense(budget_categories)

	if index in range(1, len(budget_categories)+1):
		budget_categories[index-1].reduce_actual_expense(amount)
		init(budget_categories)
	else:
		print("\nInvalid input!! Enter a valid number")
		reduce_planned_expense(budget_categories)


def transfer_balance(budget_categories):
	try:
		index1 = int(input("Enter the category number of the category to transfer from: "))
		index2 = int(input("Enter the category number of the category to transfer to: "))
		amount = float(input("Enter the amount to transfer: "))
	except:
		print("\nInvalid input!! Enter a valid number or amount")
		reduce_planned_expense(budget_categories)

	if index1 in range(1, len(budget_categories)+1) and index2 in range(1, len(budget_categories)+1):
		Budget.transfer_balance(budget_categories[index1-1], budget_categories[index2-1], amount)
		init(budget_categories)
	else:
		print("\nInvalid input!! Enter a valid number")
		reduce_planned_expense(budget_categories)


if __name__ == "__main__":	

	food = Budget("Food")
	categories.append(food)

	clothing = Budget("Clothing")
	categories.append(clothing)

	entertainment = Budget("Entertainment")
	categories.append(entertainment)	

	init(categories)
	