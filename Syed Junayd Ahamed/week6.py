#1. 
print("My", "Name", "Is", "King", sep="$$")

#2.
names = input("Enter three Names: ").split()
print("Name1:", names[0])
print("Name2:", names[1])
print("Name3:", names[2])

#3.
number = 5.26459884
print(f"{number:.2f}")

#4.
year = 2023
quantity = 3
price = 450
print(f"I have bought {quantity} footballs for {price:.2f} £, in the year {year}.")

#5.
sentence = "I have bought 3 footballs for 450.00 £, in the year 2023."
print(sentence[0])

#6.
sentence = "I have bought 3 footballs."
print(len(sentence)
      
#7.
import datetime
current_date = datetime.date.today()
print("Current date:", current_date)

#8.
import random
number = random.randint(1, 100)
print("Random number:", number)

#9.
import random
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
random_number = random.randint(num1, num2)
print("Random number:", random_number)

#10.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum = num1 + num2
print("The sum is:", sum)
