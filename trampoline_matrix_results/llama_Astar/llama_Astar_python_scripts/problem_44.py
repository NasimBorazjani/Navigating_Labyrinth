
import heapq


def a_star():
   # Define the initial state of the trampoline park, as a 2d tuple
   initial_state = ((1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1),
                   (0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1),
                   (0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1),
                   (1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1),
                   (1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0),
                   (0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1),
                   (0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0),
                   (0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1),
                   (0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0),
                   (0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0),
                   (0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1))
   num_rows = 11
   num_cols = 11
   start_pos = (2, 1)
   goal_pos = (10, 9)
   # The number of diagonal jumps required
   num_diagonal_jumps = 3


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
       if state[goal_pos[0]][goal_pos[1]] == 0:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 8 adjacent trampolines
       for row_offset in range(-1, 2):
           for col_offset in range(-1, 2):
               # Check if the new state would be valid, ie the new position is within the grid and the trampoline is functional
               new_row, new_col = start_pos[0] + row_offset, start_pos[1] + col_offset
               if (0 <= new_row < num_rows and 0 <= new_col < num_cols and state[new_row][new_col] == 0):
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   new_state[new_row][new_col] = 1
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of moves made, as the task is to minimize the number of moves required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # Relax the constraint on the number of diagonal jumps to calculate the heuristic
                       h = heuristic(new_state, goal_pos, num_diagonal_jumps)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(new_row, new_col)], new_state))
   return None


def heuristic(state, goal_pos, num_diagonal_jumps):
   # An admissible and consistent heuristic for this problem is the Manhattan distance to the goal position, plus the number of diagonal jumps made so far
   # This heuristic relaxes the constraint that the number of diagonal jumps must be exactly 3
   # It is admissible because it never overestimates the cost to reach the goal, as each diagonal jump must be made at least once
   # It's consistent because moving to a new position increases the heuristic cost of the successor node by a max of 1 (if the new position is diagonal), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = abs(goal_pos[0] - start_pos[0]) + abs(goal_pos[1] - start_pos[1])
   # Count the number of diagonal jumps made so far
   diagonal_jumps = sum(1 for row_offset in range(-1, 2) for col_offset in range(-1, 2) if abs(row_offset) == abs(col_offset))
   h += diagonal_jumps
   return h


print(a_star())
