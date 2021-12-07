import numpy as np

results = {}

def mark_number(board, number):
    index = get_index(board, number)
    board[index[0][0],index[1][0]] = 999

def get_index(board, number):
    return np.where(board == number)

def check_row_is_complete(board, number):
    # Check rows in which all values are equal
    for i in range(board.shape[0]):
        if np.all(board[i] == 999):
            return True

def check_col_is_complete(board, number):
    # Check Columns in which all values are equal
    trans_arr = board.T
    for i in range(trans_arr.shape[0]):
        if np.all(trans_arr[i] == 999):
            return True

def play_game(numbers, board, board_id):
    iteration = 1
    for number in numbers:
        if number in board:
            mark_number(board, number)
            if check_row_is_complete(board, number) or check_col_is_complete(board, number):
                results[board_id] = {
                    'board_data' : board, 
                    'winning_number' : number,
                    'iteration': iteration
                }
                break
        iteration += 1

def find_winner_id(results):
    smallest = None
    winner_id = None
    
    for b in results:
        number_of_iteration = results[b]['iteration']
        if not smallest:
            smallest = number_of_iteration
            winner_id = b
        else:
            if number_of_iteration < smallest:
                smallest = number_of_iteration
                winner_id = b
    return winner_id


def get_sum_of_all_unmarked_numbers(board_data):
    pos = np.where( board_data != 999)
    location = [item for item in zip(pos[0], pos[1])]
    sum = 0 
    for l in location:
        number = board_data[l[0],l[1]]
        sum += number
    return sum

# Load Data
with open('day4_input.txt', 'r') as f:
    data = [] 
    for value in f:
        line = value.split()
        if len(line) > 0:
            new_line = [int(i) for i in line]
            data.append(new_line)

def make_boards(data):
    array_size = 5
    boards = []
    for i in range(0, len(data), array_size):
        x = np.array(data[i:i+array_size])
        boards.append(x)
    return boards

numbers = [69,88,67,56,53,97,46,29,37,51,3,93,92,78,41,22,45,66,13,82,2,7,52,40,18,70,32,95,89,64,84,68,83,26,43,0,61,36,57,34,80,39,6,63,72,98,21,54,23,28,65,16,76,11,20,33,96,4,10,25,30,19,90,24,55,91,15,8,71,99,58,14,60,48,44,17,47,85,74,87,86,27,42,38,81,79,94,73,12,5,77,35,9,62,50,31,49,59,75,1]
#numbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

"""
Part One
"""
boards = make_boards(data)
for board_id, board_data in enumerate(boards):
    play_game(numbers, board_data, board_id)

winner_board = find_winner_id(results)
board_data = results[winner_board]['board_data']
winning_number = results[winner_board]['winning_number']
sum_of_all_unmarked_numbers = get_sum_of_all_unmarked_numbers(board_data)
final_score = winning_number * sum_of_all_unmarked_numbers
print("Part One", final_score)

"""
Part Two
"""


