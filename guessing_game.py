import random

target=random.randint(1,100)

while True:
    userChoice=input("ENter a random number or quit")
    if(userChoice=="quit"):
        break
    
    userChoice=int(userChoice)
    if(userChoice==target):
        print("Success: you won")
    elif(userChoice<target):
        print("wrong, take a bigger number: ")
    else:
        print("Wrong, take a small number :")

print("Game over")




