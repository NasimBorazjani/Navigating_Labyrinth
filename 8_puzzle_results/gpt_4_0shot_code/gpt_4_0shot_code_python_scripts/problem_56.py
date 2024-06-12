
import heapq
import copy

# Define the initial state and goal state
initial_state = [[66, 96, 24, 10], [79, 33, 84, 100], [22, 80, 15, '_']]
goal_state = [[100, 96, 84, 80], [66, 33, 24, 22], [15, 10, '_', '_']]

# Define the directions of movement
directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

# Define the A* search function
def a_star_search(initial_state, goal_state):
    # Initialize the priority queue
    queue = []
    heapq.heappush(queue, (0, 0, initial_state, [], (1, 3)))

    # Perform the search
    while queue:
        _, g, current_state, moves, empty_spot = heapq.heappop(queue)
        if current_state == goal_state:
            return moves
        for dx, dy in directions:
            x, y = empty_spot[0] + dx, empty_spot[1] + dy
            if 0 <= x < 3 and 0 <= y < 4:
                next_state = copy.deepcopy(current_state)
                next_state[empty_spot[0]][empty_spot[1]], next_state[x][y] = next_state[x][y], next_state[empty_spot[0]][empty_spot[1]]
                h = sum(abs(i//4 - next_state[i//4][i%4]//4) + abs(i%4 - next_state[i//4][i%4]%4) for i in range(12))
                heapq.heappush(queue, (g+h, g+1, next_state, moves+[next_state[x][y]], (x, y)))

# Print the solution
print(a_star_search(initial_state, goal_state))
