# Week 7 exercises
print("My", "name", "is", "King", sep="$$")

print("please input the three names")
name1, name2, name3 = input("Enter the three names: ").split()

print("name1:", name1, "\nname2:", name2, "\nname3:", name3)



year=2023
quantity=3
price=450
print(f"I have bought {quantity} footballs for {price:.2f}$, in the year {year}")


#(5)
sen="I have bought 3 footballs for 450$, in the year 2023" 
print(sen[0])


#(6)
sen1="I have bought 3 footballs"
print(len(sen1))


#(7)
import datetime
print(datetime.datetime.now())


#(8)
import random
print(random.randint(1,100))


#(9)
print("Enter the first number")
a = int(input())
print("Enter the second number")
b = int(input())
print(random.randint(a,b))


#(10)
print("Enter the first number")
c = int(input())
print("Enter the second number")
d = int(input())
print(c+d)


