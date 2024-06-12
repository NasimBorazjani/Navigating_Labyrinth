
import heapq


def a_star():
   # Define the initial state of the trampoline park, as a 12x12 2d list
   initial_state = [[1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1],
                   [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
                   [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
                   [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],
                   [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0],
                   [0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                   [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0],
                   [0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
                   [1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
                   [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0]]
  
   # Define the start and goal positions
   start = (11, 2)
   goal = (3, 10)
   num_rows = 12
   num_cols = 12


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the jumps required to get to each state in a list; no jumps performed to reach the initial state
   queue = [(0, 0, [], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal:
           return actions


       # Generate all possible actions from the current state, which includes jumping to any of the 8 adjacent trampolines, as long as they are not broken
       for row_offset, col_offset in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
           new_row, new_col = state[0] + row_offset, state[1] + col_offset
           # Check if the new state would be valid, ie the new position is within the grid and the trampoline is not broken
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] == 0:
               # Generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the goal state
               new_cost = g + 1


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal), new_cost, actions + [new_state], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the Manhattan distance between the current state and the goal state
   # This heuristic relaxes the constraint that Alex must make exactly 4 diagonal jumps, as it does not consider the number of diagonal jumps made
   # It is admissible because it never overestimates the cost to reach the goal, as the Manhattan distance is a lower bound on the actual cost
   # It's consistent because moving to a neighboring state in the grid increases the heuristic cost of the successor node by a max of 1 (if the moved position is on the same row or column as the goal), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
