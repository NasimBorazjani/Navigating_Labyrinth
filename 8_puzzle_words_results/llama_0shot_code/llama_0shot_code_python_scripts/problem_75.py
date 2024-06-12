
from collections import deque

def bfs(init_board, words):
    # Define the 4 possible moves
    moves = [(-1, 1), (1, 1), (-1, -1), (1, -1)]
    # Convert the list of words into a set for faster lookup
    words = set(words)
    # Create a queue for BFS and insert the initial state
    queue = deque([(init_board, 0)])
    # Create a set to store all visited states
    visited = set()
    while queue:
        # Remove a state from the queue
        board, steps = queue.popleft()
        # Convert the board into a string representation for easy lookup
        state = ''.join([''.join(row) for row in board])
        if state in visited:
            continue
        # Mark the state as visited
        visited.add(state)
        # Check if the state is the goal state
        if set(state.split('_')[1:]).issubset(words):
            return steps
        # Generate all possible next states
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '_':
                    for move in moves:
                        ni, nj = i + move[0], j + move[1]
                        if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                            new_board = [row.copy() for row in board]
                            new_board[ni][nj], new_board[i][j] = new_board[i][j], new_board[ni][nj]
                            queue.append((new_board, steps + 1))

# Test the function
init_board = [['_', 's', 's', 'h', 'o'], ['r', 'i', 'l', 'o', 'y'], ['j', 'o', 'l', 'i', 'p'], ['d', 'r', 'a', 'i', 'n'], ['n', 'i', 'v', 'a', 'l']]
words = ['soho', 'rilly', 'josip', 'drain', 'nival']
print(bfs(init_board, words))
