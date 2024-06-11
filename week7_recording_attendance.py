import openpyxl as o
import pandas as pd
import matplotlib.pyplot as plt

# Define a function to display the menu
def display_menu():
    print("Welcome to the Attendance Tracker!")
    print("Please choose an option:")
    print("1. Record attendance")
    print("2. View all attendance records")
    print("3. Visualize attendance data")
    print("4. Quit")

# Define a function to record attendance
def record_attendance(file_name):
    name = input("Enter employee name: ")
    date = input("Enter date (YYYY-MM-DD): ")
    status = input("Enter status (Present, Absent, Late): ")
    
    # Create a DataFrame with the new attendance record
    new_record = pd.DataFrame({"Name": [name], "Date": [date], "Status": [status]})
    
    # Append the new record to the existing data or create a new file
    try:
        attendance_data = pd.read_excel(file_name)
        attendance_data = pd.concat([attendance_data, new_record], ignore_index=True)
    except FileNotFoundError:
        attendance_data = new_record
    
    # Save the updated data to the Excel file
    attendance_data.to_excel(file_name, index=False)
    print("Attendance recorded successfully.")

# Define a function to view all attendance records
def view_records(file_name):
    try:
        attendance_data = pd.read_excel(file_name)
        print("Displaying Attendance Records:")
        print(attendance_data)
    except FileNotFoundError:
        print("No attendance records found.")

# Define a function to visualize attendance data
def visualize_data(file_name):
    try:
        attendance_data = pd.read_excel(file_name)
        attendance_data['Date'] = pd.to_datetime(attendance_data['Date'])
        attendance_data.set_index('Date', inplace=True)
        
        plt.figure(figsize=(10, 6))
        plt.plot(attendance_data.index, attendance_data['Status'], marker='o', linestyle='-', color='blue')
        plt.title("Attendance Data")
        plt.xlabel("Date")
        plt.ylabel("Attendance Status")
        plt.grid(True)
        plt.show()
    except FileNotFoundError:
        print("No attendance records found.")

# Define the main function to run the program
def main():
    file_name = "attendance.xlsx"
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            record_attendance(file_name)
        elif choice == "2":
            view_records(file_name)
        elif choice == "3":
            visualize_data(file_name)
        elif choice == "4":
            print("Thank you for using the Attendance Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
