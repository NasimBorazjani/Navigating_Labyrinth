
from collections import deque

def bfs(init_board, target_words):
    # Convert the board and target words into strings
    init_board_str = ''.join([''.join(row) for row in init_board])
    target_str = ''.join(target_words)
    
    # Define the 4 possible swaps
    swaps = {'up-right': (-1, 1), 'down-right': (1, 1), 'up-left': (-1, -1), 'down-left': (1, -1)}
    
    # Define the initial state
    init_state = (init_board_str, 0, 0)
    
    # Use a queue to perform BFS
    queue = deque([init_state])
    
    # Use a set to store visited states
    visited = set()
    
    while queue:
        # Pop a state from the queue
        board_str, x, y = queue.popleft()
        
        # If this state is the target state, return the swaps
        if board_str == target_str:
            return []
        
        # If this state has been visited before, skip it
        if (board_str, x, y) in visited:
            continue
        
        # Mark this state as visited
        visited.add((board_str, x, y))
        
        # Generate new states by swapping the blank tile with its neighbors
        for direction, (dx, dy) in swaps.items():
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(init_board) and 0 <= new_y < len(init_board[0]):
                new_board_str = list(board_str)
                new_board_str[x * len(init_board[0]) + y], new_board_str[new_x * len(init_board[0]) + new_y] = \
                    new_board_str[new_x * len(init_board[0]) + new_y], new_board_str[x * len(init_board[0]) + y]
                queue.append((''.join(new_board_str), new_x, new_y))
    
    # If there is no solution, return None
    return None

# Test the function
init_board = [['e', 's', '_', 't'], ['l', 'o', 'e', 'm'], ['c', 'a', 'o', 'k'], ['p', 'p', 'g', 'e'], ['d', 'r', 'a', 'w']]
target_words = ['sat', 'leep', 'mack', 'pogo', 'drew']
print(bfs(init_board, target_words))
