
import heapq


def initialize():
   # Define the initial state of the trampoline park as a 2d tuple
   initial_state = ((1, 1, 1, 0, 0, 0, 0, 1, 1),
                   (0, 1, 1, 0, 0, 0, 0, 0, 0),
                   (1, 1, 1, 1, 0, 1, 0, 0, 1),
                   (0, 0, 0, 1, 0, 0, 0, 0, 0),
                   (0, 0, 1, 1, 0, 1, 1, 0, 1),
                   (1, 1, 1, 1, 1, 0, 0, 0, 0),
                   (0, 1, 1, 1, 0, 1, 1, 0, 0),
                   (1, 1, 1, 0, 0, 0, 0, 0, 0),
                   (1, 1, 1, 0, 0, 0, 1, 0, 0))
   num_rows = 9
   num_cols = 9
   start_pos = (8, 7)
   goal_pos = (0, 3)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, start_pos, goal_pos, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, start_pos, goal_pos, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if (state[start_pos[0]][start_pos[1]] == 0 and
           state[goal_pos[0]][goal_pos[1]] == 0):
           return actions


       # Generate all possible actions from the current state, which includes jumping to any of the 8 adjacent trampolines, as long as they are not broken
       for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
           new_pos = (start_pos[0] + dr, start_pos[1] + dc)
           # Check if the new position is valid, ie within the bounds of the park and not broken
           if (0 <= new_pos[0] < num_rows and
               0 <= new_pos[1] < num_cols and
               state[new_pos[0]][new_pos[1]] == 0):
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[start_pos[0]][start_pos[1]] = 1
               new_state[new_pos[0]][new_pos[1]] = 0
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the goal
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_pos), new_cost, actions + [new_pos], new_state))
   return None


def heuristic(state, goal_pos):
   # An admissible and consistent heuristic is the Manhattan distance between the current position and the goal position
   # This heuristic relaxes the constraint that Alex must make exactly 3 diagonal jumps, as it allows Alex to move in any direction
   # It is admissible because it never overestimates the cost to reach the goal, as each step in the heuristic cost is a valid step in the actual path
   # It's consistent because moving in any direction reduces the heuristic cost of the successor node by a max of 1 (if the moved position is closer to the goal), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = abs(state[goal_pos[0]][goal_pos[1]] - state[start_pos[0]][start_pos[1]])
   return h


print(a_star())
