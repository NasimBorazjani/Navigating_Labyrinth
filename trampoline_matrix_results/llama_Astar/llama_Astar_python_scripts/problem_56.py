
import heapq


def a_star():
   # Define the initial state of the trampoline park, as a 2d tuple
   initial_state = ((0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0),
                   (1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1),
                   (0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0),
                   (1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0),
                   (0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0),
                   (0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0),
                   (0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0),
                   (0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0),
                   (1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1),
                   (0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0),
                   (0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1),
                   (1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0))
  
   # Encoding other variables given in the problem statement
   num_rows = 12
   num_cols = 12
   start_pos = (11, 7)
   goal_pos = (2, 0)
   num_diag_jumps = 4


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
       for row_diff in range(-1, 2):
           for col_diff in range(-1, 2):
               # Check if the new state would be valid, ie the trampoline is not broken and the number of diagonal jumps is not exceeded
               if (0 <= state[0] + row_diff < num_rows and 0 <= state[1] + col_diff < num_cols and
                   initial_state[state[0] + row_diff][state[1] + col_diff] == 0 and
                   (row_diff != col_diff or abs(row_diff) + abs(col_diff) == num_diag_jumps)):
                   # Generate the new state
                   new_state = (state[0] + row_diff, state[1] + col_diff)
                   # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the goal state
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_pos), new_cost, actions + [new_state], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance between the current state and the goal state
   # This heuristic relaxes the constraint that Alex must make exactly 4 diagonal jumps, as the heuristic estimate for the goal state is 0, as the distance of the goal state would be 0 in the goal state
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
