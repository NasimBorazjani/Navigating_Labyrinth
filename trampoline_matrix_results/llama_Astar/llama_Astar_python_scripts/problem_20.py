
import heapq


def a_star():
   # Define the initial state of the trampoline park, as a 2d tuple
   initial_state = ((0, 0, 1, 1, 1, 1, 0, 1, 1, 0),
                   (1, 0, 1, 1, 1, 1, 0, 1, 0, 0),
                   (0, 0, 0, 1, 1, 0, 0, 1, 1, 1),
                   (1, 0, 1, 1, 1, 0, 0, 0, 1, 1),
                   (0, 0, 1, 1, 1, 1, 0, 0, 1, 1),
                   (0, 0, 0, 1, 1, 0, 0, 0, 1, 1),
                   (0, 0, 0, 0, 1, 0, 0, 0, 1, 1),
                   (0, 0, 0, 0, 0, 0, 0, 0, 1, 1),
                   (1, 0, 1, 0, 0, 0, 0, 1, 0, 0),
                   (0, 0, 1, 0, 1, 1, 1, 1, 1, 1))
  
   # Define the goal state
   goal_state = (7, 6)
  
   # Define the number of rows and columns
   num_rows = 10
   num_cols = 10


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
       if state[goal_state[0]][goal_state[1]] == 0:
           return actions


       # Generate all possible actions from the current state, which includes jumping to any of the 8 adjacent trampolines, as long as they are not broken
       for row_offset in range(-1, 2):
           for col_offset in range(-1, 2):
               # Check if the new state would be valid, ie the new position is within the grid and there is no broken trampoline
               new_row, new_col = goal_state[0] + row_offset, goal_state[1] + col_offset
               if 0 <= new_row < num_rows and 0 <= new_col < num_cols and state[new_row][new_col] == 0:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   new_state[new_row][new_col] = 1
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the goal state
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(new_row, new_col)], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the Manhattan distance between the current position and the goal position
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as the cost of moving from one position to another is always the same
   # It is consistent because moving from one position to another always increases the heuristic cost of the successor node by a max of 1 (if the moved position is closer to the goal), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = abs(state[0][0] - goal[0]) + abs(state[0][1] - goal[1])
   return h


print(a_star())
