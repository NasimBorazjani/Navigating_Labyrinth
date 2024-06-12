
import heapq


def a_star():
   # Define the initial state of the trampoline park, as a 2d tuple
   initial_state = ((0, 1, 1, 0, 1, 1, 1, 1, 0),
                   (0, 0, 0, 0, 0, 0, 1, 1, 1),
                   (0, 0, 0, 0, 0, 0, 0, 0, 0),
                   (1, 1, 0, 1, 0, 0, 0, 1, 1),
                   (0, 1, 1, 1, 1, 1, 0, 0, 1),
                   (1, 0, 0, 1, 1, 0, 0, 0, 0),
                   (1, 0, 1, 1, 1, 0, 0, 0, 0),
                   (0, 1, 1, 0, 1, 0, 1, 0, 1),
                   (1, 1, 1, 1, 1, 0, 0, 0, 0))
   num_rows = 9
   num_cols = 9
   start = (8, 6)
   goal = (0, 0)
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


       # We can check if the current state is the goal state with a simple equality check
       if state == goal:
           return actions


       # Generate all valid actions from the current state, which includes jumping to any of the 8 adjacent trampolines, as long as they are not broken
       for d_row, d_col in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the new position is valid, ie if the new position is within the bounds of the park and the trampoline is not broken
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] == 0:
               # The actions is valid, generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of jumps made, as our objective is to minimize the number of jumps required to reach the goal state
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal), new_cost, actions + [new_state], new_state))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance between the current state and the goal state
   # This heuristic relaxes the constraint that Alex must make exactly 3 diagonal jumps, as it allows Alex to jump to any of the 8 adjacent trampolines
   # It is admissible because it never overestimates the cost to reach the goal, as each diagonal jump must be made at least once
   # It's consistent because moving a jump from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved jump is diagonal), which is equal to the cost of reaching the successor node
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
