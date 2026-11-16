#check whether given number is positive, negative or zero

num = input("Type a number: ") #float instead of int
if float(num) > 0:
    print("This is a positive number")
elif float(num) < 0:
    print ("This is a negative number")
else:
    print ("This number is zero")


#classify student's grade based on criterias
#70-100: 1st
#60-69: 2.1
#50-59: 2.2
#40-49: 3rd
#0-39: F

mark = input("Type the student's mark: ") #float instead of int
if float(mark) >= 70:
    print("1st grade")
elif float(mark) >= 60:
    print("2.1 grade")
elif float(mark) >= 50:
    print("2.2 grade")
elif float(mark) >= 40:
    print("3rd grade")
else:
    print("F grade")



#check if given year is leap year
year = input("Type a year: ")
if int(year)%4 == 0:
    print("This is a leap year")
elif int(year)%100 == 0:
    print ("This is a leap year")
elif int(year)%400 == 0:
    print("This is a leap year")
else: 
    print("This is not a leap year")



#check if person is eligible to vote. Can vote if 18 or older

#check if given number is divisible by both 5 and 11




    
#calculate electricity bill based on number of units consumed

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


#check if a given number is divisible by both 5 and 11
num = input("Please enter the number: ")
if float(num)%5 == 0 and float(num)%11 == 0 :
   print("The number can divide by 5 and 11")
else:
   print("The number cannot divide by 5 or 11 or both")


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