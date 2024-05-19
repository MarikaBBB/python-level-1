# Print a welcome message
print("Welcome to the Financial Tracker!")

# Create empty lists to store incomes and expenses
incomes = []
expenses = []

# Main loop for the financial tracker program
while True:
    # Prompt the user to choose an action
    action = input("Enter '1' to add income, '2' to add an expense, '3' to view financial summary, and '4' to quit: ")
    
    # Add an income
    if action == '1':
        amount = float(input("Enter the income amount: "))
        incomes.append(amount)
        print("Income added successfully.")
    
    # Add an expense
    elif action == '2':
        amount = float(input("Enter the expense amount: "))
        expenses.append(amount)
        print("Expense added successfully.")
    
    # View financial summary
    elif action == '3':
        total_income = sum(incomes)
        total_expenses = sum(expenses)
        remaining_balance = total_income - total_expenses
        print(f"\nFinancial Summary:")
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Remaining Balance: ${remaining_balance:.2f}")
    
    # Quit the program
    elif action == '4':
        print("Exiting program, goodbye!")
        break
    
    # Error handling for incorrect inputs
    else:
        print("Incorrect input, try again.")
