
import heapq

def initialize():
    # Define the initial state of the board and the list of target words
    initial_state = [['u', 'c', 'r', 'y'], ['d', 'n', 'n', 'r'], ['_', 'u', 'm', 'p'], ['k', 'e', 'e', 'e']]
    target_words = ['cry', 'dune', 'rump', 'knee']
    
    num_rows = len(initial_state)
    num_cols = len(initial_state[0])

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [], initial_state)]

    return initial_state, target_words, num_rows, num_cols, visited_costs, queue

def a_star():
    initial_state, target_words, num_rows, num_cols, visited_costs, queue = initialize()

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Convert the state to a string to check if it is the goal state
        state_str = str(state)
        if all(''.join(row) == target_words[i] for i, row in enumerate(state)) and state_str in target_words:
            return actions

        # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
        for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_row, new_col = None, None
            # Find the position of the blank space
            for i in range(num_rows):
                for j in range(num_cols):
                    if state[i][j] == '_':
                        new_row, new_col = i + d_row, j + d_col
                        break
            # Check if the new position of the blank space is valid
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                # Generate the new state by swapping the blank space with its diagonal neighbor
                new_state = [list(row) for row in state]
                new_state[new_row][new_col], new_state[i][j] = new_state[i][j], new_state[new_row][new_col]
                # Convert the new state to a string to track visited states
                new_state_str = str(new_state)
                # Calculate the cost of the new state
                new_cost = g + 1

                # If the new state has not been visited or a lower cost path to it is found, add it to the queue
                if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                    visited_costs[new_state_str] = new_cost
                    heapq.heappush(queue, (g + 1, new_cost, actions + [(d_row, d_col)], new_state))
    
    return None

print(a_star())
