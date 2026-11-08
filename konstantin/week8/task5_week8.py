# is
a = [0, 1, 1, 2, 3, 5]
b = a
if b is a:
    print("Y")
else:
    print("N")  # Y

# is not
a = [0, 1, 1, 2, 3, 5]
b = [0, 1, 1, 2, 3, 5]
if b is not a:
    print("Y")
else:
    print("N")  # Y
