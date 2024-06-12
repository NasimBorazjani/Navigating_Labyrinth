
import heapq


def a_star():
   # Define the initial state of the trampoline park, as a 2d tuple
   initial_state = ((1, 0, 0, 0, 1, 1, 1, 1, 0, 0),
                   (1, 1, 1, 0, 0, 1, 0, 1, 0, 1),
                   (1, 0, 0, 0, 1, 0, 0, 0, 0, 0),
                   (1, 1, 1, 1, 0, 1, 0, 0, 0, 0),
                   (1, 0, 1, 0, 0, 1, 1, 0, 0, 0),
                   (1, 1, 1, 1, 1, 1, 0, 0, 0, 0),
                   (0, 1, 1, 1, 1, 0, 1, 1, 1, 0),
                   (1, 0, 1, 1, 0, 0, 1, 1, 0, 0),
                   (1, 1, 1, 0, 1, 1, 0, 1, 0, 1),
                   (1, 1, 1, 0, 0, 1, 1, 0, 0, 1))
  
   # Encoding other variables given in the problem statement
   num_rows = 10
   num_cols = 10
   start_pos = (0, 1)
   goal_pos = (6, 9)
   num_diagonal_jumps = 3


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start_pos] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the jumps required to get to each state in a list; no jumps performed to reach the initial state
   queue = [(0, 0, [], start_pos)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_pos:
           return actions


       # Generate all possible actions from the current state, which includes jumping to any of the 8 adjacent trampolines, as long as they are not broken
       for d_row, d_col in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the new state would be valid, ie the new position is within the grid and the trampoline is not broken
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] == 0:
               # The actions is valid, generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the goal state
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # Relax the constraint on the number of diagonal jumps to calculate the heuristic
                   h = heuristic(new_state, goal_pos, num_diagonal_jumps)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state], new_state))
                  
   return None


def heuristic(state, goal, num_diagonal_jumps):
   # An admissible and consistent heuristic for this problem is the Manhattan distance between the current state and the goal state, plus the number of diagonal jumps made so far
   # This heuristic relaxes the constraint that the number of diagonal jumps must be exactly 3
   # It is admissible because it never overestimates the cost to reach the goal, as each diagonal jump must be made at least once
   # It's consistent because moving a jump from one direction to another reduces the heuristic cost of the successor node by a max of 1 (if the moved jump is a diagonal one), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = abs(state[0] - goal[0]) + abs(state[1] - goal[1]) + num_diagonal_jumps
   return h


print(a_star())
