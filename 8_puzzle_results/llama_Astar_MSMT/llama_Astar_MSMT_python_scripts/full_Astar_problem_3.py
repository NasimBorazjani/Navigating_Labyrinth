
import heapq


def initialize():
   # Define the initial state of the puzzle as a 2d tuple
   initial_state = (('87', '50', '82'),
                   ('68', '_', '74'),
                   ('23', '61', '11'))
   num_rows = 3
   num_cols = 3
   goal_state = (('9', '8', '7'),
                 ('6', '5', '4'),
                 ('3', '2', '1'))


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, goal_state, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, goal_state, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes swapping the empty spot with any of the 8 neighboring tiles
       for row_shift in [-1, 0, 1]:
           for col_shift in [-1, 0, 1]:
               # Check if the new state would be valid, ie the new state must not move the empty spot out of the grid and not move it to the same position
               if (0 <= state[0].index('_') + row_shift < num_rows and 0 <= state[0].index('_') + col_shift < num_cols and (row_shift != 0 or col_shift != 0)):
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   empty_spot_row, empty_spot_col = state[0].index('_')
                   new_state[empty_spot_row][empty_spot_col] = new_state[empty_spot_row + row_shift][empty_spot_col + col_shift]
                   new_state[empty_spot_row + row_shift][empty_spot_col + col_shift] = '_'
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to solve the puzzle
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The heuristic function is the Manhattan distance from the current state to the goal state
                       h = heuristic(state, goal_state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [int(new_state[empty_spot_row][empty_spot_col + col_shift])], new_state))
   return None




def heuristic(state, goal_state):
   # The heuristic function is the Manhattan distance from the current state to the goal state
   # The heuristic is admissible and consistent as it never overestimates the cost to reach the goal
   return abs(state[0].index('_') - goal_state[0].index('_')) + abs(state[0].index('_') - goal_state[0].index('_'))


print(a_star())
