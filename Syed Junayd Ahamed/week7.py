#1.
a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)

#2.
x = 10
print(x)

x = 10
x += 5
print(x)

x = 10
x -= 5
print(x)

x = 10
x *= 5
print(x)

x = 10
x /= 5
print(x)  

x = 10
x %= 3
print(x) 

x = 10
x //= 3
print(x) 

x = 10
x &= 3
print(x)

x = 10
x |= 3
print(x)

x = 10
x ^= 3
print(x)

x = 10
x >>= 1
print(x)

x = 10
x <<= 1
print(x)

print(x := 10)

#3.
a = 10
b = 5
print("Equal to:", a == b)
print("Not equal to:", a != b)
print("Greater than:", a > b)
print("Less than:", a < b)
print("Greater than or equal to:", a >= b)
print("Less than or equal to:", a <= b)

#4.
AND: Both conditions must be True.
OR: At least one condition must be True.
NOT: Reverses True to False and False to True.

a = 10
b = 5
print(a > 5 and b < 10)
print(a < 5 or b < 10)
print(not(a > 5))

#5.
is: Returns True if both variables refer to the same object.
is not: Returns True if both variables refer to different objects.

a = [10, 20, 30]
b = a
c = [10, 20, 30]
print(a is b)
print(a is not c)

#6.
in: Checks if a value exists.
not in: Checks if a value does not exist.

numbers = [1, 3, 5, 7, 9]
print(5 in numbers)
print(10 not in numbers)

#7.
x = 10
y = 3
print(x & y)

x = 10
y = 3
print(x | y) 

x = 10
y = 3

x = 10
y = 3
print(x ^ y) 

x = 10
print(~x)

x = 10
print(x << 2)

x = 10
print(x >> 2)

#8.
a = 10
a += 5
a -= 3
a *= 2
a //= 4
print(a)

#9.
x = 7
y = 12
print(x > y)   # Output: False
print(x <= y)  # Output: True
print(x < y and x != y)  # Output: True
print(x > y or y > 10)   # Output: True

#10.
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)       # Output: True
print(10 not in my_list)  # Output: True

a = [1, 2]
b = [1, 2]
print(a is b)  # Output: False
print(a == b)  # Output: True
