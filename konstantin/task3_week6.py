my_tuple = (15, "Python", 3.14, True, 42, False)

# I.
print(my_tuple.index("Python"))

# II.
c = 0
for i in my_tuple:
    if i == "Python":
        c += 1
print("Count of 'Python' in tuple:", c)

# III.
print(tuple(my_tuple[i] for i in range(1, 5)))
