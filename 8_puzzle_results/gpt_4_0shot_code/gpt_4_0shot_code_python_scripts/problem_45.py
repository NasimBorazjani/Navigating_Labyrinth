
import heapq
import copy

# Define the initial and goal states
initial_state = [[11, 55, 69, 67], [19, 31, '_', 35], [64, 65, 88, 96]]
goal_state = [[96, 88, 69, 67], [65, 64, 55, 35], [31, 19, 11, '_']]

# Define the directions for moving the tiles
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# Define the A* search algorithm
def a_star_search(initial_state, goal_state):
    # Initialize the priority queue and the visited states
    queue = [(0, initial_state, [], 0)]
    visited_states = set()

    while queue:
        # Pop the state with the lowest estimated cost
        (estimated_cost, state, path, cost) = heapq.heappop(queue)

        # Check if the state is the goal state
        if state == goal_state:
            return path

        # Check if the state has been visited
        if str(state) in visited_states:
            continue

        # Mark the state as visited
        visited_states.add(str(state))

        # Find the empty spot
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == '_':
                    empty_spot = (i, j)

        # Try moving the empty spot in all directions
        for direction in directions:
            new_spot = (empty_spot[0] + direction[0], empty_spot[1] + direction[1])

            # Check if the new spot is within the grid
            if 0 <= new_spot[0] < len(state) and 0 <= new_spot[1] < len(state[0]):
                # Swap the empty spot with the new spot
                new_state = copy.deepcopy(state)
                new_state[empty_spot[0]][empty_spot[1]], new_state[new_spot[0]][new_spot[1]] = new_state[new_spot[0]][new_spot[1]], new_state[empty_spot[0]][empty_spot[1]]

                # Calculate the new cost and the new estimated cost
                new_cost = cost + 1
                new_estimated_cost = new_cost + heuristic(new_state, goal_state)

                # Push the new state into the queue
                heapq.heappush(queue, (new_estimated_cost, new_state, path + [new_state[new_spot[0]][new_spot[1]]], new_cost))

# Define the heuristic function
def heuristic(state, goal_state):
    # Use the Manhattan distance as the heuristic
    distance = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            for x in range(len(goal_state)):
                for y in range(len(goal_state[x])):
                    if state[i][j] == goal_state[x][y]:
                        distance += abs(i - x) + abs(j - y)
    return distance

# Solve the puzzle
solution = a_star_search(initial_state, goal_state)
print(solution)
