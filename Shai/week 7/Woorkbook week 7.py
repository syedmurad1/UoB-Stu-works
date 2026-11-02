#1.
print("My", "name", "Is", "King", sep="$$")

#2.
name1, name2, name3 = input("Enter three names: ").split()
print(f"Name1: {name1}")
print(f"Name2: {name2}")
print(f"Name3: {name3}")

#3.
float_number = float(5.26459884)
print(round(float_number, 2))

#4.
year = 2023
quantity = 3
price = 450
print(f"I have bought {quantity} footballs for {float(price):.2f}£, in the year {year}.")

#5.
sentence_1 = "I have bought 3 footballs for 450.00£, in the year 2023."
words = sentence_1.split()
print(words[0])

#6.
print(len("I have bought 3 footballs"))

#7.
import datetime
today = datetime.date.today()
print(today)

#8.
import random
random_number = random.randint(1, 100)
print(random_number)

#9.
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
lowest = min(number1, number2)
highest = max(number1, number2)
random_number = random.randint(int(lowest), int(highest))
print(random_number)

#10.
num1 = float(input("Enter the first number to add: "))
num2 = float(input("Enter the second number to add: "))
print(f"The sum of {num1} and {num2} is: {num1 + num2}")
