#phyton quiz game

questions=("1-What is the largerst country in Africa ?",
           "2-Where do you sleep ?",
           "3-Are you a robot ?",
           "4-What color is the moon ?")

options=(("A.Brazil","B.South Africa","C.Algeria","D.Morroco"),
         ("A.Home","B.School","C.Street","D.Stadium"),
         ("A.Maybe","B.Yes","C.No","D.I dont know"),
         ("A.Yellow","B.Blue","C.White","D.Green"))

answers=("C", "A", "C", "C")

guesses=[]
question_num=0
score=0



for question in questions :
    print(question)
    print("--------------------")
    for option in options[question_num]:
        print(option)
    guess=input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess ==answers[question_num]:
       score+=1
       print("Correct!")
    else:
       print("Incorrect")    
       print(f"The answer '{answers[question_num]}' is the correct answer")
    question_num+=1

if score== 4 :
    print("YOU ARE SO SMART,YOU GOT EVERYTHING CORRECT!!")
else :
    print(f"Your score is {score},Thank you for playing.") 
 

    

