from termcolor import colored

x='x'
o='o'

board=[
    [' ',' ',' '],
    [' ', ' ',' '],
    [' ',' ',' ']
]

def cell(mark):
    color ='red' if mark=='x' else 'green'
    return colored(mark,color)

def print_board(board):
    line='---+---+---'
    print(line)
    for row in board:
        print(f'{cell(row[0])} | {cell(row[1])} |{cell(row[2])}')
        print(line)

def check_winner(board):
    for rows in board:
        if rows[0]==rows[1]==rows[2] !=' ':
            return True
    
    for column in range(3):
        if board[0][column]==board==[1][column]==board[2][column] != ' ':
            return True
    
    if board[0][0]==board[1][1]==board[2][2] != ' ' or \
       board[0][2]==board[1][1]==board[2][0] != ' ':
        return True
    
    return False


def is_full(board):
    for row in board:
        if ' ' in row:
            return False
        
    return True

def get_position(prompt):
    while True:
        try:
            postion= int(input(prompt))
            if postion<0 or postion>2:
                raise ValueError
            return postion
        except ValueError:
            print("invalid output")

def get_move(current_player):
    print(f"player {current_player}'s turn")
    while True:
        row=get_position('enter(0-2):')
        column=get_position('enter(0-2):')
        if board[row][column]==' ':
            board[row][column]=current_player
            break
        print("THIS PLACE IS TAKEN")

def main():
    print_board(board)
    current_player=x 
    while True:
        get_move(current_player)
        
        print_board(board)
        if check_winner(board):
            print(f"{current_player} is winner")
            break
        
        if is_full(board):
            print('board is full')
            break

        current_player=o if current_player==x else x


if __name__=='__main__':
    main()


    
    
    
   




    
        
             
       




