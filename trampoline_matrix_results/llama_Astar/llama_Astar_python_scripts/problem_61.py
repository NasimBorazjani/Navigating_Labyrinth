
import heapq


def a_star():
   # Define the initial state of the trampoline park as a 2d tuple
   initial_state = ((1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0),
                   (0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1),
                   (1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1),
                   (0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1),
                   (1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0),
                   (1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1),
                   (1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1),
                   (0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1),
                   (0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
                   (0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0),
                   (0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1),
                   (1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1),
                   (0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1))
   num_rows = 13
   num_cols = 13
   # The goal state is at position (7, 1)
   goal_state = (7, 1)


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the jumps required to get to each state in a list; no jumps performed to reach the initial state
   queue = [(0, 0, [(0, 11)], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
       if actions[-1] == goal_state:
           return actions


       # Generate all valid actions from the current state, which includes jumping to any of the eight adjacent trampolines, as long as they are not broken
       for row_diff in range(-1, 2):
           for col_diff in range(-1, 2):
               # Check if the new position is valid, ie if the new position is within the grid and the trampoline is not broken
               new_row, new_col = actions[-1][0] + row_diff, actions[-1][1] + col_diff
               if 0 <= new_row < num_rows and 0 <= new_col < num_cols and state[new_row][new_col] == 0:
                   # The actions is valid, generate the new state
                   new_state = [list(row[:]) for row in state]
                   # Do the jump
                   new_state[new_row][new_col] = 1
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of jumps made, as our objective is to minimize the number of jumps required to reach the goal state
                   new_cost = g + 1
                  
                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(new_row, new_col)], new_state))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance from the current state to the goal state
   # This heuristic relaxes the constraint that Alex must make exactly 4 diagonal jumps, as it allows Alex to jump to any of the eight adjacent trampolines
   # It is admissible because it never overestimates the cost to reach the goal, as the shortest path to the goal is always a straight line
   # The heuristic is consistent because moving a jump from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved jump is a diagonal one), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
   return h


print(a_star())
