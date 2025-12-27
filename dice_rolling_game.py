#ask: roll the dice
# if users enters y
#generate two random numbers
#print them
#if users enter n
#thank you them
#if the user input anything else
#Terminate
#else 



import random

while True:
    choice=input('roll the dice? (y/n): ').lower()
    if choice=='y':
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        print(f'({dice1},{dice2})')
    elif choice== 'n':
        print("Thank you")
    else:
        print("Invalid")
    

