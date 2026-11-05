number = 5.26459884
print(f"{number:.2f}")          
year,quantity,price = 2023,3,450
print(f"I have bought {quantity} footballs for {price:.2f}￡,in the year {year}")
sentence = "I have bought 3 footballs for 450.00 £, in the year 2023."
print(sentence[0])
print(len("I have bought 3 footballs."))
from datetime import date
today=date.today()
print(today)
import random
number=random.randint(1,100)
print(number)
import random
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
number = random.randint(min(a, b), max(a, b))
print("Random number:", number)
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
total = a + b
print("Sum:", total)
