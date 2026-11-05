
# Task 1
#f string exercise

favgame = input("please enter the name of your favourite game: ")
print("Your favourite game is: " + favgame)
print(f"Your favourite game is: {favgame}") #f string

#1. Use the print () function to display the $$ separator between each string.
#Expected Output:
#My$$Name$$Is$$Kin

print("My", "Name", "Is", "King", sep="$$")

#2. Write a program to take three names as input from a user in the single input() function call and 
#Expected Output:
#Enter three Names: Ali Syed Tom
#Name1: Ali
#Name2: Syed
#Name3: Tom

name1,name2,name3 = input("Enter three names: ").split( )
print("Name1:",name1)
print("Name2:",name2)
print("Name3:",name3)

#3. Display float number (5.26459884) with 2 decimal places using print ().

x = 5.26459884
print(f"{x:.2f}")

#4. Write a program to use f-strings method to format the following three variables as per the 
#expected output
#year = 2023
#quantity = 3
#price = 450
#Expected Output:
#I have bought 3 footballs for 450.00 £, in the year 202

year = 2023
quantity = 3
price = 450

print(f"I have bought {quantity} footballs for {price:.2f} £, in the year {year}." )

#5. Get the first character from the following sentence: I have bought 3 footballs for 450.00 £, in the 
#year 2023.

sentence = "I have bought 3 footballs for 450.00 £, in the year 2023."
    
first character = sentence[0]
print(first character)

# 6. Get the length of the following sentence: I have bought 3 footballs.

sentence = "I have bought 3 footballs."
sentence length = len(sentence)
print(sentence length)

# 7. Get the current date using today (). 

from datetime import date
current date = date.today()
print(current date)

#8.Generate a random number between 1 and 100

Import random
random nnumber = random.randint(1, 100)
print(random number)

#9. Write a program to take two numbers as input from a user and generate a random number between those two numbers
