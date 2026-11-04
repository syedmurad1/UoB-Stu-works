#student number 2965286, jq26920@bristol.ac.uk



print("My","Name","Is","King",sep="$$")
namelist={}
namelist = input("Write three names: ").split()
print("Name1: ",namelist[0])
print("Name2: ",namelist[1])
print("Name3: ",namelist[2])

number=float(5.26459884)
print(f"{number:.2f}")

year=2023
quantity=3
price=float(450)

print(f"I have bought {quantity} footballs for {price:.2f}£, in the year {year}")

sentence ="I have bought 3 footballs for 450.00£, in the year 2023"
print(sentence[0])

sentence2 = "I have bought 3 footballs."
print(len(sentence2))

from datetime import date
today = date.today()
print(today)

import random
number = random.randint(1,100)
print(number)

import random
num1, num2= map(int, input("insert two random numbers").split())
numero = random.randint(num1,num2)
print(numero)

numb1, numb2=map(int, input("Choose two numbers: ").split())
add=numb1+numb2
print(add)