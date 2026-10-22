#2.
print("2.")
numbers = [3, 7, 2, 9, 4, 1, 8]
numbers.append(5) #adds 5 to the end of the list
numbers.remove(9) #removes 9 from the list
print(numbers)
numbers.sort() #sorts the list
print(numbers)
numbers.reverse() #reverses the list
print(numbers)
numbers[2] = 6 #inserts 6 at the index 2
print(numbers)
element = 4
print(numbers.index(element)) #prints the index of 4

#3. 
print("3.")
my_tuple = (15, "Python", 3.14, True, 42, False)
print(my_tuple.index("Python")) #prints the index of "Python"
truecount = my_tuple.count(True) #counts how many time True appears
print(truecount)
print(my_tuple[1:5]) #prints the values fromthe index 1 to 4

#4.
print("4.")
studentMarks = {"tom": 75,
    "syed": 80,
    "goku": 44,
    "zac": 90,
    "ali": 80,
    "majeed": 70,
    "ayush": 20,
    "sardor": 55,
    "dior": 83,
    "shoka": 100,
    "andrei": 93,
    "rayhona": 77,
    "luna": 66,
    "junayd": 80,
    "shai": 90 }
print(studentMarks)