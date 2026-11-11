#checks whether a given number is positive, negative, or zero.

num = input("Enter the number: ")
if int(num) > 0:
    print("The number is a positive number.")
elif int(num) < 0:
    print("The number is a negative number.")
else:
    print("The number is zero.")


#Write a program that classifies a student's grade based on the following criteria
#70-100: 1st, 60-69:2.1, 50-59: 2.2, 40-49: 3rd, 0-39:F

grade = input("Please enter the student grade: ")
if float(grade) >= 70 and float(grade) < 100:
    print("1st grade")
elif  float(grade) >= 60:
    print("2.1 grade")
elif  float(grade) >= 50:
    print("2.2 grade")
elif  float(grade) >= 40:
    print("3rd grade")
else:
    print("F grade")


#Write a program that checks if a given year is a leap year.
year = input("Please enter the year: ")
if int(year)%4 == 0:
   if int(year)%100 !=0 :
    if int(year)%900 != 200 or int(year)%900 != 600:
         print("This year is a leap year!")
    else:
        print("This year is not a leap year!")
   else:
    print("This year is not a leap year!")
else:
    print("This year is not a leap year!")




#Write a program that checks if a person is  eligible to vote. A person can vote if their age is 18 or older.
age = input("Please enter your age: ")
if int(age) >= 18:
    print("The person is eligible to vote")
else:
    print("The person is not eligible to vote")


#5 write a program to check if a given number is divisible by both 5 and 11
num = input("Please enter the number: ")
if float(num)%5 == 0 and float(num)%11 == 0 :
   print("The number can divide by 5 and 11")
else:
   print("The number cannot divide by 5 or 11 or both")


#6 Write a program to calculate an electricity bill based on the number of units consumed:
#For the first 100 units: 0.50 pounds per unit
#For the next 100 units (101-200): 0.75 pounds per unit
#For the next 100 units (201-300): 1.20 pounds per unit
#For any units above 300: 1.50 per unit
unit = int(input("Please enter the units: "))
if unit > 100:
    if unit<=200:
        bill = (100*0.50) + (unit-100)*0.75
        print("An electricity bill is " ,bill," pounds per units")
    elif unit<=300:
        bill = (100*0.50) + (100*0.75) + (unit-200)*1.20
        print("An electricity bill is " ,bill," pounds per units")
    elif unit>300:
        bill = (100*0.50) + (100*0.75) + (100*1.20) + (unit-300)*1.50
        print("An electricity bill is " ,bill," pounds per units")
else:
    bill = unit*0.5
    print("An electricity bill is " ,bill," pounds per units")