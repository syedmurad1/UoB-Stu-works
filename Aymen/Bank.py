
is_running=True
Balance=0
while is_running==True:
 def balance():
    print("-------------------------------------------------")
    print(f"     Your current balance is: {Balance}")
    print("-------------------------------------------------")

 def deposit():
    amount=float(input("Please enter the amount you want to deposit: "))
    global Balance
    Balance+=amount
    print("---------------------------------------------------------------------------")
    print(f"You have successfully deposited {amount}. Your new balance is: {Balance}")
    print("---------------------------------------------------------------------------")

 def withdraw():
    amount=float(input("Please enter the amount you want to withdraw: "))
    global Balance
    if amount>Balance:
        print("-------------------------------------------------")
        print("You do not have enough balance to withdraw this amount.")
        print("-------------------------------------------------")
    else:
        Balance-=amount
        print("---------------------------------------------------------------------------")
        print(f"You have successfully withdrawn {amount}. Your new balance is: {Balance}")
        print("---------------------------------------------------------------------------")

 Option=input("Welcome to the Bank! Choose an option: ")
 print("1. Check Balance")
 print("2. Deposit Money")
 print("3. Withdraw Money")
 print("4. Exit") 

 if Option=="1":
    balance()
 elif Option=="2":
    deposit()
 elif Option=="3":
    withdraw()
 elif Option=="4":
    print("Thank you for using our bank services!")
    is_running=False
 else:
    print("Invalid option. Please try again.")