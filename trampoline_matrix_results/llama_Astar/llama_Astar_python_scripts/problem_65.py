
import heapq


def a_star():
   # Define the initial state of the trampoline park as a 2d tuple
   initial_state = ((0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0),
                   (1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1),
                   (1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1),
                   (1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0),
                   (1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0),
                   (1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1),
                   (1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0),
                   (1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1),
                   (1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1),
                   (1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0),
                   (0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0),
                   (0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
                   (0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1))
   num_rows = 13
   num_cols = 13
   # The destination is at position (8, 9)
   destination = (8, 9)
   # The number of diagonal jumps Alex must make
   num_diagonal_jumps = 4


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the destination state
       if actions[-1] == destination:
           return actions


       # Generate all possible actions from the current state, which includes jumping to any of the 8 adjacent trampolines
       for row_offset in range(-1, 2):
           for col_offset in range(-1, 2):
               # Check if the new state would be valid, ie the new position is within the grid and the trampoline is not broken
               new_row, new_col = actions[-1][0] + row_offset, actions[-1][1] + col_offset
               if 0 <= new_row < num_rows and 0 <= new_col < num_cols and state[new_row][new_col] == 0:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   new_state[new_row][new_col] = 1
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the destination
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(new_state, destination, num_diagonal_jumps)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(new_row, new_col)], new_state))
   return None


def heuristic(state, destination, num_diagonal_jumps):
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances of each trampoline from the destination, plus the absolute difference between the number of diagonal jumps made so far and the required number of diagonal jumps
   # This heuristic relaxes the constraint that Alex must make exactly 4 diagonal jumps, as it allows Alex to make more or fewer diagonal jumps than required
   # It is admissible because it never overestimates the cost to reach the goal, as each additional diagonal jump must be made at least once
   # It's consistent because moving a jump from one trampoline to another reduces the heuristic cost of the successor node by a max of 1 (if the moved jump is diagonal), which is equal to the cost of reaching the successor node
   h = 0
   for row in range(len(state)):
       for col in range(len(state[row])):
           if state[row][col] == 0:
               # Calculate the Manhattan distance of the current trampoline from the destination
               manhattan_distance = abs(row - destination[0]) + abs(col - destination[1])
               # Calculate the number of diagonal jumps made so far from the current trampoline to the destination
               diagonal_jumps = abs(row - destination[0]) + abs(col - destination[1]) - abs(row - col)
               # Add the heuristic cost of the current trampoline to the estimate
               h += manhattan_distance + abs(num_diagonal_jumps - diagonal_jumps)
   return h


print(a_star())
