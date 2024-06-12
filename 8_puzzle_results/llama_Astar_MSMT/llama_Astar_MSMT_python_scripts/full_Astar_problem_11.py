
import heapq


def initialize():
   # Define the initial state of the puzzle
   initial_state = (('59', '76', '55'),
                   ('54', '_', '85'),
                   ('50', '95', '53'))
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
       if state == (('1', '2', '3'),
                   ('4', '_', '8'),
                   ('5', '6', '7')):
           return actions


       # Generate all possible actions from the current state, which involves swapping the empty spot with any of the 8 neighboring tiles
       for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
           new_row, new_col = state[1].index('_') + d_row, state[1].index('_') + d_col
           # Check if the new coordinate is valid, ie if the new tile is within the bounds of the grid
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[new_row][new_col], new_state[state[1].index('_') // num_cols][state[1].index('_') % num_cols] = new_state[state[1].index('_') // num_cols][state[1].index('_') % num_cols], new_state[new_row][new_col]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to solve the puzzle
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [int(new_state[new_row][new_col])], new_state))
   return None




def heuristic(state):
   # The heuristic function can be the Manhattan distance between the current state and the goal state
   # This heuristic is admissible because it is a lower bound on the cost to reach the goal state
   # The heuristic is consistent because the estimated cost to reach the goal from any successor node is higher or equal to the cost to reach the goal from the current node, plus the cost to reach the successor node from the current node
   return sum(abs(state[i][j] - str(i * num_cols + j + 1)) for i in range(num_rows) for j in range(num_cols) if state[i][j] != '_')


print(a_star())
