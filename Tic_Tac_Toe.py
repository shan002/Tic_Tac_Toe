board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

winner = None


def show_board():
    print('\n')
    for row in board:
        for index in row:
            if not index:
                print('-', end=' ')
            elif index == 1:
                print('0', end=' ')
            elif index == 8:
                print('X', end=' ')
        print('\n')


def player1():
    print('Player_1 Input')
    row = int(input('row: '))
    column = int(input('column: '))
    return row, column


def player2():
    print('Player_2 Input')
    row = int(input('row: '))
    column = int(input('column: '))
    return row, column


def determine_winner():
    global winner
    result_list = []
    result_list += [sum(row) for row in board]

    for i in range(3):
        s = sum([row[i] for row in board])
        result_list.append(s)

    result_list.append(sum([board[i][i] for i in range(3)]))
    result_list.append(sum([board[i][2 - i] for i in range(3)]))

    for r in result_list:
        if r == 3:
            winner = 'Player_1'
        elif r == 24:
            winner = 'Player_2'


def play():
    show_board()
    for i in range(9):
        if not i % 2:
            row, column = player1()
            while board[row - 1][column - 1]:
                print('\nThis box is already filled!\n')
                row, column = player1()
            board[row - 1][column - 1] = 1
        else:
            row, column = player2()
            while board[row - 1][column - 1]:
                print('\nThis box is already filled!\n')
                row, column = player2()
            board[row - 1][column - 1] = 8
        show_board()
        determine_winner()
        if winner:
            break

    if winner:
        print(f'\n\nWinner is {winner}\n')
    else:
        print(f'\n\nMatch is draw\n')


play()
