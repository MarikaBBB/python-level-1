conversion_choice = input("1)lb to kg, 2)kg to lb...")

if conversion_choice == "1":
    pounds = float(input("How many lb do you want to convert?"))
    kilograms = pounds / 2.204
    print("This is", kilograms, "kg")
elif conversion_choice == "2":
    kilograms = float(input("How many kg do you want to convert?"))
    pounds = kilograms * 2.204
    print("This is", pounds, "lb")
else:
    print("Invalid choice")
