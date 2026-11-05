Group Presentation 

#2.
numbers = [3, 7, 2, 9, 4, 1, 8]
numbers.append(5)
numbers.remove(9)
numbers.sort()
numbers.reverse()
numbers.insert(2, 6)
print("Index of 4:", numbers.index(4))
print("Final list:", numbers)

#3.
my_tuple = (15, "Python", 3.14, True, 42, False)
print("Index of Python:", my_tuple.index("Python"))
print("Count of True:", my_tuple.count(True))
print("Elements from index 1 to 4:", my_tuple[1:5])

#4.
students = {

    "Aliya": 85,

    "Ben": 72,

    "Charles": 90,

    "Daniel": 65,

    "Emma": 88,

    "George": 76,

    "Hannah": 95,

    "Isa": 81,

    "Junayd": 99,

    "Kate": 92,

    "Leo": 78,

    "Mohammed": 84,

    "Nuh": 73,

    "Olivia": 89,

    "Peter": 67

}
students["Frank"] = 60
for name, mark in students.items():

    print(name, ":", mark)

#5.
Mutable: A mutable object is an object whose value can be changed after it has been created.
example: 
numbers = [10, 20, 30]
numbers[0] = 50

print(numbers)

output: [50, 20, 30]

Immutable: An immutable object is an object whose value cannot be changed after it has been created.
Examples: Integers, strings, tuples and floats.

example:
name = "Python"
name = "Programming"
print(name)

output: Programming
The original string cannot be modified. Instead, Python creates a new string and assigns it to the variable.

#6.
Local Variables: A local variable is a variable that is created inside a function and can only be accessed within that function.
example:
def greet():
    name = "Junayd"
    print("Hello", name)
greet()

output: Hello Junayd
The variable name is created inside the function greet(). Therefore, it is a local variable and cannot normally be accessed outside that function.

Global Variables: A global variable is a variable that is created outside a function and can be accessed throughout the program, including inside functions.
example:
name = "Junayd"

def greet():

    print("Hello", name)

greet()
print(name)

output: Hello Junayd
        Junayd
The variable name is created outside the function, so it is a global variable. Both the function and the main program can access it.

  
