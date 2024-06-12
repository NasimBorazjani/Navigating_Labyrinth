
import heapq
import numpy as np


def a_star():
    # Define the initial grid state
    grid = np.array([[37, 50, 'x', 70],
                     ['x', 46, 'x', 65],
                     [41, 43, 'x', 49],
                     ['x', 30, 'x', 'x']])
    
    # Define the range of numbers that can replace 'x'
    numbers = list(range(22, 73))
    
    # Define the initial state as a tuple
    initial_state = tuple(map(tuple, grid))
    
    # Encoding other variables given in the problem statement
    num_rows = 4
    num_cols = 4
    
    visited_costs = {}
    visited_costs[initial_state] = 0
    
    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [], initial_state, set(numbers))]
    
    while queue:
        _, g, actions, state, available_numbers = heapq.heappop(queue)
        
        # If there are no more unknown numbers in the grid, return the actions taken
        if 'x' not in np.array(state).flatten():
            return actions
        
        # Generate all possible actions from the current state
        for row in range(num_rows):
            for col in range(num_cols):
                if state[row][col] == 'x':
                    for num in available_numbers:
                        # Create a copy of the current state
                        new_state = [list(row) for row in state]
                        new_state[row][col] = num
                        new_state = tuple(map(tuple, new_state))
                        
                        # Update the set of available numbers
                        new_available_numbers = available_numbers.copy()
                        new_available_numbers.remove(num)
                        
                        # Calculate the cost of the new state
                        new_cost = g + num
                        
                        # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (new_cost + heuristic(new_state, new_available_numbers), new_cost, actions + [(row, col, num)], new_state, new_available_numbers))
    
    return None


def heuristic(state, available_numbers):
    # An admissible and consistent heuristic is the sum of the minimum possible values that can replace the remaining 'x's in the grid
    # The heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing
    # It is admissible because it underestimates the cost to reach the goal state, as the sum of the minimum possible values is always less than the actual sum
    # It is consistent because the estimated cost of the next node is higher if a number is added to the grid, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the minimum possible value that can replace the 'x' is always less than or equal to the actual value
    h = 0
    for row in state:
        for col in row:
            if col == 'x':
                h += min(available_numbers)
    return h


print(a_star())
