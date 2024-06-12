
from collections import deque

def bfs(initial_board, target_words):
    # Define the 4 possible moves from the blank space
    moves = [(0, 1), (1, 1), (1, 0), (1, -1)]
    # Define the target state
    target_state = [list(word) for word in target_words]
    # Initialize the queue with the initial state and an empty path
    queue = deque([(initial_board, [])])
    # While there are states to explore
    while queue:
        # Dequeue a state
        board, path = queue.popleft()
        # If this state is the target state
        if board == target_state:
            # Return the path that led to this state
            return path
        # For each possible move
        for dx, dy in moves:
            # Compute the new position of the blank space
            x, y = next((i, j) for i, j in ((i, j) for i, row in enumerate(board) for j, cell in enumerate(row) if cell == '_'))
            new_x, new_y = x + dx, y + dy
            # If the new position is valid
            if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]):
                # Swap the blank space with the new cell
                new_board = [row.copy() for row in board]
                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
                # Enqueue the new state and the path that led to it
                queue.append((new_board, path + [dx, dy]))

# Test the function with the provided example
initial_board = [['_', 's', 'a', 'n'], ['q', 'u', 'o', 'u'], ['c', 'h', 'u', 't'], ['l', 't', 'r', 'e']]
target_words = ["sun", "quot", "chat", "lure"]
print(bfs(initial_board, target_words))
