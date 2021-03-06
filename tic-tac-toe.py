import random


def create_field():
    board = [['.', '.', '.'],
             ['.', '.', '.'],
             ['.', '.', '.']]
    return board


def draw_field(board):
    for x in board:
        print(x[0], x[1], x[2])


def player_move(token, board):
    while True:
        print('Ходит ', token)
        line = input('Введите строку: ')
        column = input('Введите столбец; ')
        
        try:
            line = int(line)
            column = int(column)
        except:
            print('Вводите только цифры')
            continue
        
        if not(1 <= line <= 3) or not(1 <= column <= 3):
            print('Нельзя выбрать эту клетку. Вводите числа от 1 до 3')
            continue
        
        if board[line - 1][column - 1] == '.':
            board[line - 1][column - 1] = token
            return board
        else:
            print('Эта клетка уже занята')
            continue


def is_win(board):
    win = [[board[0][0], board[0][1], board[0][2]],
           [board[1][0], board[1][1], board[1][2]],
           [board[2][0], board[2][1], board[2][2]],
           [board[0][0], board[1][0], board[2][0]],
           [board[0][1], board[1][1], board[2][1]],
           [board[0][2], board[1][2], board[2][2]],
           [board[0][0], board[1][1], board[2][2]],
           [board[0][2], board[1][1], board[2][0]]]
    
    for each in win:
        if (each[0] != '.') and (each[0] == each[1] == each[2]):
            return each[0]
    return False

        
def main(board):
    i = random.randrange(0, 2)
    if i == 0:
        sym = 'O'
    else:
        sym = 'X'

    draw_field(board)
    count = 0

    while True:
        player_move(sym, board)
        draw_field(board)
        count += 1

        if count > 4:
            victory = is_win(board)
            if victory:
                print(victory + ' победил!')
                break
        
        if count == 9:
            print('Ничья!')
            break

        if sym == 'O':
            sym = 'X'
        else:
            sym = 'O'

while True:
    string = input('Чтобы начать игру нажмите Enter')

    if not string:
        field = create_field()
        main(field)
    else:
        break
