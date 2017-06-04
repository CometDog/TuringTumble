board = []
row_count = [6,9,11,11,11,11,11,11,11,11,1]
max_row_count = len(row_count)
empty_value = '-'
exit_point = 'x'
no_column = ' '
right_dir = '\\'
left_dir = '/'
blue_marble = 'B'

def print_board(board):
    for row in board:
        print (' '.join(row))

def init_board(board):
    for row in range(max_row_count):
        diff_row_count = max_row_count - row_count[row]
        skip_middle_row = diff_row_count % 2
        columns_to_skip = []
        for skip_row in range(diff_row_count - skip_middle_row):
            if skip_row < ((diff_row_count - skip_middle_row) / 2):
                columns_to_skip.append(skip_row + 1)
            else:
                columns_to_skip.append(max_row_count - (skip_row -  ((diff_row_count - skip_middle_row) / 2)))
        board.append([])

        for column in range(max_row_count):
            if column == (max_row_count - 1) / 2:
                if skip_middle_row == 1:
                    board[row].append(no_column)
                else:
                    board[row].append(empty_value)
            elif column + 1 in columns_to_skip:
                board[row].append(no_column)
            else:
                board[row].append(empty_value)

def placements(board):
    board[0][4] = left_dir
    board[1][3] = left_dir
    board[2][2] = right_dir
    board[3][3] = right_dir
    board[4][4] = right_dir
    board[5][5] = left_dir
    board[6][4] = right_dir
    board[7][5] = left_dir
    board[8][4] = right_dir
    board[9][5] = left_dir

def right_dir_logic(x, y):
    x += 1
    y += 1
    coord = [x, y]
    return coord

def left_dir_logic(x, y):
    x += 1
    y -= 1
    coord = [x, y]
    return coord

def drop_blue_marble(board):
    coord = [0,4]
    while coord[0] < 10:
        if board[coord[0]][coord[1]] == empty_value:
            print ("Drop failed")
            break
        elif board[coord[0]][coord[1]] == right_dir:
            coord = right_dir_logic(coord[0],coord[1])
            print (coord)
        elif board[coord[0]][coord[1]] == left_dir:
            coord = left_dir_logic(coord[0],coord[1])
            print (coord)

init_board(board)
placements(board)
print_board(board)
drop_blue_marble(board)
