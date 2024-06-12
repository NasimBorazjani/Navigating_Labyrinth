
import heapq


def initialize():
   # Define the initial state of the puzzle as a 2d tuple
   initial_state = (('36', '16', '48'),
                   ('86', '_', '13'),
                   ('89', '31', '37'))
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


       # Check if the current state is the goal state
       if state == (('8', '7', '6'),
                   ('5', '_', '4'),
                   ('3', '2', '1')):
           return actions


       # Generate all possible actions from the current state, which includes swapping the empty spot with any of the 8 neighboring spots
       for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
           new_row, new_col = state.index('_') + d_row, state.index('_') + d_col
           # Check if the new coordinate is valid, ie if the new spot is within the bounds of the grid
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # To generate the new state, we must swap the empty spot with the number in the new spot
               new_state = [row[:] for row in state]
               new_state[new_row][new_col], new_state[state.index('_') // num_rows][state.index('_') % num_cols] = new_state[state.index('_') // num_rows][state.index('_') % num_cols], new_state[new_row][new_col]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost of the new state is the number of actions taken so far, as the task is to minimize the number of actions required to solve the puzzle
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The coordinate of the new state must be added to the actions
                   heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [new_state[new_row][new_col]], new_state))
   return None




def heuristic(state):
   # The heuristic function can be the Manhattan distance from the current state to the goal state
   # This heuristic is admissible because it is a lower bound on the cost to reach the goal state
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of the cost from the current node to a successor node plus the estimated cost from the successor node to the goal
   return sum(abs(state.index('_') // num_rows - i) + abs(state.index('_') % num_cols - j) for i, row in enumerate(state) for j, cell in enumerate(row) if cell != '_' and cell != '8')


print(a_star())
