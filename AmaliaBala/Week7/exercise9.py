#Generate a random number between two user-entered numbers

number1 = int(input("Enter the lower number: "))

number2 = int(input("Enter the higher number: "))

print("Random number:", random.randint(number1, number2))
