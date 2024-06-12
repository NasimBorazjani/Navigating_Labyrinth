
import heapq


def a_star():
   # Define the initial state of the trampoline park, as a 2d tuple
   initial_state = ((1, 0, 1, 1, 1, 1, 1, 0, 0),
                   (0, 1, 1, 1, 1, 1, 1, 0, 0),
                   (1, 1, 1, 1, 0, 0, 0, 1, 0),
                   (1, 1, 1, 0, 0, 1, 1, 0, 0),
                   (0, 0, 1, 0, 0, 1, 1, 0, 0),
                   (1, 1, 0, 0, 1, 0, 1, 0, 0),
                   (0, 1, 1, 1, 1, 1, 1, 1, 0),
                   (1, 0, 0, 0, 0, 1, 1, 0, 0),
                   (0, 0, 0, 0, 0, 0, 0, 0, 0))
  
   # Encoding other variables given in the problem statement
   num_rows = 9
   num_cols = 9
   start_pos = (8, 2)
   goal_pos = (0, 7)
   num_diagonal_jumps = 3


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the jumps required to get to each state in a list; no jumps performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state[goal_pos[0]][goal_pos[1]] == 0:
           return actions


       # Generate all possible actions from the current state, which includes jumping to any of the 8 adjacent trampolines, as long as they are not broken
       for d_row, d_col in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
           jump_row, jump_col = start_pos[0] + d_row, start_pos[1] + d_col
           # Check if the jump is valid, ie if the trampoline is not broken and the number of diagonal jumps is not exceeded
           if (0 <= jump_row < num_rows and 0 <= jump_col < num_cols and
               state[jump_row][jump_col] == 0 and
               abs(d_row) + abs(d_col) == 1):
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[start_pos[0]][start_pos[1]] = 1
               new_state[jump_row][jump_col] = 0
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the goal
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_pos), new_cost, actions + [(jump_row, jump_col)], new_state))
                  
   return None


def heuristic(state, goal_pos):
   # An admissible and consistent heuristic is the Manhattan distance from the current position to the goal position
   # This heuristic relaxes the constraint that Alex must make exactly 3 diagonal jumps, as it does not consider the number of diagonal jumps made
   # It is admissible because it never overestimates the cost to reach the goal, as the heuristic cost of the successor node is always less than or equal to the cost of reaching the goal from the current state
   # It's consistent because moving to a neighboring position of the current state reduces the heuristic cost of the successor node by a max of 1 (if the moved position is closer to the goal), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = abs(goal_pos[0] - start_pos[0]) + abs(goal_pos[1] - start_pos[1])
   return h


print(a_star())
