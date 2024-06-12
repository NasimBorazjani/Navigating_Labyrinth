
import heapq
import copy

# Define the initial and goal states
initial_state = [[25, 94, 12, '_'], [70, 43, 47, 85], [86, 64, 52, 92]]
goal_state = [[94, 92, 86, 85], [70, 64, 52, 47], [43, 25, 12, '_']]

# Define the possible moves
moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# Function to get the position of the empty tile
def get_empty_tile(state):
    for i in range(3):
        for j in range(4):
            if state[i][j] == '_':
                return i, j

# Function to get the Manhattan distance of a state
def get_manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(4):
            if state[i][j] != '_':
                x, y = divmod(state[i][j]-1, 4)
                distance += abs(x - i) + abs(y - j)
    return distance

# Function to perform the A* search
def astar_search():
    # Initialize the priority queue with the initial state
    queue = [(get_manhattan_distance(initial_state), initial_state)]
    # While the queue is not empty
    while queue:
        # Pop the state with the smallest estimated cost
        cost, state = heapq.heappop(queue)
        # If this state is the goal state
        if state == goal_state:
            return state
        # Get the position of the empty tile
        x, y = get_empty_tile(state)
        # For each possible move
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            # If the move is within the grid
            if 0 <= nx < 3 and 0 <= ny < 4:
                # Copy the current state
                new_state = copy.deepcopy(state)
                # Swap the empty tile with the adjacent tile
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                # Add the new state to the queue
                heapq.heappush(queue, (cost - get_manhattan_distance(state) + get_manhattan_distance(new_state) + 1, new_state))

# Print the solution
print(astar_search())
