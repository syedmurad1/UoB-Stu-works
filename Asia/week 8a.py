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