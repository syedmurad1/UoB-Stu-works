#Menu 

menu={"Potato" :2.99,
      "Chips" : 1.99,
      "Chicken" : 5.99,
      "Meat" : 9.99}

cart=[]
price=0


print("-------Menu-------" )
for key, value in menu.items() :
    print(f"{key}:${value:.2f}")

while True : 
    food=input("select an item(select q to quit) ")
    if food=="q".lower():
      break
    elif menu.get(food) is not None :
       cart.append(food)     

print("------Your Order------")
for food in cart:
   price+=menu.get(food)   
   print(food, end=" ")   

print("")
print(f"Your total is {price}")    