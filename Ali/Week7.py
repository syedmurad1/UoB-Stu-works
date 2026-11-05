import random

game = input("Enter your favorite game:")
print(f"Your favorite game is: {game}")

print(random.randint(1, 1231232312312321))

#1. Use the print () function to display the $$ separator between each string.

print("My", "Name", "Is", "King", sep="$$")

#2. Write a program to take three names as input from a user in the single input() function call as per the expected Output...

h1, h2, h3 = input("enter three names:").split()
print(f"name1: {h1}")
print(f"name2: {h2}")
print(f"name3: {h3}")

#3. Display float number (5.26459884) with 2 decimal places using print ().

number = 5.26459884
rounddeci = f"({number:.2f})"
print(rounddeci) 


#4. Write a program to use f-strings method to format the following three variables as per the expected output...

year = 2023
quantity = 3
price = 450

#5. Get the first character from the following sentence: I have bought 3 footballs for 450.00 £, in the year 2023

sentence = (f'I', 'have bought', quantity, 'footballs for', price, 'pounds in the year of', year, '.')
print(sentence)
print(sentence[0])

#6. Get the length of the following sentence: I have bought 3 footballs.

print(len(sentence[0:4]))

#7. Get the current date using today ()

from datetime import date
today = date.today()
print(today)  

#8. . Generate a random number between 1 and 100.

import random
randumb = random.randint(1, 100)
print(randumb)


#9. Write a program to take two numbers as input from a user and generate a random number between those two numbers.
#10. Write a program to take two numbers as input from a user and program should add those two numbers and display.

r1, r2 = input("enter two numbers:").split()
randos = random.randint(int(r1), int(r2))
print(randos)

print(r1+r2)