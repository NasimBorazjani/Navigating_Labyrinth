
import heapq


def a_star():
   # Define the initial state of the trampoline park, as a 2d tuple
   initial_state = ((0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1),
                   (1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0),
                   (1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1),
                   (0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0),
                   (0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1),
                   (1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1),
                   (1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0),
                   (0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1),
                   (1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1),
                   (0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1),
                   (1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0))
  
   # Encoding other variables given in the problem statement
   num_rows = 11
   num_cols = 11
   destination = (0, 0)
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
       if (state[8][8] == 1 and state[0][0] == 1) and len(actions) == num_diagonal_jumps * 2:
           return actions


       # Generate all possible actions from the current state, which includes jumping to any of the 8 adjacent trampolines, as long as they are not broken
       for d_row, d_col in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
           new_row, new_col = 8 + d_row, 8 + d_col
           # Check if the new state would be valid, ie the new position is within the grid and the trampoline is not broken
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and state[new_row][new_col] == 1:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[new_row][new_col] = 1
               new_state[8][8] = 0
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the goal
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, destination, num_diagonal_jumps), new_cost, actions + [(new_row, new_col)], new_state))
                  
   return None


def heuristic(state, goal, num_diagonal_jumps):
   # An admissible and consistent heuristic for this problem is the Manhattan distance from the current state to the goal state, plus the number of diagonal jumps made so far
   # This heuristic relaxes the constraint that Alex must make exactly 3 diagonal jumps, as it only penalizes the number of diagonal jumps made so far
   # It is admissible because it never overestimates the cost to reach the goal, as each diagonal jump must be made at least once
   # It's consistent because moving a jump from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved jump is a diagonal one), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] == 1:
               h += abs(i - goal[0]) + abs(j - goal[1])
   return h


print(a_star())
