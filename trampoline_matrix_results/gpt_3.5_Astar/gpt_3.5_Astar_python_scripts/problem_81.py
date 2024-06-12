
import heapq


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1),
                     (0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0),
                     (1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1),
                     (0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1),
                     (1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0),
                     (0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0),
                     (0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1),
                     (0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0),
                     (1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1),
                     (0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1),
                     (1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1),
                     (1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0),
                     (1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1),
                     (1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0))
    num_rows = 14
    num_cols = 14
    start = (11, 12)
    goal = (3, 1)
    # Define the possible moves Alex can make
    moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    # Initialize a priority queue to store the states to be visited
    queue = []
    # Record the actions taken to reach each state
    actions = {}
    # Record the cost to reach each state
    costs = {}
    # Record the number of diagonal jumps made to reach each state
    diagonal_jumps = {}
    # Initialize the starting state
    heappush(queue, (0, 0, start))
    actions[start] = []
    costs[start] = 0
    diagonal_jumps[start] = 0

    while queue:
        _, cost, current = heappop(queue)

        # Check if the current state is the goal state
        if current == goal and diagonal_jumps[current] == 4:
            return actions[current]

        # Generate all possible actions from the current state
        for move in moves:
            new_row = current[0] + move[0]
            new_col = current[1] + move[1]

            # Check if the new position is within the grid and not a broken trampoline
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] == 0:
                new_state = (new_row, new_col)
                new_cost = cost + 1
                new_diagonal_jumps = diagonal_jumps[current]

                # Check if the move is diagonal
                if abs(move[0]) == 1 and abs(move[1]) == 1:
                    new_diagonal_jumps += 1

                # If the number of diagonal jumps is within the limit, proceed
                if new_diagonal_jumps <= 4:
                    # Calculate the heuristic cost based on the Manhattan distance to the goal
                    h = abs(new_row - goal[0]) + abs(new_col - goal[1])
                    # Calculate the total cost
                    total_cost = new_cost + h

                    # If the new state has not been visited or a lower cost path is found, update the records
                    if new_state not in costs or new_cost < costs[new_state]:
                        costs[new_state] = new_cost
                        diagonal_jumps[new_state] = new_diagonal_jumps
                        actions[new_state] = actions[current] + [new_state]
                        heappush(queue, (total_cost, new_cost, new_state))

    return None


print(a_star())
