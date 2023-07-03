## Rock, Paper and scissors game!

import random
r=''
n=0
print("Enter your choice {Rock,Paper,Scissors}\n")
for j in range(3):
    a=input("Enter your choice: ")
    b=random.randint(1,3)
    if b==1:
        r="rock"
        if a=="scissors":
            print("you loose")
        elif a=="paper":
            print("You win")
            n+=1
        else:
            print("It's a tie")
    elif b==2:
        r="paper"
        if a=="scissors":
            print("you win")
            n+=1
        elif a=="rock":
            print("You loose")
        else:
            print("It's a tie")

    elif b==3:
        r="scissors"
        if a=="rock":
            print("You win")
            n+=1
            
        elif a=="paper":
            print("You loose")
        else:
            print("It's a tie")
if n>2:
    print("victory")
elif n==2:
    print("tie, play again")
else:
    print("\ncomputer wins")
        
