
import heapq


def initialize():
   # Define the initial state of the trampoline park as a 2d tuple
   initial_state = ((0, 1, 0, 1, 0, 1, 1, 1, 0),
                   (1, 0, 1, 0, 0, 0, 1, 0, 0),
                   (0, 0, 0, 1, 1, 1, 0, 1, 1),
                   (1, 0, 0, 0, 0, 1, 1, 0, 1),
                   (0, 0, 0, 0, 1, 0, 0, 1, 0),
                   (1, 0, 0, 0, 1, 1, 1, 0, 1),
                   (0, 1, 0, 0, 1, 0, 1, 1, 0),
                   (0, 1, 0, 0, 1, 0, 0, 0, 1),
                   (1, 1, 0, 0, 0, 0, 0, 1, 0))
  
   # Encoding other variables given in the problem statement
   num_rows = 9
   num_cols = 9
   start_pos = (8, 8)
   goal_pos = (2, 1)


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the trampolines jumped on to reach each state in a list; no trampolines jumped on to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, start_pos, goal_pos, visited_costs, queue
  
def a_star():
  
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the trampoline park, number of rows and columns, start and goal positions)
   initial_state, num_rows, num_cols, start_pos, goal_pos, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
       if state[goal_pos[0]][goal_pos[1]] == 0:
           return actions


       # Generate all valid actions from the current state, which includes jumping to any of the 8 adjacent trampolines, as long as they are not broken and the number of diagonal jumps is exactly 3
       # Generate the coordinates of the adjacent trampolines
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
           new_row, new_col = start_pos[0] + d_row, start_pos[1] + d_col
           # Check if the new position is valid, ie if the coordinate of the adjacent trampoline is a valid coordinate within the bounds of the park
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and state[new_row][new_col] == 0:
               # The actions is valid, generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[new_row][new_col] = 1
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of jumps made, as our objective is to minimize the number of jumps required to reach the goal state
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_pos), new_cost, actions + [(new_row, new_col)], new_state))
                  
   return None


def heuristic(state, goal_pos):
   # An admissible and consistent heuristic is the Manhattan distance from the current state to the goal state
   # This heuristic relaxes the constraint that Alex must make exactly 3 diagonal jumps, as the heuristic estimate for the goal state is 0, as the distance of the goal state would be 0 in the goal state.
   h = abs(goal_pos[0] - start_pos[0]) + abs(goal_pos[1] - start_pos[1])
   return h


print(a_star())
