import random
Rock ='r'
Paper='p'
Scissors= 's'
emojis={Rock: '🪨', Scissors: '✂️', Paper:'📄' }
choices =tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice=input('Rock,paper, scissors? (r/p/s)').lower()
        if user_choice in choices:
            return user_choice 
        else:
            return "Invalid choice"


def display_choice(user_choice, computer_choice):
    print(f'your choice {emojis[user_choice]}')
    print(f'computer choice{emojis[computer_choice]}')


def determine_winner(user_choice, computer_choice):
    if user_choice==computer_choice:
        print("tie")
    elif(
        (user_choice==Rock and computer_choice==Scissors) or
        (user_choice==Scissors and computer_choice== Paper) or 
        (user_choice== Paper and computer_choice==Rock)

    ):
        print("you win")
    else:
        print("you lose")



def play():
    while True:
        user_choice=get_user_choice()
        computer_choice= random.choice(choices)

        display_choice(user_choice, computer_choice)
        determine_winner(user_choice,computer_choice)


        should_continue=input('continue? (y/n)').lower()
        if(should_continue=='n'):
            break


play()





