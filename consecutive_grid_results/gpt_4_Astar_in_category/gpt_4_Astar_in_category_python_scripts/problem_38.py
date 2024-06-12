
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid as a 2d tuple
   initial_state = (('x', '89', '95'),
                   ('x', 'x', '96'),
                   ('74', '93', 'x'))
   num_rows = 3
   num_cols = 3
   # Create the set of the valid numbers that could be in the grid
   numbers = set(range(45, 98))


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must not have any remaining unknown numbers, thus we need to get (the coordinates of) the unknown numbers to check whether the current state is the goal state
       x_coords = [(i, j) for i, row in enumerate(state) for j, element in enumerate(row) if element == 'x']
       if not x_coords:
           # Convert the cells of the state to ints to calculate and compare the sum of the specific positions in the current state with the given goal sums
           state_array = np.array([[int(element) for element in row] for row in state])
           # Check if the numbers in each row and column are strictly increasing or decreasing
           if (all(all(state_array[i, j] < state_array[i, j + 1] for j in range(num_cols - 1)) or all(state_array[i, j] > state_array[i, j + 1] for j in range(num_cols - 1)) for i in range(num_rows)) and
               all(all(state_array[i, j] < state_array[i + 1, j] for i in range(num_rows - 1)) or all(state_array[i, j] > state_array[i + 1, j] for i in range(num_rows - 1)) for j in range(num_cols))):
               return actions


       # If the state has at least 1 remaining unknown number, generate all possible actions from the current state, which includes replacing the next x in the grid with any of unique integers in the range
       else:
           first_x_coord = x_coords[0]
           # The number must be unique and not be present in any other cells of the grid
           used_numbers  = set(int(cell) for row in state for cell in row if cell != 'x')
           for number in numbers:
               # Check if the new state, containing the new number, would be valid; ie the number must be unique and the sum of specified positions must not exceed the goal sums with the addition of the new number
               if number not in used_numbers:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   new_state[first_x_coord[0]][first_x_coord[1]] = str(number)
                   new_state = tuple(tuple(row) for row in new_state)
                   # The additional cost of this state is the value of the number replaced with x as we are trying to minimize the sum of the numbers in the grid
                   new_cost = g + number
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # Relaxing the constraints on the columns sums and the diagonal sum to calculate the heuristic
                       h = heuristic(new_state, numbers)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(first_x_coord[0], first_x_coord[1], number)], new_state))
   return None




def heuristic(state, numbers):
   # The heuristic function can be a simulation of filling the grid greedily, using the next smallest number repeatedly as long as the number is unique and the order of the numbers in the rows and columns is maintained
   # This heuristic is admissible because it is greedy, always opting for the action that fills the grid the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a number is removed from the grid, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of water that can be added to the bucket is by using the largest jug that won't cause an overflow, which is exactly the jug used to fill the bucket in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)


   # Get numbers not used in the state currently
   used_numbers = set(int(cell) for row in state for cell in row if cell != 'x')
   available_numbers = sorted(list(numbers - used_numbers))
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] == 'x' and available_numbers:
               h += available_numbers.pop(0)
   return h


print(a_star())
