
import heapq


def initialize():
   # Define the initial state of the grid as a 2d tuple
   initial_state = ((0, 0, 1, 0, 1, 1, 0, 0, 0),
                   (0, 0, 0, 1, 1, 1, 0, 1, 1),
                   (0, 1, 0, 0, 0, 0, 1, 0, 1),
                   (0, 1, 1, 1, 0, 0, 1, 1, 0),
                   (0, 1, 1, 1, 1, 0, 0, 1, 1),
                   (1, 0, 1, 1, 0, 1, 0, 0, 0),
                   (0, 1, 1, 1, 1, 0, 0, 0, 0),
                   (1, 1, 0, 1, 1, 0, 1, 0, 0),
                   (0, 1, 1, 1, 1, 1, 0, 0, 0))
   num_rows = 9
   num_cols = 9
   start_pos = (1, 0)
   goal_pos = (5, 8)
   # Create the set of the valid numbers that could be in the grid
   numbers = set(range(29, 54))


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, start_pos, goal_pos, numbers, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, start_pos, goal_pos, numbers, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state[goal_pos[0]][goal_pos[1]] == 0:
           return actions


       # Generate all possible actions from the current state, which includes jumping to any of the 8 adjacent trampolines
       # Generate the coordinates of the adjacent trampolines
       for d_row, d_col in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
           new_pos = (start_pos[0] + d_row, start_pos[1] + d_col)
           # Check if the new position is valid, ie if the new position is within the bounds of the grid and the trampoline is functional
           if 0 <= new_pos[0] < num_rows and 0 <= new_pos[1] < num_cols and state[new_pos[0]][new_pos[1]] == 0:
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
   # An admissible and consistent heuristic is the Manhattan distance from the current position to the goal position
   # The heuristic relaxes the constraint that Alex must make exactly 3 diagonal jumps
   # It is admissible because it never overestimates the cost to reach the goal, as each diagonal jump must be made at least once
   # It's consistent because moving a diagonal jump reduces the heuristic cost of the successor node by a max of 1 (if the moved position is diagonal), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = abs(goal_pos[0] - start_pos[0]) + abs(goal_pos[1] - start_pos[1])
   return h


print(a_star())
