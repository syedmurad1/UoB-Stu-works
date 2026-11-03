#dictionaries exercise

marks = {        #dictionary that represent the marks of students in a test
    "Amalia": 85,
    "Alice": 78,
    "Ben": 65,
    "Clara": 92,
    "David": 70,
    "Emma": 88,
    "George": 54,
    "Hannah": 81,
    "Isaac": 76,
    "Julia": 95,
    "Kevin": 62,
    "Lily": 89,
    "Maria": 73,
    "Noah": 67,
    "Olivia": 90
}
marks["Frank"] = 60     #adding a new student with mark 60
for name, mark in marks.items(): 
    print(name, mark)
