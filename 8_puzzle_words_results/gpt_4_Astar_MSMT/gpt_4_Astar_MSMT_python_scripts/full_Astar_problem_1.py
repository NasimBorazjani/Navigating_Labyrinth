
import heapq

def initialize():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('i', 'c', 'a', 'm'),
                   ('h', 'p', 'l', 'o'),
                   ('_', 'r', 'a', 'y'),
                   ('d', 'l', 'e', 'r'))
   num_rows = 4
   num_cols = 4
   # Define the goal state of the board as a 2d tuple
   goal_state = (('_', 'c', 'a', 'm'),
                 ('h', 'i', 'l', 'l'),
                 ('p', 'r', 'a', 'y'),
                 ('d', 'o', 'e', 'r'))

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

       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
       for d_row, d_col in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
           # Get the coordinate of the blank space
           blank_coord = [(i, j) for i, row in enumerate(state) for j, element in enumerate(row) if element == '_'][0]
           new_row, new_col = blank_coord[0] + d_row, blank_coord[1] + d_col
           # Check if the new coordinate is valid, ie if the new position is within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[blank_coord[0]][blank_coord[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_coord[0]][blank_coord[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to sort the board
               new_cost = g + 1

               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The direction of the swap action is the direction in which the blank space was moved
                   if d_row == -1 and d_col == 1:
                       action = 'up-right'
                   elif d_row == 1 and d_col == 1:
                       action = 'down-right'
                   elif d_row == -1 and d_col == -1:
                       action = 'up-left'
                   elif d_row == 1 and d_col == -1:
                       action = 'down-left'
                   heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [action], new_state))
   return None

def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the count of tiles that are not in their goal position
   # This heuristic relaxes the constraint that only the blank space can be moved, and only to a diagonal position
   # It is admissible because it never overestimates the cost to reach the goal, as each misplaced tile must be moved at least once
   # It's consistent because moving a tile reduces the heuristic cost of the successor node by a max of 1 (if the moved tile is placed in its goal position), which is equal to the cost of reaching the successor node
   # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
   # And the cost of the goal state is 0, as all tiles will be in their goal position
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] != goal[i][j]:
               h += 1
   return h


print(a_star())
