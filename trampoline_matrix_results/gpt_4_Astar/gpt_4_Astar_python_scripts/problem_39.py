
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (9, 9)
    goal_state = (0, 3)
    # Define the map of the trampoline park
    park_map = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
                [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                [0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0],
                [1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
                [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0],
                [1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0],
                [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0],
                [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1],
                [0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1]]
    # Define the possible moves Alex can make
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    # Define the size of the park
    park_size = 11

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[(initial_state, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [], initial_state, 0)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state, diagonal_jumps = heapq.heappop(queue)

        # If the current state is the goal state and the number of diagonal jumps is 3, return the actions taken
        if state == goal_state and diagonal_jumps == 3:
            return actions

        # Generate all possible actions from the current state
        for move in moves:
            new_state = (state[0] + move[0], state[1] + move[1])
            # Check if the new state is valid, i.e., within the park and not on a broken trampoline
            if (0 <= new_state[0] < park_size and 0 <= new_state[1] < park_size and
                park_map[new_state[0]][new_state[1]] == 0):
                # Calculate the new number of diagonal jumps
                new_diagonal_jumps = diagonal_jumps + 1 if move in [(1, 1), (-1, -1), (1, -1), (-1, 1)] else diagonal_jumps
                # The cost so far is the number of jumps made
                new_cost = g + 1
                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if (new_state, new_diagonal_jumps) not in visited_costs or new_cost < visited_costs[(new_state, new_diagonal_jumps)]:
                    visited_costs[(new_state, new_diagonal_jumps)] = new_cost
                    # The heuristic is the Manhattan distance to the goal state, plus the number of diagonal jumps still needed
                    h = abs(new_state[0] - goal_state[0]) + abs(new_state[1] - goal_state[1]) + max(0, 3 - new_diagonal_jumps)
                    heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state], new_state, new_diagonal_jumps))
    return None

print(a_star())
