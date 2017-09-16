import random


field = [['.','.','.'],
         ['.','.','.'],
         ['.','.','.']]


def drawField(board):
    for x in board:
        print(x[0], x[1], x[2])


def playerMove(token, board):
    correct = False
    while not correct:
        print('Ходит' , token)
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
            correct = true
        else:
            print('Эта клетка уже занята')
            continue


def isWin(board):
    win = [[board[0][0], board[0][1], board[0][2]],
           [board[1][0], board[1][1], board[1][2]],
           [board[2][0], board[2][1], board[2][2]],
           [board[0][0], board[1][0], board[2][0]],
           [board[0][1], board[1][1], board[2][1]],
           [board[0][2], board[1][2], board[2][2]],
           [board[0][0], board[1][1], board[2][2]],
           [board[0][2], board[1][1], board[2][0]]]
    
    for each in win:
       if (each[0] != '.') and each[0] == each[1] == each[2]:
           return each[0]
    return False

        
def main(board):
    i = random.randrange(0, 2)
    if i == 0:
        sym = 'O'
    else:
        sym = 'X'

    drawField(board)
    count = 0

    win = False
    while not win:
        playerMove(sym, board)
        drawField(board)
        count += 1

        if count > 4:
            victory = isWin(board)
            if victory:
                print(victory + ' победил!')
                win = True
                break
        
        if count == 9:
            print('Ничья!')
            break

        if sym == 'O':
            sym = 'X'
        else:
            sym = 'O'

while True:
    isPlay = input('Чтобы начать игру нажмите Enter')
    if not isPlay:
        main(field)
    else:
        break
    for x in field:
        x[0] = '.'; x[1] = '.'; x[2] = '.'
