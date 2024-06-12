
import heapq


def a_star():
   # Define the initial state of the trampoline park, as a 2d tuple
   initial_state = ((0, 1, 0, 0, 0, 1, 1, 0, 1, 0),
                   (0, 0, 0, 1, 0, 1, 1, 0, 0, 0),
                   (1, 1, 1, 0, 0, 1, 1, 0, 0, 1),
                   (1, 0, 0, 0, 0, 0, 0, 0, 0, 1),
                   (1, 1, 1, 0, 0, 0, 0, 0, 0, 1),
                   (0, 0, 0, 0, 1, 0, 0, 1, 1, 1),
                   (0, 0, 1, 1, 0, 1, 1, 1, 1, 0),
                   (0, 0, 1, 1, 1, 1, 0, 0, 1, 0),
                   (1, 0, 1, 1, 1, 1, 1, 0, 1, 1),
                   (1, 1, 1, 0, 0, 1, 1, 1, 1, 1))
  
   # Encoding other variables given in the problem statement
   num_rows = 10
   num_cols = 10
   start_pos = (1, 9)
   goal_pos = (5, 0)
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


       # Generate all valid actions from the current state, which includes jumping to any of the 8 adjacent trampolines, as long as they are not broken
       for d_row, d_col in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
           new_pos = (state[0] + d_row, state[1] + d_col)
           # Check if the new position is valid, ie if the new position is within the bounds of the park and the trampoline is not broken
           if (0 <= new_pos[0] < num_rows and 0 <= new_pos[1] < num_cols and initial_state[new_pos[0]][new_pos[1]] == 0):
               # The actions is valid, generate the new state
               new_state = new_pos
               # The cost so far is the number of jumps made, as our objective is to minimize the number of jumps required to reach the goal state
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_pos, num_diag_jumps), new_cost, actions + [new_state], new_state))
                  
   return None


def heuristic(state, goal, num_diag_jumps):
   # An admissible and consistent heuristic is the sum of the Manhattan distances (the shortest path) of each tile from its goal position
   # The heuristic relaxes the constraint that a tile can only be swapped with the empty spot and presumes we can move the tiles to their goal position by swapping them with any of the other tiles
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving a tile to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if the tile is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of each tile from its goal position would be 0 in the goal state.
   h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
   return h


print(a_star())
