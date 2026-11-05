#1. Use the print () function to display the $$ separator between each string.
print("My", "name", "Is", "King", sep="$$")

#2. Write a program to take three names as input from a user in the single input() function call and Expected Output:
#Enter three Names: Ali Syed Tom
#Name1: Ali
#Name2: Syed
#Name3: Tom
name1, name2, name3 = input("Enter three names: ").split()
print(f"Name1: {name1}")
print(f"Name2: {name2}")
print(f"Name3: {name3}")

#3. Display float number (5.26459884) with 2 decimal places using print ()
float_number = float(5.26459884)
print(round(float_number, 2))

#4. Write a program to use f-strings method to format the following three variables as per the 
#expected output
#year = 2023
#quantity = 3
#price = 450
#Expected Output:
#I have bought 3 footballs for 450.00 £, in the year 2023
year = 2023
quantity = 3
price = 450
print(f"I have bought {quantity} footballs for {float(price):.2f}£, in the year {year}.")

#5. Get the first character from the following sentence: I have bought 3 footballs for 450.00 £, in the year 2023
sentence_1 = "I have bought 3 footballs for 450.00£, in the year 2023."
words = sentence_1.split()
print(words[0])

#6. Get the length of the following sentence: I have bought 3 footballs.
print(len("I have bought 3 footballs"))

#7. Get the current date using today (). 
import datetime
today = datetime.date.today()
print(today)

#8. Generate a random number between 1 and 100.
import random
random_number = random.randint(1, 100)
print(random_number)

#9. Write a program to take two numbers as input from a user and generate a random number between those two numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
lowest = min(number1, number2)
highest = max(number1, number2)
random_number = random.randint(int(lowest), int(highest))
print(random_number)

#10. Write a program to take two numbers as input from a user and program should add those two numbers and display
num1 = float(input("Enter the first number to add: "))
num2 = float(input("Enter the second number to add: "))
print(f"The sum of {num1} and {num2} is: {num1 + num2}")
