
import heapq


def initialize():
   # Define the initial state of the puzzle as a 2d tuple
   initial_state = (('80', '62', '76'),
                   ('47', '67', '82'),
                   ('24', '73', '_'))
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
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == '_':
                   for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                       new_row, new_col = i + d_row, j + d_col
                       # Check if the new tile is within the bounds of the grid
                       if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[i][j], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[i][j]
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to solve the puzzle
                           new_cost = g + 1


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               # The heuristic function is not needed in this problem as the goal state is given and there are no constraints on the order of the tiles
                               heapq.heappush(queue, (new_cost, new_cost, actions + [int(state[i][j])], new_state))
   return None


print(a_star())