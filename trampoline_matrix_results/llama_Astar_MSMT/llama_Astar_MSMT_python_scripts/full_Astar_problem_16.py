
import heapq


def initialize():
   # Define the initial state of the trampolines as a 2d tuple
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
   dest_pos = (6, 9)
   max_diagonal_jumps = 3


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, start_pos, dest_pos, max_diagonal_jumps, visited_costs, queue
  
def a_star():
  
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the trampolines, dimensions of the park, start and destination positions, and max diagonal jumps)
   initial_state, num_rows, num_cols, start_pos, dest_pos, max_diagonal_jumps, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state[start_pos[0]][start_pos[1]] == dest_pos[0] and state[dest_pos[0]][dest_pos[1]] == 0:
           return actions


       # Generate all possible actions from the current state, which includes jumping to any of the 8 adjacent trampolines, as long as they are not broken and the number of diagonal jumps does not exceed the maximum
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
           new_pos = (start_pos[0] + d_row, start_pos[1] + d_col)
           if 0 <= new_pos[0] < num_rows and 0 <= new_pos[1] < num_cols and state[new_pos[0]][new_pos[1]] == 0 and (abs(new_pos[0] - start_pos[0]) + abs(new_pos[1] - start_pos[1])) - 1 <= max_diagonal_jumps:
               # The actions is valid, generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[start_pos[0]][start_pos[1]] = 1
               new_state[new_pos[0]][new_pos[1]] = 0
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of jumps made, as our objective is to minimize the number of jumps required to reach the goal state 
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, dest_pos), new_cost, actions + [new_pos], new_state))
                  
   return None


def heuristic(state, dest_pos):
   # An admissible and consistent heuristic is the Manhattan distance from the current position to the destination
   # This heuristic relaxes the constraint that Alex must make exactly 3 diagonal jumps
   # It is admissible because it never overestimates the cost to reach the goal, as each diagonal jump must be made at least once
   # It's consistent because moving to a neighboring position reduces the heuristic cost of the successor node by a max of 1 (if the moved position is closer to the destination), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = abs(state[dest_pos[0]] - dest_pos[1]) + abs(state[dest_pos[0]] - dest_pos[1])
   return h


print(a_star())
