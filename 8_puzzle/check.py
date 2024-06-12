import numpy as np
import copy

def is_feasible(board_main, swaps):
    board = copy.deepcopy(board_main)
    # Define the directions of movement
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    h, w = len(board), len(board[0])
    
    blank_pos = [(i, row.index("_")) for i, row in enumerate(board) if "_" in row][0]
    
    # Iterate over the numbers
    for swap in swaps:    
        # Check each direction
        for direction in directions:
            new_i = blank_pos[0] + direction[0]
            new_j = blank_pos[1] + direction[1]
            
            # Check if the new position is valid and contains the current number
            if 0 <= new_i < h and 0 <= new_j < w and board[new_i][new_j] == swap:
                # Swap the blank space and the number
                board[blank_pos[0]][blank_pos[1]], board[new_i][new_j] = board[new_i][new_j], board[blank_pos[0]][blank_pos[1]]
                # Update the position of the blank space
                blank_pos = (new_i, new_j)
                break
        else:
            # If no valid move was found, return False
            return False
    
    # If all numbers were successfully swapped, return True
    return True


def get_goal_board(start_board):
    # Flatten the list
    flat_list = [item for sublist in start_board for item in sublist]
    
    # Separate the '_' from the rest of the elements
    flat_list = [item for item in flat_list if item != '_']
    
    # Sort the flattened list
    flat_list.sort()
    
    flat_list = flat_list[::-1]
    
    # Add the '_' back to the end of the list
    flat_list.append('_')
    
    # Put the sorted numbers back into the original 2D list
    i = 0
    goal_board = copy.deepcopy(start_board)
    for sublist in goal_board:
        for j in range(len(sublist)):
            sublist[j] = flat_list[i]
            i += 1
    return goal_board


def is_correct(board_main, swaps):
    if not is_feasible(board_main, swaps):
        return False, None
    
    board = copy.deepcopy(board_main)
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    h, w = len(board), len(board[0])
    
    blank_pos = [(i, row.index("_")) for i, row in enumerate(board) if "_" in row][0]
    
    # Iterate over the numbers
    for swap in swaps:    
        # Check each direction
        for direction in directions:
            new_i = blank_pos[0] + direction[0]
            new_j = blank_pos[1] + direction[1]
            
            # Check if the new position is valid and contains the current number
            if 0 <= new_i < h and 0 <= new_j < w and board[new_i][new_j] == swap:
                # Swap the blank space and the number
                board[blank_pos[0]][blank_pos[1]], board[new_i][new_j] = board[new_i][new_j], board[blank_pos[0]][blank_pos[1]]
                # Update the position of the blank space
                blank_pos = (new_i, new_j)
                break
    
    goal_board = get_goal_board(board)
    
    if goal_board == board:
        return True, len(swaps)
    return False, None

"""board = [[70, 58, '_'], [38, 95, 78], [98, 7, 89]]
swaps = [58, 95, 7, 98, 38, 70, 95, 58, 78, 7, 98, 38, 70, 98, 58, 95, 98, 70]
print(is_feasible(board, swaps))
print(is_correct(board, swaps))"""

#print(is_correct([[74, 69, 29, 78], [40, 98, 57, 45], [97, 34, 33, '_']], []))
