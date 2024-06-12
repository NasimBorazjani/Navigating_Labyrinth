
import heapq


def a_star():
   # Define the initial state of the trampoline park, as a 2d tuple
   initial_state = ((0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1),
                   (1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0),
                   (0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0),
                   (1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1),
                   (1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0),
                   (1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1),
                   (0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0),
                   (0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1),
                   (1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0),
                   (0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1),
                   (1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0))
  
   # Encoding other variables given in the problem statement
   num_rows = 11
   num_cols = 11
   start_pos = (10, 10)
   goal_pos = (0, 4)
   num_diag_jumps = 3


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


       # Generate all possible actions from the current state, which includes jumping to any of the 8 adjacent trampolines, as long as they are not broken and the number of diagonal jumps is not exceeded
       for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]:
           new_pos = (start_pos[0] + d_row, start_pos[1] + d_col)
           # Check if the new position is valid, ie if the new position is within the bounds of the park and the trampoline is not broken and the number of diagonal jumps is not exceeded
           if (0 <= new_pos[0] < num_rows and 0 <= new_pos[1] < num_cols and state[new_pos[0]][new_pos[1]] == 0 and (abs(d_row) == abs(d_col)) == (len(actions) < num_diag_jumps):
               # The actions is valid, generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[new_pos[0]][new_pos[1]] = 1
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of jumps made, as our objective is to minimize the number of jumps required to reach the goal state
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_pos), new_cost, actions + [new_pos], new_state))
                  
   return None


def heuristic(state, goal_pos):
   # An admissible and consistent heuristic is the Manhattan distance from the current state to the goal state
   # This heuristic relaxes the constraint that Alex must make exactly 3 diagonal jumps, as it allows Alex to jump to any of the 8 adjacent trampolines
   # It is admissible because it never overestimates the cost to reach the goal, as each diagonal jump must be made at least once
   # It's consistent because moving a jump from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved jump is diagonal), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] == 0:
               h += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
   return h


print(a_star())
