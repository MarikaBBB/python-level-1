import datetime

def add_entries():
    date = input("Enter the date for the diary entry (DD-MM-YY) or leave blank to use today's date: ")
    if date == "":
        date = datetime.date.today().strftime("%d-%m-%y")
    entry = input("Enter the diary entry you want to enter: ")
    with open("diary.txt", "a") as file:
        file.write(f"{entry} - {date}\n")
    print("Diary entry was written successfully!")

def view_entries():
    try:
        with open("diary.txt", "r") as file:
            entries = file.readlines()
            if entries:
                for entry in entries:
                    print(entry.strip())
            else:
                print("No diary entries were found!")
    except FileNotFoundError:
        print("No diary entries were found!")

while True:
    print("\nMenu:")
    print("1. Add a new diary entry")
    print("2. View existing diary entries")
    print("3. Quit")
    
    choice = input("Please choose the option that you want: ")
    
    if choice == "1":
        add_entries()
    elif choice == "2":
        view_entries()
    elif choice == "3":
        print("You have chosen to Quit, Goodbye!")
        break
    else:
        print("You have chosen a wrong number. Try again!")
