
from collections import deque

def bfs(init_board, target_words):
    # Define the 4 possible moves
    moves = [(-1, 1), (1, 1), (-1, -1), (1, -1)]
    # Convert the target words into a set for faster lookup
    target_set = set(target_words)
    # Initialize the queue with the initial state and the empty path
    queue = deque([(init_board, [])])
    # Initialize the set of visited states with the initial state
    visited = set([str(init_board)])

    while queue:
        # Remove a state from the queue
        board, path = queue.popleft()
        # Check if the board spells the target words
        if str(board[1:]) in target_set:
            return path
        # Generate all possible next states
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '_':
                    for move in moves:
                        new_i, new_j = i + move[0], j + move[1]
                        # Check if the new state is valid
                        if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]):
                            # Swap the blank tile with the neighboring tile
                            new_board = [list(row) for row in board]
                            new_board[i][j], new_board[new_i][new_j] = new_board[new_i][new_j], new_board[i][j]
                            # Convert the new state into a string and check if it was visited before
                            new_state = str(new_board)
                            if new_state not in visited:
                                # Mark the new state as visited
                                visited.add(new_state)
                                # Insert the new state into the queue with the extended path
                                queue.append((new_board, path + [move]))

    # If there is no solution, return an empty list
    return []

# The initial board
init_board = [['y', 'h', 'r', 'm', '_', 's'], 
              ['b', 'o', 'w', 'k', 'r', 'u'], 
              ['r', 'e', 'l', 'e', 'u', 's'], 
              ['c', 'c', 'a', 'u', 't', 'y']]

# The target words
target_words = ['humus', 'bywork', 'cereus', 'clarty']

# Call the function and print the result
print(bfs(init_board, target_words))
