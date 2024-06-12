
import heapq


def a_star():
   # Define the initial state of the trampoline park, as a 2d tuple
   initial_state = ((1, 1, 1, 0, 0, 0, 0, 1, 1, 0),
                   (0, 1, 1, 0, 1, 0, 1, 0, 1, 0),
                   (1, 1, 0, 0, 1, 0, 1, 0, 1, 1),
                   (1, 0, 0, 0, 0, 0, 1, 1, 0, 1),
                   (1, 0, 0, 0, 0, 0, 1, 1, 1, 1),
                   (1, 1, 0, 0, 0, 1, 1, 1, 0, 1),
                   (1, 1, 0, 0, 0, 0, 1, 0, 1, 0),
                   (0, 1, 0, 0, 0, 0, 0, 1, 1, 0),
                   (1, 0, 0, 1, 1, 1, 1, 0, 0, 0),
                   (0, 0, 1, 1, 1, 1, 0, 0, 1, 1))
   num_rows = 10
   num_cols = 10
   start_pos = (9, 0)
   goal_pos = (1, 5)
   # The maximum number of diagonal jumps allowed
   max_diagonal_jumps = 3


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start_pos] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], start_pos)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_pos:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 8 adjacent trampolines
       for row_offset, col_offset in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
           new_state = (state[0] + row_offset, state[1] + col_offset)
           # Check if the new state would be valid, ie the new state must be within the grid and the trampoline must not be broken
           if (0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and initial_state[new_state[0]][new_state[1]] == 0):
               # Calculate the number of diagonal jumps from the start position to the new state
               diagonal_jumps = abs(new_state[0] - start_pos[0]) + abs(new_state[1] - start_pos[1]) - 2 * abs(new_state[0] - state[0])
               # Check if the number of diagonal jumps is within the allowed limit
               if diagonal_jumps <= max_diagonal_jumps:
                   # The cost so far is the number of moves made, as the task is to minimize the number of moves required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(new_state, goal_pos)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Euclidean distance from the current state to the goal state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # It is consistent because moving to a neighboring state always increases the heuristic cost of the successor node by a value less than or equal to the cost of reaching the successor node
   return math.sqrt((state[0] - goal[0]) ** 2 + (state[1] - goal[1]) ** 2)


print(a_star())
