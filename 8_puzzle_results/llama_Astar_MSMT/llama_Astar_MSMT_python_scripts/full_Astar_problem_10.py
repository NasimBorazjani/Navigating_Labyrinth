
import heapq


def initialize():
   # Define the initial state of the 8-puzzle as a 2d tuple
   initial_state = (('93', '88', '60'),
                   ('28', '18', '24'),
                   ('_', '47', '53'))
   num_rows = 3
   num_cols = 3


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == (('9', '8', '7'),
                   ('6', '5', '4'),
                   ('3', '2', '1')):
           return actions


       # Generate all possible actions from the current state, which includes swapping the empty spot with any of the 8 neighboring tiles
       for row_shift, col_shift in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
           new_row, new_col = state.index('_') + row_shift, state.index('_') + col_shift
           # Check if the new coordinate is valid, ie if the new tile is within the bounds of the grid
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[new_row][new_col], new_state[state.index('_')][state.index('_')] = new_state[state.index('_')][state.index('_')], new_state[new_row][new_col]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to solve the puzzle
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state[new_row][new_col]], new_state))
   return None




def heuristic(state):
   # The heuristic function can be the Manhattan distance from the current state to the goal state
   # This heuristic is admissible because it is a lower bound on the cost to reach the goal state
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of the cost from the current node to a successor node plus the estimated cost from the successor node to the goal
   return sum(abs(state.index('_') // 3 - row) + abs(state.index('_') % 3 - col) for row, col, value in enumerate(state[0]) if value != '_')


print(a_star())
