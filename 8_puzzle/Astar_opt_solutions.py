
import heapq
import sys

def a_star(initial_state):
    # Convert the initial state to a tuple of tuples
    initial_state = tuple(tuple(row) for row in initial_state)
    
    # Flatten the initial state and sort it in descending order to get the goal state
    goal_state = sorted([num for sublist in initial_state for num in sublist if num != '_'], reverse=True) + ['_']
    # Convert the goal state back to a tuple of tuples
    goal_state = tuple(tuple(goal_state[i:i+len(initial_state[0])]) for i in range(0, len(goal_state), len(initial_state[0])))

    num_rows = len(initial_state)
    num_cols = len(initial_state[0])

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes swapping any of the 4 tiles neighboring the empty spot 
        empty_row, empty_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == '_'][0]
        for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            swap_row, swap_col = empty_row + d_row, empty_col + d_col
            # Check if the new position is valid, ie if the swap tile is a valid tile on the board
            if 0 <= swap_row < num_rows and 0 <= swap_col < num_cols:
                # Generate the new state
                new_state = [list(row[:]) for row in state]
                number_to_be_swapped = new_state[swap_row][swap_col]
                new_state[empty_row][empty_col], new_state[swap_row][swap_col] = new_state[swap_row][swap_col], new_state[empty_row][empty_col]
                new_state = tuple(tuple(row) for row in new_state)
                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), g + 1, actions + [number_to_be_swapped], new_state))
    return None

def heuristic(state, goal):
    # The heuristic function is the sum of the Manhattan distances of each tile from its goal position
    h = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != '_':
                goal_row, goal_col = [(x, y) for x in range(len(goal)) for y in range(len(goal[x])) if goal[x][y] == state[i][j]][0]
                h += abs(i - goal_row) + abs(j - goal_col)
    return h

def main():
    # Read the initial state from the command line
    initial_state = eval(sys.argv[1])
    print(a_star(initial_state))

if __name__ == "__main__":
    main()