'''
Docstring for snake gun game
for snake 1,
for water -1,
for gun 0
'''
import random as rand

computer=rand.choice([1,-1,0])
u=int(input("Enter 1 for snake, -1 for water and 0 for gun: "))

reverseDict={1:"snake", -1:"water", 0:"gun"}

print(f"you chose {reverseDict[u]} \ncomputer choice {reverseDict[computer]}")


if u==computer:
    print("draw")
else:
    if u==1 and computer==-1:
        print("you win")
    elif u==-1 and computer==0:
        print("you win")
    elif u==0 and computer==1:
        print("you win")
    else:
        print("you lose")    