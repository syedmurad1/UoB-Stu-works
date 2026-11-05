# 9. Write a program to take two numbers as input from a user and generate a random number 
# between those two numbers.

import random

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

random_number = random.randint(num1, num2)

print("Random number:", random_number)