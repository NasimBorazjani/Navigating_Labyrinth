import numpy as np
import copy
from nltk.corpus import words


def is_feasible(board_main, swaps):
    board = copy.deepcopy(board_main)
    
    directions = {'up-left': (-1, -1), 'down-left': (1, -1), 'up-right':(-1, 1), 'down-right': (1, 1)}
    
    h, w = len(board), len(board[0])
    
    blank_pos = [(i, row.index("_")) for i, row in enumerate(board) if "_" in row][0]
    
    # Iterate over the swaps
    for swap in swaps:   
        if swap not in directions:
            return False 
        direction  = directions[swap]
        new_i = blank_pos[0] + direction[0]
        new_j = blank_pos[1] + direction[1]
        
        # Check if the new position is valid 
        if 0 <= new_i < h and 0 <= new_j < w:
            # Swap the blank space and the number
            board[blank_pos[0]][blank_pos[1]], board[new_i][new_j] = board[new_i][new_j], board[blank_pos[0]][blank_pos[1]]
            # Update the position of the blank space
            blank_pos = (new_i, new_j)
        
        else:
            return False

    return True
    

def get_words_in_board(board):
    decoded_words = []
    
    for i in range(len(board)):
        row = board[i]
        if i == 0:
            row = row[1:]
        word = ''.join(row)
        words = word.split()
        decoded_words.extend(words)
    
    return decoded_words



def is_correct(board_main, target_words, swaps):
    board = copy.deepcopy(board_main)
    #diagonal swaps
    directions = {'up-left': (-1, -1), 'down-left': (1, -1), 'up-right':(-1, 1), 'down-right': (1, 1)}
    
    h, w = len(board), len(board[0])
    
    blank_pos = [(i, row.index("_")) for i, row in enumerate(board) if "_" in row][0]
    
    # Iterate over the numbers
    for swap in swaps:   
        if swap not in directions:
            return False, None
        direction  = directions[swap]
        new_i = blank_pos[0] + direction[0]
        new_j = blank_pos[1] + direction[1]
        
        # Check if the new position is valid 
        if 0 <= new_i < h and 0 <= new_j < w:
            # Swap the blank space and the number
            board[blank_pos[0]][blank_pos[1]], board[new_i][new_j] = board[new_i][new_j], board[blank_pos[0]][blank_pos[1]]
            # Update the position of the blank space
            blank_pos = (new_i, new_j)


    words_in_board = get_words_in_board(board)
    for board_word in words_in_board:
        if board_word not in target_words:
            return False, None
    return True, len(swaps)
    

"""board = [['e', 'b', 'a', 'd'], ['c', 'l', 'r', '_'], ['c', 'a', 'o', 'm']]
swaps = ["down-left", "up-left", "up-left"]

print(is_correct([[74, 69, 29, 78], [40, 98, 57, 45], [97, 34, 33, '_']], []))"""

