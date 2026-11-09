# 1. Provide a python example of following arithmetic operators:
x = 10
y = 5
print(x + y) # 15
print(x - y) # 5
print(x * y) # 50
print(x / y) # 2.0
print(x % y) # 0
print(x ** y) # 100000
print(x // y) # 2

# 2. Provide a python example of following assignment operators:
x = 10
print(x)     # = 10
x += 2
print(x)            # +=  (x is now 12)
x -= 3
print(x)            # -=  (x is now 9)
x *= 4
print(x)            # *=  (x is now 36)
x /= 2
print(x)            # /=  (x is now 18.0)
x %= 5
print(x)            # %=  (x is now 3.0)
x //= 2
print(x)            # //= (x is now 1.0)
x **= 3
print(x)            # **= (x is now 1.0)
x = int(x)        
x &= 6
print(x)            # &=  (x is now 0)
x |= 1
print(x)            # |=  (x is now 1)
x ^= 2
print(x)            # ^=  (x is now 3)
x >>= 1
print(x)            # >>= (x is now 1)
x <<= 2
print(x)            # <<= (x is now 4)

# 3. Provide a python example of following comparison operators
x = 10
y = 5
print(x == y)  # False
print(x != y)  # True
print(x > y)   # True
print(x < y)   # False
print(x >= y)  # True
print(x <= y)  # False

# 4. Provide a python example of following logical operators
x = True
y = False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False

# 5. Provide a python example of following identity operators
x = 10
y = 10
is_same = x is y  # True
is_not_same = x is not y  # False   

# 6. Provide a python example of following membership operators
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)     # True
print(6 not in my_list) # True

# 7. Provide a python example of following bitwise operators
x = 10 
y = 4
print(x & y)  # 0 
print(x | y)  # 14
print(x ^ y)  # 14 
print(~x)     # -11
print(x << 2) # 40
print(x >> 2) # 2

# 8. Assign the value 10 to a variable a. Use arithmetic and assignment operators to: Add 5 to a. Subtract 3 from a. Multiply a by 2. Divide a by 4 (use floor division). Print the result of a.
a = 10
a += 5
a -= 3
a *= 2
a //= 4
print(a)

# 9. Define two variables, x = 7 and y = 12. Use comparison operators to check if: x is greater than y, x is less than or equal to y. 
# Combine these comparisons using logical operators to: Check if x is less than y and x is not equal to y. Check if x is greater than y or y is greater than 10.
# Print the results of each check.

x = 7
y = 12

print(x > y)  # False
print(x <= y)  # True

print(x < y and x != y)  # True
print(x > y or y > 10)  # True

# 10. Define a list my_list = [1, 2, 3, 4, 5]. Check if:
# The number 3 is in my_list.
# The number 10 is not in my_list.
# Define two variables, a = [1, 2] and b = [1, 2].
# Check if:
# a is b
# a == b

my_list = [1, 2, 3, 4, 5]
print(3 in my_list)     # True
print(10 not in my_list) # True

a = [1, 2]
b = [1, 2]
print(a is b)  # False
print(a == b)  # True