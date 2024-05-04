print("Welcome to the quiz on capital cities of the world")

while True:
  guess = str(input("What is the capital of England?"))
  if guess == "London":
    print(f"Correct! The capital of england is {guess}!")
    break
  else:
    print(f"Incorrect, the capital of england is not {guess}!")
    print("Try again!")