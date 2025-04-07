#type: ignore
import numpy as np

def display_menu():
    print("\nWelcome to the Personal Budget Analyzer!")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Budget Summary")
    print("4. Exit")
    return input("Enter your choice (1-4): ")

def add_income(income_list):
    try:
        amount = float(input("Enter income amount: "))
        source = input("Enter income source (e.g., salary, freelance): ")
        income_list.append((amount, source))
        print(f"Income of {amount} from {source} added successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid number for income.")

def add_expense(expense_list):
    try:
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category (e.g., groceries, rent): ")
        expense_list.append((amount, category))
        print(f"Expense of {amount} for {category} added successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid number for expense.")

def budget_summary(income_list, expense_list):
    if not income_list and not expense_list:
        print("No income or expenses recorded yet.")
        return
    
    income_array = np.array([item[0] for item in income_list])
    expense_array = np.array([item[0] for item in expense_list])
    
    total_income = np.sum(income_array) if income_array.size > 0 else 0
    total_expense = np.sum(expense_array) if expense_array.size > 0 else 0
    savings = total_income - total_expense
    
    avg_income = np.mean(income_array) if income_array.size > 0 else 0
    avg_expense = np.mean(expense_array) if expense_array.size > 0 else 0
    print("\nBudget Summary:")
    print(f"Total Income: {total_income:.2f}")
    print(f"Total Expenses: {total_expense:.2f}")
    print(f"Savings: {savings:.2f}")
    print(f"Average Income: {avg_income:.2f}")
    print(f"Average Expense: {avg_expense:.2f}")
    
    if income_list:
        print("\nIncome Sources:")
        for amount, source in income_list:
            print(f"{source}: {amount:.2f}")
    if expense_list:
        print("\nExpense Categories:")
        for amount, category in expense_list:
            print(f"{category}: {amount:.2f}")

def main():
    income_list = []
    expense_list = []
    while True:
        choice = display_menu()
        if choice == "1":
            add_income(income_list)
        elif choice == "2":
            add_expense(expense_list)
        elif choice == "3":
            budget_summary(income_list, expense_list)
        elif choice == "4":
            print("Thank you for using the Personal Budget Analyzer!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
