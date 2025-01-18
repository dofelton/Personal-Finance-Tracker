from db import db
from models import Transaction
from datetime import datetime

def add_transaction(user_id, amount, category, type):
    transaction = Transaction(user_id, amount, category, datetime.now().isoformat(), type)
    db.collection("transactions").add(transaction.to_dict())
    print("Transaction added.")

def add_income(user_id, amount, category, type):
    income = Transaction(user_id, amount, category, datetime.now().isoformat(), type)
    db.collection("income").add(income.to_dict())
    print("Income added.")

def add_expense(user_id, amount, category, type):
    expense = Transaction(user_id, amount, category, datetime.now().isoformat(), type)
    db.collection("expense").add(expense.to_dict())
    print("Expense added.")

def get_transactions(user_id):
    transactions = db.collection("transactions").where("user_id", "==", user_id).stream()
    return [t.to_dict() for t in transactions]

def get_income(user_id):
    income = db.collection("income").where("user_id", "==", user_id).stream()
    return [i.to_dict() for i in income]

def get_expenses(user_id):
    expenses = db.collection("expense").where("user_id", "==", user_id).stream()
    return [e.to_dict() for e in expenses]

def calculate_summary(user_id):
    income_entries = get_income(user_id)
    expense_entries = get_expenses(user_id)    
    income = sum(i['amount'] for i in income_entries)  # if i['type'] == 'income')
    expenses = sum(e['amount'] for e in expense_entries)  # if e['type'] == 'expense')
    print(f"Total Income: {income}")
    print(f"Total Expenses: {expenses}")
    print(f"Current Balance: {income - expenses}")

def set_budget(user_id, category, amount):
    budget = {"user_id": user_id, "category": category, "amount": amount, "date": datetime.now().isoformat()}
    db.collection("budgets").add(budget)
    print("Budget set.")

def check_budget(user_id, category):
    budgets = db.collection("budgets").where("user_id", "==", user_id).where("category", "==", category).stream()
    for b in budgets:
        print(b.to_dict())

print("Welcome to your Finance Tacker!")
print("")
print("Here you can:\n1 Get account summary\n2 Add an income transaction\n3 Add an expense transaction")
choice = input("What would you like to do?(Enter 1, 2, or 3) ")
# print(choice)
# print(type(choice))
if choice == "1":
    calculate_summary("user1")
elif choice == "2":
    current_income = input("Enter income amount: ")
    income_category = input("What is the income category? ")
    add_income("user1", float(current_income), income_category, "income")
elif choice == "3":
    current_expense = input("Enter expense amount: ")
    expense_category = input("What is the expense category? ")
    add_expense("user1", float(current_expense), expense_category, "expense")
else:
    print("That was not a valid choice.")
