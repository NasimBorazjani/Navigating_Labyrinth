
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid as a 2d tuple
   initial_state = (('x', 'x', '85'),
                   ('58', 'x', '84'),
                   ('x', '74', '59'))
   num_rows = 3
   num_cols = 3
   # Create the set of the valid numbers that could be in the grid
   numbers = set(range(48, 91))


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must not have any unknown numbers, thus we need to get (the coordinates of) the unknown numbers to check whether the current state is the goal state
       x_coords = [(i, j) for i, row in enumerate(state) for j, element in enumerate(row) if element == 'x']
       if not x_coords:
           # Convert the cells of the state to ints to calculate and compare the sum of the specific positions in the current state with the given goal sums
           state_array = np.array([[int(element) for element in row] for row in state])
           # Check if the state maintains the consecutive order in each row and column
           if (np.all([np.all(np.diff(row) > 0) or np.all(np.diff(row) < 0) for row in state_array]) and
               np.all([np.all(np.diff(state_array[:, j]) > 0) or np.all(np.diff(state_array[:, j]) < 0) for j in range(num_cols)])):
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
   # Relax the constraints on the order of the numbers in the rows and columns to compute an admissible and consistent heuristic
   # This heuristic considers the sum of the smallest unique numbers in the range that can replace the xs in the grid
   # The heuristic assumes xs can be filled with the smallest unique number in the range, even if the order of the numbers in the rows and columns is violated, thus reporting a lower cost estimate to reach the goal state, making it admissible
   # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of replacing an x in the grid with a number is the number itself, which is always greater than or equal to the number used to fill that position in the heuristic
   # Also the cost of the goal state is 0, as there are no unknown numbers to fill in the grid


   # Get numbers not used in the state currently
   used_numbers = set(int(cell) for row in state for cell in row if cell != 'x')
   available_numbers = sorted(list(numbers - used_numbers))
   h = 0
   for row in state:
       for cell in row:
           if cell == 'x' and available_numbers:
               h += available_numbers.pop(0)
   return h


print(a_star())
