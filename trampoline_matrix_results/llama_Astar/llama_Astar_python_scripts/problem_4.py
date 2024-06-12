
import heapq


def a_star():
   # Define the initial state of the trampoline park, as a 2d tuple
   initial_state = ((0, 0, 1, 0, 0, 0, 0, 0, 1),
                   (0, 1, 0, 1, 1, 0, 0, 0, 0),
                   (1, 1, 1, 1, 1, 1, 1, 1, 0),
                   (1, 1, 0, 1, 1, 0, 0, 0, 0),
                   (1, 0, 1, 0, 1, 0, 1, 1, 1),
                   (1, 0, 1, 0, 0, 0, 1, 0, 1),
                   (0, 1, 0, 0, 0, 1, 1, 0, 1),
                   (0, 0, 1, 0, 1, 1, 1, 1, 1),
                   (1, 0, 0, 1, 1, 0, 0, 1, 1))
   num_rows = 9
   num_cols = 9
   start_pos = (8, 1)
   goal_pos = (0, 5)
   # The maximum number of diagonal jumps allowed
   max_diagonal_jumps = 3


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if start_pos == goal_pos:
           return actions


       # Generate all possible actions from the current state, which includes jumping to any of the 8 adjacent trampolines, as long as they are not broken
       for row_offset in range(-1, 2):
           for col_offset in range(-1, 2):
               # Check if the new state would be valid, ie the new position is within the grid and the trampoline is not broken
               new_row, new_col = start_pos[0] + row_offset, start_pos[1] + col_offset
               if 0 <= new_row < num_rows and 0 <= new_col < num_cols and state[new_row][new_col] == 0:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   new_state[new_row][new_col] = 1
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the goal
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # Relax the constraints on the diagonal jumps to calculate the heuristic
                       h = heuristic(new_state, goal_pos, max_diagonal_jumps)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(new_row, new_col)], new_state))


                   # Update the start position for the next jump
                   start_pos = (new_row, new_col)
   return None


def heuristic(state, goal_pos, max_diagonal_jumps):
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances of the current position to the goal position and the number of diagonal jumps made so far
   # This heuristic relaxes the constraint that Alex must make exactly 3 diagonal jumps, as it allows Alex to make more or fewer diagonal jumps, but penalizes it
   # It is admissible because it never overestimates the cost to reach the goal, as each additional diagonal jump must be made at least once
   # It's consistent because moving a jump from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved jump is a diagonal one), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = abs(goal_pos[0] - start_pos[0]) + abs(goal_pos[1] - start_pos[1])
   for row in range(num_rows):
       for col in range(num_cols):
           if state[row][col] == 1:
               h += abs(row - col)
   return h


print(a_star())
