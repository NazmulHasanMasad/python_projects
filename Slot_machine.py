import random
def get_starting_balance():
    while True:
        try:
            balance=int(input(" enter your starting balance "))
            if balance <=0:
                print("Balance must be poitive number")
            else:
                return balance
        except ValueError:
            print("please enter a valid number")

def get_bet_amount(balance):
    while True:
        try:
            bet= int(input("enter the anount of bet"))
            if bet >balance or bet <=0:
                print("invalid amount of bet")
            else:
                return bet
        except ValueError:
            print("Enter a valid amount of bet")
         
def spin_reels():
    symbols = ['🍒', '🍋', '🔔', '⭐️', '🍉', '😎']
    return [random.choice(symbols) for _ in range(3)]

def display_reels(reels):
    print(f'{reels[0]} | {reels[1]} | {reels[2]}' )


def calculate_payout(reels, bet):
    if reels[0]==reels[1]==reels[2]:
        return bet*10
    if reels[0]==reels[1] or reels[0]==reels[2] or reels[1]==reels[2]:
        return bet*2
    return 0




def main():
    balance=get_starting_balance()


    print("welcome to the game")
    print(f'you start your game with balance of ${balance}')

    while balance>0:
        print(f'current balance ${balance}')
        bet=get_bet_amount(balance)
        reels=spin_reels()
        display_reels(reels)
        payout=calculate_payout(reels,bet)
        

        if payout>0:
            print(f'you won ${payout}')
        else:
            print("You lost the game")

        balance+=payout-bet
        if balance<0:
            print("You do not have enoughf balance")
            break

        play_again=input('do you want to play again??(y/n)').lower()
        if play_again != 'y':
            print(f'you walk with balamnce {balance}')
            break

if __name__=='__main__':
    main()




    






