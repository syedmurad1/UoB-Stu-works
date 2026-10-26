#Local
def calculate():
    x = 10          
    print(x)          

calculate()
# print(x) 
#Global
count = 5                 

def show():
    print(count)          

def increase():
    global count
    count += 1             

show()
increase()
print(count)               