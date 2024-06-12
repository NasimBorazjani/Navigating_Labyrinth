
import heapq


def initialize():
   # Define the initial state of the puzzle as a 2d tuple
   initial_state = (('77', '49', '_'),
                   ('56', '72', '74'),
                   ('96', '33', '59'))
   num_rows = 3
   num_cols = 3
   goal_state = (('8', '7', '6'),
                 ('5', '4', '3'),
                 ('2', '1', '_'))


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


       # Generate all possible actions from the current state, which involves swapping the empty spot with any of the 8 neighboring tiles
       for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
           new_row, new_col = state.index('_') + d_row, state.index('_') + d_col
           # Check if the new state would be valid, ie the new state must have the empty spot in a valid position and the new state must not have any tiles out of order
           if (0 <= new_row < num_rows and 0 <= new_col < num_cols and
               all(int(state[i][j]) >= int(state[i][k]) for i in range(num_rows) for j in range(num_cols) if state[i][j] != '_' for k in range(num_cols) if state[i][k] != '_' and j != k)):
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[new_row][new_col], new_state[state.index('_') // num_rows][state.index('_') % num_cols] = new_state[state.index('_') // num_rows][state.index('_') % num_cols], new_state[new_row][new_col]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to solve the puzzle
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state[new_row][new_col]], new_state))
   return None




def heuristic(state, goal_state):
   # An admissible and consistent heuristic for this problem is the Manhattan distance (shortest path) from the current state to the goal state
   # The heuristic relaxes the constraints that the tiles can move in 4 directions, that the tiles can be out of order in the current state, and that the goal state is in descending order with the empty spot in the bottom right corner
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one state to an adjacent state is the number of tiles that need to be swapped, which is always greater than or equal to 1, the decrease in the Manhattan distance
   return abs(state.index('_') // num_rows - goal_state.index('_') // num_rows) + abs(state.index('_') % num_cols - goal_state.index('_') % num_cols)


print(a_star())
