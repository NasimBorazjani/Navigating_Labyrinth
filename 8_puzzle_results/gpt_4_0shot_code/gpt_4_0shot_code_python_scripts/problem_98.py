
import heapq
import numpy as np

# Define the initial state and the goal state
initial_state = np.array([[89, 88, 62, 57, 79, 53], [92, 48, 61, 67, 78, 14], [32, 63, 27, '_', 19, 54]])
goal_state = np.array([[92, 89, 88, 79, 78, 67], [63, 62, 61, 57, 54, 53], [32, 27, 19, 14, '_', '_']])

# Define the heuristic function
def heuristic(state):
    return np.sum(state != goal_state)

# Define the search function
def search(state):
    # Initialize the priority queue
    queue = [(heuristic(state), state)]
    # Initialize the set of visited states
    visited = set()
    # Initialize the list of moves
    moves = []
    # While the queue is not empty
    while queue:
        # Pop the state with the lowest heuristic value
        _, state = heapq.heappop(queue)
        # If this state is the goal state
        if np.array_equal(state, goal_state):
            # Return the list of moves
            return moves
        # If this state has not been visited yet
        if str(state) not in visited:
            # Add this state to the set of visited states
            visited.add(str(state))
            # For each possible move
            for move in ['left', 'right', 'up', 'down']:
                # Try to make the move
                new_state, moved_tile = make_move(state, move)
                # If the move is valid
                if new_state is not None:
                    # Add the new state to the queue
                    heapq.heappush(queue, (heuristic(new_state), new_state))
                    # Add the moved tile to the list of moves
                    moves.append(moved_tile)
    # If no solution is found
    return None

# Define the function to make a move
def make_move(state, move):
    # Find the position of the empty spot
    empty_spot = np.where(state == '_')
    # Depending on the move
    if move == 'left':
        # If the empty spot is not on the left edge
        if empty_spot[1] > 0:
            # Swap the empty spot with the tile on the left
            state[empty_spot], state[empty_spot[0], empty_spot[1]-1] = state[empty_spot[0], empty_spot[1]-1], state[empty_spot]
            # Return the new state and the moved tile
            return state, state[empty_spot]
    elif move == 'right':
        # If the empty spot is not on the right edge
        if empty_spot[1] < state.shape[1] - 1:
            # Swap the empty spot with the tile on the right
            state[empty_spot], state[empty_spot[0], empty_spot[1]+1] = state[empty_spot[0], empty_spot[1]+1], state[empty_spot]
            # Return the new state and the moved tile
            return state, state[empty_spot]
    elif move == 'up':
        # If the empty spot is not on the top edge
        if empty_spot[0] > 0:
            # Swap the empty spot with the tile above
            state[empty_spot], state[empty_spot[0]-1, empty_spot[1]] = state[empty_spot[0]-1, empty_spot[1]], state[empty_spot]
            # Return the new state and the moved tile
            return state, state[empty_spot]
    elif move == 'down':
        # If the empty spot is not on the bottom edge
        if empty_spot[0] < state.shape[0] - 1:
            # Swap the empty spot with the tile below
            state[empty_spot], state[empty_spot[0]+1, empty_spot[1]] = state[empty_spot[0]+1, empty_spot[1]], state[empty_spot]
            # Return the new state and the moved tile
            return state, state[empty_spot]
    # If the move is not valid
    return None, None

# Call the search function
print(search(initial_state))
