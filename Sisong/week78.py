#name1, name2, name3 = input("Enter three Names:").split()
#print("Name1:"+name1)
#print("Name2:"+name2)
#print("Name3:"+name3)

num = 5.26459884
print("{:.2f}".format(num))

print("My", "Name", "Is", "King", sep="$$")

year = 2023
quantity = 3
price = 450
print(f"I have bought {quantity} footballs for {price:.2f} £, in the year {year}.")

sentence = "I have bought 3 footballs for 450.00 £, in the year 2023."
print(sentence[0])

sentence = "I have bought 3 footballs."
print(len(sentence))

import datetime
today = datetime.date.today()
print(today)

import random
number = random.randint(1, 100)
print(number)

import random
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
number = random.randint(num1, num2)
print("Random number:", number)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
total = num1 + num2
print("Sum:", total)