
# #Activity 1
name=input("Please enter your name: ")
print("My", "Name", "Is", name, sep='$$')

# #Activity 2
name1,name2,name3=input("Please enter your names:",).split()
print("Name 1:", name1)
print("Name 2:", name2)
print("Name 3:", name3)

# #Activity 3
print(round(5.26459884, 2))

# #Activity 4
year=2023
quantity=3
price=450
print(f"I have bought {quantity} footballs for {price}£, in the year {year}.")

#Activity 5
Sentence=("I" "have" "bought" "3" "footballs" "for" "450£" "in" "the" "year" "2023")
print(Sentence[0])

#Activity 6
Sentence=("I have bought 3 footballs.")
print(len(Sentence))

#Activity 7
import time
time_now=time.localtime()
print(f"Current time is {time_now.tm_hour}:{time_now.tm_min}:{time_now.tm_sec}")

# #Activity 8
import random
print("Random number between 1 and 100 is:", random.randint(1,100))

# #Activity 9
num01,num02=input("Please enter two numbers: ").split()
print(random.randint(int(num01), int(num02)))

#Activity 10
num1,num2=input("Please enter two numbers: ").split()
def add(num1,num2):
    return float(num1)+float(num2)
print(f"The sum of {num1} and {num2} is {add(num1,num2)}")



