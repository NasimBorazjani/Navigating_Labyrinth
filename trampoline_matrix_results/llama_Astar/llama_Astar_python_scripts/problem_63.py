
import heapq


def a_star():
   # Define the initial state of the trampoline park as a 2d tuple
   initial_state = ((1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0),
                   (1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0),
                   (0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1),
                   (1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1),
                   (0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1),
                   (0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1),
                   (0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1),
                   (0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1),
                   (1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1),
                   (0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0),
                   (0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0),
                   (0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1),
                   (1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0))
   num_rows = 13
   num_cols = 13
   start_pos = (4, 0)
   goal_pos = (12, 12)
   # The maximum number of diagonal jumps allowed
   max_diagonal_jumps = 4


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
       for row_offset in range(-1, 2):
           for col_offset in range(-1, 2):
               # Check if the new state would be valid, ie the new position is within the grid and the number of diagonal jumps does not exceed the maximum
               if (0 <= start_pos[0] + row_offset < num_rows and 0 <= start_pos[1] + col_offset < num_cols and
                   (row_offset == 0 or col_offset == 0) and
                   abs(row_offset) + abs(col_offset) <= max_diagonal_jumps):
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   new_state[start_pos[0] + row_offset][start_pos[1] + col_offset] = 1
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the goal
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(new_state, goal_pos)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(start_pos[0] + row_offset, start_pos[1] + col_offset)], new_state))
   return None


def heuristic(state, goal_pos):
   # An admissible and consistent heuristic for this problem is the Manhattan distance from the current position to the goal position
   # This heuristic relaxes the constraint that Alex must make exactly 4 diagonal jumps, as it allows Alex to jump to any of the 8 adjacent trampolines
   # It is admissible because it never overestimates the cost to reach the goal, as each jump is either horizontal or vertical
   # It's consistent because moving to a neighboring position reduces the heuristic cost of the successor node by a max of 1 (if the moved position is closer to the goal), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = abs(goal_pos[0] - start_pos[0]) + abs(goal_pos[1] - start_pos[1])
   return h


print(a_star())
