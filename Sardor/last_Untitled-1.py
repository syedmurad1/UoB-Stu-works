import datetime
student_id = input("Enter your student ID: ")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
mark1, mark2, mark3, mark4 = map(float, input("Enter your marks for four subjects separated by spaces: ").split())
marks = [mark1, mark2, mark3, mark4]
current_hour = datetime.datetime.now().hour
if current_hour < 12:
    time = "Good morning!"
elif 12 <= current_hour < 18:
    time = "Good afternoon!"
else:
    time = "Good evening!"
print(time, first_name,last_name)

average_mark = sum(marks) / 4  #I would have also used "len(marks)"" instead of number "4" here, but the questions says there are exactly 4 marks, so no need for it
print("Your average mark is:", average_mark)

highest_mark = marks[0]

if mark2 > highest_mark:
    highest_mark = mark2
if mark3 > highest_mark:
    highest_mark = mark3
if mark4 > highest_mark:
    highest_mark = mark4

marks.remove(highest_mark) #after finding the highest mark, I am not taking it into consideration when finding the lowest mark.

lowest_mark = marks[0]   # starting to find the lowest mark in the exam with conditions
if marks[1] < lowest_mark:
    lowest_mark = marks[1]
if marks[2] < lowest_mark:
    lowest_mark = marks[2]
print("Your highest mark is:", highest_mark)
print("Your lowest mark is:", lowest_mark)

difference = highest_mark - lowest_mark
print("The difference between the highest and lowest marks is:", difference)

if average_mark >= 60:
    average_result = "Pass"
else:
    average_result = "Fail"

if 70 <= average_mark < 80:
    print("Well done!")
if 80 <= average_mark :
    print("Excellent")