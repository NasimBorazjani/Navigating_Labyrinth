
import heapq
import numpy as np


def initialize():
   # Define the initial state of the grid
   initial_state = np.array([['66', 'x', 'x'], ['65', '68', 'x'], ['x', 'x', '79']])
   # Define the range of numbers
   num_range = set(map(str, range(50, 93)))
   # Define the set of numbers already in the grid
   num_in_grid = set(initial_state.flatten())
   # Define the set of available numbers
   available_nums = num_range - num_in_grid
   # Define the dimensions of the grid
   num_rows = 3
   num_cols = 3
   # Define the initial cost
   initial_cost = 0
   # Define the initial path
   initial_path = []
   # Define the visited costs dictionary
   visited_costs = {}
   visited_costs[tuple(map(tuple, initial_state))] = initial_cost
   # Define the queue
   queue = [(initial_cost, initial_cost, initial_path, initial_state)]
   return num_range, num_in_grid, available_nums, num_rows, num_cols, initial_cost, initial_path, visited_costs, queue


def a_star():
   num_range, num_in_grid, available_nums, num_rows, num_cols, initial_cost, initial_path, visited_costs, queue = initialize()
   while queue:
       _, g, path, state = heapq.heappop(queue)
       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       if 'x' in state:
           # Get the position of the next 'x' in the grid
           x_pos = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == 'x'][0]
           # Generate all possible actions from the current state
           for num in available_nums:
               # Generate the new state
               new_state = state.copy()
               new_state[x_pos] = num
               # Check if the new state is valid
               if is_valid(new_state, num_rows, num_cols):
                   # Calculate the new cost
                   new_cost = g + calculate_cost(new_state)
                   # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                   if tuple(map(tuple, new_state)) not in visited_costs or new_cost < visited_costs[tuple(map(tuple, new_state))]:
                       visited_costs[tuple(map(tuple, new_state))] = new_cost
                       heapq.heappush(queue, (new_cost, new_cost, path + [(*x_pos, int(num))], new_state))
       else:
           return path
   return None


def is_valid(state, num_rows, num_cols):
   # Check if the numbers in each row and column are strictly increasing or decreasing
   for i in range(num_rows):
       row = state[i, :]
       if 'x' not in row and not (all(int(row[i]) < int(row[i + 1]) for i in range(len(row) - 1)) or all(int(row[i]) > int(row[i + 1]) for i in range(len(row) - 1))):
           return False
   for j in range(num_cols):
       col = state[:, j]
       if 'x' not in col and not (all(int(col[i]) < int(col[i + 1]) for i in range(len(col) - 1)) or all(int(col[i]) > int(col[i + 1]) for i in range(len(col) - 1))):
           return False
   return True


def calculate_cost(state):
   # Calculate the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left to the bottom-right corner
   top_row = state[0, :]
   right_col = state[:, -1]
   diagonal = state.diagonal()
   cost = sum(int(num) for num in top_row if num != 'x') + sum(int(num) for num in right_col if num != 'x') + sum(int(num) for num in diagonal if num != 'x')
   return cost


print(a_star())
