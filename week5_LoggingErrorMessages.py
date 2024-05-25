import datetime

def log_error_message():
    error_message = input("Enter the error message: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("5_loggingError.txt", "a") as file:
        file.write(f"{timestamp}: {error_message}\n")
    print("Error message logged successfully!")

def view_error_messages():
    try:
        with open("5_loggingError.txt", "r") as file:
            entries = file.readlines()
            if entries:
                for entry in entries:
                    print(entry.strip())
            else:
                print("No error messages were found!")
    except FileNotFoundError:
        print("No error messages found.")

def main():
    print("Welcome to the Error Logger!")

    while True:
        print("\nMenu:")
        print("1. Log a new error message")
        print("2. View all error messages")
        print("3. Quit")
        
        choice = input("Please choose an option: ")
        
        if choice == "1":
            log_error_message()
        elif choice == "2":
            view_error_messages()
        elif choice == "3":
            print("You have chosen to Quit, Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
