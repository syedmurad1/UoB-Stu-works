import random

game = input("Enter your favorite game:")
print(f"Your favorite game is: {game}")

print(random.randint(1, 1231232312312321))

print("My", "Name", "Is", "King", sep="$$")

h1, h2, h3 = input("enter three names:").split()
print(f"name1: {h1}")
print(f"name2: {h2}")
print(f"name3: {h3}")



number = 5.26459884
rounddeci = f"({number:.2f})"
print(rounddeci) 


year = 2023
quantity = 3
price = 450
sentence = (f'I', 'have bought', quantity, 'footballs for', price, 'pounds in the year of', year, '.')
print(sentence)
print(sentence[0])
print(len(sentence[0:4]))

from datetime import date
today = date.today()
print(today)  

import random
randumb = random.randint(1, 100)
print(randumb)

r1, r2 = input("enter two numbers:").split()
randos = random.randint(int(r1), int(r2))
print(randos)

print(r1+r2)