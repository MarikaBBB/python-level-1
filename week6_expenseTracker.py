import csv

def display_menu():
    print("Expense Tracker Menu")
    print("1. Add sample expenses")
    print("2. Display expenses")
    print("3. Exit")

def add_sample_expensive(file_path):
    sample_expenses = [
        ["Date", "Description", "Amount"],
        ["01-01-2024", "Groceries", 40.75],
        ["03-01-2024", "Electricity Bill", 85.50],
        ["10-01-2024", "Dining Out", 80.00],
        ["12-01-2024", "Movie Tickets", 30.00],
        ["15-01-2024", "Gym Membership", 45.00],
        ["18-01-2024", "Office Supplies", 25.30],
        ["20-01-2024", "Public Transportation", 165.00]
    ]
    
    try:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            for expense in sample_expenses:
                writer.writerow(expense)
        print("Samples added successfully.")
    except IOError:
        print("An error occurred when writing to the file.")

def display_expenses(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            expenses = list(reader)
            if len(expenses) == 0:
                print("No expenses found.")
                return
            for row in expenses:
                print(', '.join(row))
    except FileNotFoundError:
        print("No expenses found. Please add some expenses first.")
    except IOError:
        print("An error occurred while reading the file.")

def main():
    path = "expenses.csv"
    
    while True:
        display_menu()
        choice = int(input("Please enter your choice (1, 2, or 3): "))
        
        if choice == 1:
            add_sample_expensive(path)
        elif choice == 2:
            display_expenses(path)
        elif choice == 3:
            print("Exiting expense tracker. Thank you!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
