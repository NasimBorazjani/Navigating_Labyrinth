
import heapq


def a_star():
   # Define the initial state of the trampoline park as a 2d tuple
   initial_state = ((1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0),
                   (0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0),
                   (1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1),
                   (1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0),
                   (0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0),
                   (0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1),
                   (1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1),
                   (1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1),
                   (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0),
                   (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0),
                   (0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0),
                   (0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0),
                   (0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0),
                   (0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1))
   num_rows = 15
   num_cols = 15
   # The goal state is at position (13, 0)
   goal_state = (13, 0)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state
       if state[3] == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes jumping to any of the 8 adjacent trampolines
       for row_diff in range(-1, 2):
           for col_diff in range(-1, 2):
               # Check if the new state would be valid, ie the new position is within the grid and the trampoline is not broken
               new_row, new_col = state[3][0] + row_diff, state[3][1] + col_diff
               if 0 <= new_row < num_rows and 0 <= new_col < num_cols and state[new_row][new_col] == 0:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   new_state[3] = (new_row, new_col)
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the goal state
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(new_state, goal_state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(new_row, new_col)], new_state))
   return None


def heuristic(state, goal_state):
   # An admissible and consistent heuristic is the Manhattan distance between the current position and the goal position
   # This heuristic relaxes the constraint that Alex must make exactly 5 diagonal jumps, as the heuristic estimate for the goal state is 0, as the distance of the goal position would be 0 in the goal state
   # The heuristic is consistent because the cost of moving a position to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if the position is moved toward the goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of the goal position would be 0 in the goal state.
   h = abs(state[3][0] - goal_state[0]) + abs(state[3][1] - goal_state[1])
   return h


print(a_star())
