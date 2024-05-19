print("Welcome to the Prime Number Checker!")

try:
    askUser = int(input("Please enter a whole number: "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

# Check if the number is less than 2
if askUser < 2:
    print(f"The number {askUser} is not a prime number.")
else:
    # Assume the number is prime initially
    is_prime = True

    # Check if any number from 2 up to the square root of the number can divide it without leaving a remainder
    for i in range(2, int(askUser ** 0.5) + 1):
        if askUser % i == 0:
            is_prime = False
            break

    # Print the result
    if is_prime:
        print(f"The number {askUser} is a prime number.")
    else:
        print(f"The number {askUser} is not a prime number.")
    
