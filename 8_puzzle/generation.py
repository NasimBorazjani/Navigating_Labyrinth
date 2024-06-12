import numpy as np
import random

def generate_initial_board(h, w, max_num_in_baord, seed):
    random.seed(seed)
    board_nums = [random.randint(1, max_num_in_baord) for _ in range(h*w)]
    while len(set(board_nums)) != h*w:
        seed += 1
        random.seed(seed)
        board_nums = [random.randint(1, max_num_in_baord) for _ in range(h*w)]
        
    board_nums.sort()
    board_nums = board_nums[::-1]
    board = np.zeros((h, w)).tolist()
    
    for i in range(h):
        for j in range(w):
            board[i][j] = board_nums[i * w + j]
    board[h-1][w-1] = "_"
    return board

def swap_blank(board, seed):
    h, w = len(board), len(board[0])
    # Find the blank cell
    blank_pos = [(i, row.index("_")) for i, row in enumerate(board) if "_" in row][0]  

    swapped = False
    seed -= 1
    while not swapped:
        seed += random.randint(1, 10000)
        random.seed(seed)
        # Generate a random move
        move = random.choice(['up', 'down', 'left', 'right'])

        if move == 'up' and blank_pos[0] > 0:
            board[blank_pos[0]][blank_pos[1]], board[blank_pos[0] - 1][blank_pos[1]] = board[blank_pos[0] - 1][blank_pos[1]], board[blank_pos[0]][blank_pos[1]]
            swapped = True
        elif move == 'down' and blank_pos[0] < h - 1:
            board[blank_pos[0]][blank_pos[1]], board[blank_pos[0] + 1][blank_pos[1]] = board[blank_pos[0] + 1][blank_pos[1]], board[blank_pos[0]][blank_pos[1]]
            swapped = True
        elif move == 'left' and blank_pos[1] > 0:
            board[blank_pos[0]][blank_pos[1]], board[blank_pos[0]][blank_pos[1] - 1] = board[blank_pos[0]][blank_pos[1] - 1], board[blank_pos[0]][blank_pos[1]]
            swapped = True
        elif move == 'right' and blank_pos[1] < w - 1:
            board[blank_pos[0]][blank_pos[1]], board[blank_pos[0]][blank_pos[1] + 1] = board[blank_pos[0]][blank_pos[1] + 1], board[blank_pos[0]][blank_pos[1]]
            swapped = True

    return board

def generate_puzzle(h, w, num_moves, seed):
    max_num_in_baord = 100
    board = generate_initial_board(h, w, max_num_in_baord, seed)
    for _ in range(num_moves):
        seed += 1
        board = swap_blank(board, seed)
    return board

#print(generate_puzzle(4, 3, 100, 1))
