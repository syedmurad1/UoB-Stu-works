#Question2
#A list of integers:
'''
numbers = [3,7,2,9,4,1,8]

numbers.append(5) #Append 5 to the list
numbers.remove(9) #Remove 9 from the list
numbers.sort() #Sort the list in ascending order
numbers.reverse() #Reverse the list
numbers.insert(2,6) #Insert number 6 in the index 2
print(numbers)
print(numbers.index(4)) #print the index of number 4 in the list
'''

#Question3
#3. The following tuple of mixed data types: 

my_tuple = (15, "Python", 3.14, True, 42, False)

print(my_tuple[1]) #I. Print the index of the string "Python".
print(my_tuple.count(True)) #II. Count how many times the value True appears in the tuple.
print(my_tuple[1:5]) #III. Prints the elements from index 1 to index 4.

#Question4
#4. Create a python dictionary representing the marks of students (at least 15 students) in a test.
dictionary_student_marks = {"student_1":40, "student_2":60, "student_3":64, "student_4":76, "student_5":56, "student_6":97, "student_7":76, "student_8":84, "student_9":49, "student_10":54, "student_11":98, "student_12":57, "student_13":67, "student_14":78, "student_15":86}

dictionary_student_marks["Frank"] = 60 #I. Add a new student "Frank" with a mark of 60.

print(dictionary_student_marks) #II. Print all student names and their corresponding marks.

