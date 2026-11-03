# 1
print("My", "Name", "is", "King", sep="$$")


# 2
a, b, c = input("Enter three Names: ").split()
print("Name1:", a)
print("Name2:", b)
print("Name3:", c)


# 3
a = 5.26459884
print("%.2f" % a)


# 4
a = 2023
b = 3
c = 450
print(f"I have bought {b} footballs for {c:.2f} £, in the year {a}.")


# 5
a = "I have bought 3 footballs for 450.00 £, in the year 2023."
print(a[0])


# 6
a = "I have bought 3 footballs."
print(len(a))


# 7
from datetime import date
print(date.today())


# 8
import random
print(random.randint(1, 100))


# 9
import random
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(random.randint(a, b))


# 10
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a + b)