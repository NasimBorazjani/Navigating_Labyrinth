
import heapq


def a_star():
   # Define the initial state of the trampoline park, as a 2d tuple
   initial_state = ((1, 0, 1, 1, 0, 0, 0, 0, 0, 1),
                   (0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
                   (0, 1, 1, 0, 0, 1, 0, 0, 0, 1),
                   (0, 0, 1, 0, 1, 1, 0, 0, 1, 1),
                   (1, 0, 1, 1, 1, 0, 1, 0, 1, 1),
                   (1, 0, 1, 1, 1, 1, 1, 1, 1, 1),
                   (0, 0, 0, 1, 1, 0, 0, 1, 1, 1),
                   (1, 0, 1, 1, 1, 0, 1, 1, 1, 0),
                   (1, 1, 1, 1, 1, 1, 0, 1, 1, 0),
                   (1, 1, 1, 0, 1, 0, 1, 0, 1, 1))
  
   # Encoding other variables given in the problem statement
   num_rows = 10
   num_cols = 10
   start_pos = (1, 9)
   goal_pos = (7, 1)
   num_diag_jumps = 3


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


       # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
       if state == goal_pos:
           return actions


       # Generate all valid actions from the current state, which includes moving to any of the 8 adjacent trampolines, as long as they are not broken and the number of diagonal jumps is not exceeded
       for d_row, d_col in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
           new_pos = (state[0] + d_row, state[1] + d_col)
           # Check if the new position is valid, ie if the new position is within the bounds of the park and the trampoline is not broken and the number of diagonal jumps is not exceeded
           if (0 <= new_pos[0] < num_rows and 0 <= new_pos[1] < num_cols and initial_state[new_pos[0]][new_pos[1]] == 0 and (abs(d_row) == abs(d_col)) == (len(actions) < num_diag_jumps):
               # The actions is valid, generate the new state
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_pos not in visited_costs or new_cost < visited_costs[new_pos]:
                   visited_costs[new_pos] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_pos, goal_pos), new_cost, actions + [new_pos], new_pos))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance between the current state and the goal state
   # This heuristic relaxes the constraint that Alex must make exactly 3 diagonal jumps, as the heuristic estimate for the goal state is 0, as the distance of the goal state would be 0 in the goal state.
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
