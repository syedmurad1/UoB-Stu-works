numbers = [3, 7, 2, 9, 4, 1, 8]

#1
numbers.append(5)


#2
numbers.remove(9)

#3
numbers.sort()


#4
numbers.reverse()


    #5
numbers.insert(2, 6)


#6
print(numbers.index(4))
print(numbers)




# 3. The following tuple of mixed data types: my_tuple = (15, "Python", 3.14, True, 42, False)
# I. Print the index of the string "Python".
# II. Count how many times the value True appears in the tuple.
# III. Prints the elements from index 1 to index 4.


my_tuple = (15, "Python", 3.14, True, 42, False)
print(my_tuple.index("Python"))
print(my_tuple.count(True))
print(my_tuple[1:5])


# 4. Create a python dictionary representing the marks of students (at least 15 students) in a test.
# I. Add a new student "Frank" with a mark of 60.
# II. Print all student names and their corresponding marks.

marks = {"Alice": 72,"Ben": 65,"Chloe": 88,"Daniel": 54,"Emma": 91,"George": 47,"Hannah": 79,"Isaac": 63,"Jack": 58,"Katie": 84,"Liam": 70,"Mia": 66,"Noah": 95,"Olivia": 81,"Ryan": 59}
marks["Frank"] = 60
print(marks)


# Question 5
# Mutable means it can be changed after it is made, e.g. list and dictionary.
# Immutable means it cannot be changed after it is made, e.g. tuple and string.

fruits = ["apple", "banana"]
fruits[0] = "mango"
print(fruits)    # ['mango', 'banana'] so the list changed

colours = ("red", "blue")
# colours[0] = "green"    # Error, because a tuple cannot be changed
print(colours)

# Question 6
# A global variable is made outside a function, so it can be used anywhere in the file.
# A local variable is made inside a function, so it only exists inside that function.

school = "University of Bristol"    # global

def say_hello():
    student = "Jin"    # local
    print(student, "studies at", school)

say_hello()    # Jin studies at University of Bristol
# print(student)    # Error, because student only exists inside say_hello()







