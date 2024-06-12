
import heapq


def initialize():
   # Define the initial state and the goal state of the problem, represented as tuples
   initial_state = (8, 1)
   goal_state = (0, 5)
  
   # Encoding other variables given in the problem statement
   num_rows = 9
   num_cols = 9
   park_map = [[0, 0, 1, 0, 0, 0, 0, 0, 1],
               [0, 1, 0, 1, 1, 0, 0, 0, 0],
               [1, 1, 1, 1, 1, 1, 1, 1, 0],
               [1, 1, 0, 1, 1, 0, 0, 0, 0],
               [1, 0, 1, 0, 1, 0, 1, 1, 1],
               [1, 0, 1, 0, 0, 0, 1, 0, 1],
               [0, 1, 0, 0, 0, 1, 1, 0, 1],
               [0, 0, 1, 0, 1, 1, 1, 1, 1],
               [1, 0, 0, 1, 1, 0, 0, 1, 1]]
   diagonal_jumps = 3


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[(initial_state, diagonal_jumps)] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], (initial_state, diagonal_jumps))]
  
   return initial_state, goal_state, num_rows, num_cols, park_map, diagonal_jumps, visited_costs, queue
  
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial and goal state, dimensions of the park, park map, and number of diagonal jumps)
   initial_state, goal_state, num_rows, num_cols, park_map, diagonal_jumps, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, (state, diagonal_jumps_left) = heapq.heappop(queue)


       # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
       if state == goal_state and diagonal_jumps_left == 0:
           return actions


       # Generate all valid actions from the current state, which includes jumping to any of the 8 neighboring trampolines
       # Generate the coordinates of the neighboring trampolines
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the jump is valid, ie if the coordinate of the trampoline to jump to is a valid coordinate within the bounds of the park and the trampoline is not broken
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and park_map[new_row][new_col] == 0:
               # The jump is valid, generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of jumps made, as our objective is to minimize the number of jumps required to reach the goal state 
               new_cost = g + 1
               # If the jump is diagonal, decrement the number of diagonal jumps left
               if d_row != 0 and d_col != 0:
                   new_diagonal_jumps_left = diagonal_jumps_left - 1
               else:
                   new_diagonal_jumps_left = diagonal_jumps_left
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if (new_state, new_diagonal_jumps_left) not in visited_costs or new_cost < visited_costs[(new_state, new_diagonal_jumps_left)]:
                   visited_costs[(new_state, new_diagonal_jumps_left)] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [new_state], (new_state, new_diagonal_jumps_left)))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance (the shortest path) of the current position from the goal position
   # The heuristic relaxes the constraint that Alex must make exactly 3 diagonal jumps and presumes Alex can move to the goal position by jumping to any of the neighboring trampolines
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if Alex moves toward the goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of the current position from the goal position would be 0 in the goal state.
   h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
   return h


print(a_star())
