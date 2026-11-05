#print favorite game
'''
favgame = input("Please enter your favorite game: ")
print("Your favorite game is " + favgame)
print(f"Your favorite game is {favgame}") 
#This can be use to show that u know
'''

#First task Use the print () function to display the $$ separator between each string. Expected Output: My$$Name$$Is$$King
print("My","Name","Is","King",sep="$$")


#second task Write a program to take three names as input from a user in the single input() function call and 
#Expected Output:Enter three Names: Ali Syed Tom
#Name1: Ali
#Name2: Syed
#Name3: Tom
name1,name2,name3 = input("Please enter three name: ").split()
print("\nName1:"+ name1,"\nName2:"+ name2,"\nName3:"+ name3)

'''
name1,name2,name3 = input("Enter three names: ").split()
print("Name1:",name1)
print("Name2:",name2)
print("Name3:",name3)
'''

#third task Display float number (5.26459884) with 2 decimal places using print ().
num = float(5.26459884)
print('%.2f' %(num))

#fourth task Write a program to use f-strings method to format the following three variables as per the expected output 
#Expected Output: I have bought 3 footballs for 450.00 £, in the year 2023. 
year = 2023 
quantity = 3 
price = 450 

print(f"I have bought {quantity} footballs for {'%.2f' %(price)} £, in the year {year}")

#fifth task Get the first character from the following sentence: I have bought 3 footballs for 450.00 £, in the year 2023. 
sentence = "I have bought 3 footballs for 450.00 £, in the year 2023"
print("The first character from the following sentence : " + sentence[0])

#sixth task Get the length of the following sentence: I have bought 3 footballs. 
text = "I have bought 3 footballs"
print("The length of the following text is ",len(text))

#seventh task Get the current date using today (). 
from datetime import date
today = date.today()
print(today)

#eighth task Generate a random number between 1 and 100. 
import random
print(random.randint(1,100))

#ninth task Write a program to take two numbers as input from a user and generate a random number between those two numbers. 
num1,num2 = input("Please enter two numbers: ").split()
import random
print(random.choice([int(num1),int(num2)]))

#tenth task Write a program to take two numbers as input from a user and program should add those two numbers and display.
no1,no2 = input("Please enter two numbers: ").split()
result = int(no1) + int(no2)
print(result)
