#LANGE00052 written Code A
#This program greets the user by the time of day then calculates
#the average highest lowest and difference of four test marks,
#and finally reports a pass/fail result with extra messages
#Extra features: check each mark is in range 0-100,and track 
#whichtest the highest/lowest mark came from.
from datetime import datetime  #used to get the current system time
# input section
student_id = input("Enter your student ID :")
first_name = input("Enter your first name :")
last_name = input("Enter your last name :")
# Read the four test marks and convert them from strings to integers
mark1 = int(input("Enter test mark1:"))
mark2 = int(input("Enter test mark2:"))
mark3 = int(input("Enter test mark3:"))
mark4 = int(input("Enter test mark4:")) 
# Check if the marks in the range
if mark1<0 or mark1>100:
    print("This mark is out of range (0-100) program end.")
    exit()
if mark2<0 or mark2>100:
    print("This mark is out of range (0-100) program end.")
    exit()
if mark3<0 or mark3>100:
    print("This mark is out of range (0-100) program end.")
    exit()
if mark4<0 or mark4>100:
    print("This mark is out of range (0-100) program end.")
    exit()
# Greeting based on the current time
hour = datetime.now().hour # current hour
if hour < 12:
    greeting = "good morning"
elif hour < 18:
    greeting = "good afternoon"
else:
    greeting = "good evening"
print(greeting +", " + first_name + " "+last_name+"!")
# average
average = (mark1+mark2+mark3+mark4) / 4
print("Average=",average)
# highest and lowest( which test is )
highest = mark1
highest_test = 1
lowest = mark1
lowest_test = 1
if mark2 > highest:
    highest = mark2
    highest_test = 2
if mark3 > highest:
    highest = mark3
    highest_test = 3
if mark4 > highest:
    highest = mark4
    highest_test = 4

if mark2 < lowest:
    lowest = mark2
    lowest_test = 2
if mark3 < lowest:
    lowest = mark3
    lowest_test = 3
if mark4 < lowest:
    lowest = mark4
    lowest_test = 4
print("Highest:",highest,"(test", highest_test,")")
print("Lowest:",lowest,"(test" ,lowest_test,")")
# Difference
difference = highest - lowest
print("Difference:",difference)
# Pass or fail
if average>=60:
    print("pass")
else:
    print("fail")
if average>=80:
    print("Excellent")
elif average>=70:
    print("Well done")