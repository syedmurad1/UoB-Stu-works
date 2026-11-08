
#1. Provide a python example of following arithmetic operators: Operator + - * / % ** //
x = 5
y = 6
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)
print(x//y)

#2 Provide a python example of following assignment operators: Operator = ,+= ,-= ,*= ,/= ,%= ,//=, **= ,&= ,|= ,^= ,>>= ,<<= ,:=
c = 9
print(c)
c += 3
print(c)
c -= 4
print(c)
c *= 4
print(c)
c /= 6
print(c)
c %= 5
print(c)
c //= 5
print(c)
c **= 6
print(c)
u = 60
u &= 5
print(u)
u |= 5
print(u)
u ^= 5
print(u)
u >>= 5
print (u)
u <<=  5
print(5)

print(c := 5)

#3 Provide a python example of following comparison operators. Operator: ==, !=, >, <, >=, <=
t = 1
r = 3
print(t == r) #F
print(t != r) #T
print(t > r) #F
print(t < r) #T
print(t >= r) #F
print(t <= r) #T

#4 Provide a python example of following logical operators. Operator: and, or, not
t = 1
print(t<4 and t>=1) #T
print(t>=0 or t<2) #T
print(not(t>4 or t<=0)) #T

#5 Provide a python example of following identity operators. Operator: is, is not
s = ["me","you"]
p = ["me","you"]
n = s
print(s is p) #F
print(p is n) #F
print(p is not n) #T

#6 Provide a python example of following membership operators. Operator : in, not in 
b = ["me","you"]
print("me" in b) #T
print("her" in b) #F
print("her" not in b) #T

#7 Provide a python example of following bitwise operators. Operator: &, |, ^, ~, <<, >>
print(12&7)
print(9|10)
print(67^6)
print(~13)
print(9<<7)
print(13>>67)

#8. Assign the value 10 to a variable a. Use arithmetic and assignment operators to: 
#Add 5 to a. Subtract 3 from a. Multiply a by 2. Divide a by 4 (use floor division). Print the result of a.
a = 10
a + 5
a - 3
a * 2
a // 4

#9. Define two variables, x = 7 and y = 12.Use comparison operators to check if: x is greater than y, x is less than or equal to y 
# Combine these comparisons using logical operators to: Check if x is less than y and x is not equal to y, Check if x is greater than y or y is greater than 10. Print the results of each check. 
x = 7
y = 12
print(x >= y) #F
print(x <= y) #T
print(x<y and x is not y) #T
print(x>y or y>10) #T



#10.  Define a list my_list = [1, 2, 3, 4, 5]. Check if: The number 3 is in my_list. The number 10 is not in my_list. 
#Define two variables, a = [1, 2] and b = [1, 2]. Check if: a is b, a == b

my_list = [1, 2, 3, 4, 5]
print(3 in my_list) #T
print(10 not in my_list) #T

a = [1, 2]
b = [1, 2]
print(a is b) #F
print(a == b) #T

