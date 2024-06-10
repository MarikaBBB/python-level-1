import csv

def display_welcome():
    print("Welcome to the Personal Preferences Manager!")
    print("You can use this program to enter, update, and view your personal preferences.")
    print("-------------------------------------------------------------")

def display_menu():
    print("\nPersonal Preferences Manager Menu")
    print("1. Enter or update preferences")
    print("2. View current preferences")
    print("3. Exit")

def load_preferences(file_path):
    preferences = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            preferences = list(reader)
    except FileNotFoundError:
        preferences.append(["User ID", "Preferred Language", "Theme Color", "Notification Settings"])
    except IOError:
        print("An error occurred while reading the file.")
    return preferences

def save_preferences(file_path, preferences):
    try:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(preferences)
        print("Preferences saved successfully.")
    except IOError:
        print("An error occurred when writing to the file.")

def enter_or_update_preferences(preferences):
    user_id = input("Enter User ID: ")
    preferred_language = input("Preferred Language: ")
    theme_color = input("Theme Color: ")
    notification_settings = input("Notification Settings (On/Off): ")

    for i, row in enumerate(preferences):
        if row[0] == user_id:
            preferences[i] = [user_id, preferred_language, theme_color, notification_settings]
            break
    else:
        preferences.append([user_id, preferred_language, theme_color, notification_settings])

def view_preferences(preferences):
    if len(preferences) <= 1:
        print("No preferences found.")
        return
    print("\nCurrent Preferences:")
    for row in preferences[1:]:
        print(f"User ID: {row[0]}, Preferred Language: {row[1]}, Theme Color: {row[2]}, Notification Settings: {row[3]}")

def main():
    file_path = "preferences.csv"
    display_welcome()
    preferences = load_preferences(file_path)
    
    while True:
        display_menu()
        choice = int(input("Please enter your choice (1, 2, or 3): "))
        
        if choice == 1:
            enter_or_update_preferences(preferences)
            save_preferences(file_path, preferences)
        elif choice == 2:
            view_preferences(preferences)
        elif choice == 3:
            print("Exiting preferences manager. Thank you!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
