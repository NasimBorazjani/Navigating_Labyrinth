
import heapq


def initialize():
   # Define the initial state of the trampoline park as a 2d tuple
   initial_state = ((1, 0, 1, 1, 1, 1, 1, 0, 0),
                   (0, 1, 1, 1, 1, 1, 1, 0, 0),
                   (1, 1, 1, 1, 0, 0, 0, 1, 0),
                   (1, 1, 1, 0, 0, 1, 1, 0, 0),
                   (0, 0, 1, 0, 0, 1, 1, 0, 0),
                   (1, 1, 0, 0, 1, 0, 1, 0, 0),
                   (0, 1, 1, 1, 1, 1, 1, 1, 0),
                   (1, 0, 0, 0, 0, 1, 1, 0, 0),
                   (0, 0, 0, 0, 0, 0, 0, 0, 0))
   num_rows = 9
   num_cols = 9
   start_pos = (8, 2)
   goal_pos = (0, 7)
   # Create the set of the valid positions that could be in the grid
   valid_positions = set((i, j) for i in range(num_rows) for j in range(num_cols) if initial_state[i][j] == 0)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, start_pos, goal_pos, valid_positions, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, start_pos, goal_pos, valid_positions, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if start_pos in valid_positions and goal_pos not in valid_positions:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 8 adjacent trampolines
       for d_row, d_col in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
           new_pos = (start_pos[0] + d_row, start_pos[1] + d_col)
           # Check if the new position is valid and within the grid
           if new_pos in valid_positions:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[start_pos[0]][start_pos[1]] = 1
               new_state[new_pos[0]][new_pos[1]] = 0
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # Relaxing the constraints on the columns sums and the diagonal sum to calculate the heuristic
                   h = heuristic(new_state, goal_pos)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_pos], new_state))
   return None


def heuristic(state, goal_pos):
   # An admissible and consistent heuristic for this problem is the Manhattan distance from the current position to the goal position
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as each move increases the Manhattan distance by at least 1
   # It's consistent because moving a position closer to the goal increases the heuristic cost of the successor node by a max of 1 (if the moved position is closer to the goal), which is equal to the cost of reaching the successor node
   # Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = abs(start_pos[0] - goal_pos[0]) + abs(start_pos[1] - goal_pos[1])
   return h


print(a_star())
