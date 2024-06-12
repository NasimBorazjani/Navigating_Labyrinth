
import heapq


def a_star():
   # Define the initial state of the magic square problem, with the grid represented as a 2D tuple
   initial_state = ((62, 82, 'x'), ('x', 'x', 'x'), ('x', 'x', 'x'))
   # Define the goal state, which is the grid with all unique integers from 50 to 84, with the specified sums for rows, columns, and diagonal
   goal_state = ((62, 82, 89), (56, 50, 101), (84, 75, 66))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   num_range = range(50, 85)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state))


   while queue:
       _, g, actions, state = heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes replacing 'x' with unique integers in the specified range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] == 'x':
                   for num in num_range:
                       # Generate the new state by replacing 'x' with the unique integer
                       new_state = [list(row[:]) for row in state]
                       new_state[row][col] = num
                       new_state = tuple(tuple(row) for row in new_state)
                       # Calculate the new cost, which is the sum of all numbers in the grid
                       new_cost = g + sum(sum(row) if isinstance(row, tuple) else row for row in new_state)
                      
                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # Add the action taken to reach this state to the list of actions
                           heappush(queue, (new_cost, new_cost, actions + [(row, col, num)], new_state))
   return None


print(a_star())
