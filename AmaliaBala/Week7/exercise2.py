"""
Expected Output:
Enter three Names: Ali Syed Tom
#Name1: Ali
Name2: Syed
Name3: Tom
"""
name1, name2, name3 = input("Enter 3 names: ").split() #takes 3 names into a single input function
print(f"Name1: {name1.upper()}")
print(f"Name2: {name2.upper()}")

print(f"Name3: {name3.upper()}")
