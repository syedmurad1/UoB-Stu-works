#I created these simple game to practise my understanding of the rondom module .

import random

#Choosing the game
print("Please choose a game(1/2).")
print("---------------------")
Game=input("1-Number Guessing game\n"
"          -2-Rock Paper Scicsors" )


#Programing the Number Guessing game
number=random.randint(1,100)
while Game=="1":
    guess=int(input("Guess a number between 1 and 100: "))
    if guess==number:
        print("You guessed it right!")
    elif guess<number:
        print("Hint: The correct number is higher than your guess")
        continue
    elif guess>number:
        print("Hint: The correct number is lower than your guess")    
        continue
    input01=input("Do you want to play again? (y/n) ")
    if input01=="y".lower():
       number=random.randint(1,100)
       continue
    else:
        break

#Programing the Rock Paper Scissors game
options=("Rock","Paper","Scicors")
while Game=="2":
    turn=input("Choose: Rock or Paper or Scicors")
    pc_turn=random.choice(options)
    if (pc_turn=="Rock" and turn=="Scicors") or (pc_turn=="Paper" and turn=="Rock") or (pc_turn=="Scicors" and turn=="Paper") :
     print(f"You lost.because the pc chose {pc_turn}")
    elif (pc_turn=="Rock" and turn=="Paper") or (pc_turn=="Paper" and turn=="Scicors") or (pc_turn=="Scicors" and turn=="Rock") :
     print(f"You won.because the pc chose {pc_turn}")
    elif pc_turn==turn : 
     print(f"It's a tie!. The pc also chose {pc_turn}")
    input02=input("Do you want to play again? (y/n) ")
    if input02=="y".lower():
       continue
    else:
        break
