
import heapq


def initialize():
   # Define the initial state of the grid as a 2d tuple
   initial_state = ((0, 1, 1, 1, 0, 0, 1, 0, 0, 1),
                   (1, 0, 0, 0, 0, 0, 0, 0, 1, 1),
                   (1, 1, 0, 0, 0, 0, 0, 0, 1, 1),
                   (0, 1, 0, 1, 1, 1, 1, 0, 1, 1),
                   (0, 0, 1, 0, 1, 1, 1, 0, 0, 0),
                   (1, 1, 0, 1, 1, 0, 1, 0, 0, 0),
                   (1, 0, 1, 0, 0, 0, 1, 0, 0, 0),
                   (0, 0, 0, 0, 0, 1, 1, 0, 0, 0),
                   (0, 1, 0, 0, 1, 1, 1, 1, 0, 0),
                   (1, 0, 0, 0, 1, 1, 1, 1, 0, 0))
   num_rows = 10
   num_cols = 10
   start_pos = (0, 4)
   goal_pos = (9, 8)
  
   visited_costs = {}
   visited_costs[start_pos] = 0


   queue = [(0, 0, [], start_pos)]
  
   return initial_state, num_rows, num_cols, start_pos, goal_pos, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, start_pos, goal_pos, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_pos:
           return actions


       # Generate all possible actions from the current state, which involves jumping to any of the 8 adjacent trampolines
       for row_delta, col_delta in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
           new_state = (state[0] + row_delta, state[1] + col_delta)
           # Check if the new state is valid, ie within the grid and not a broken trampoline
           if (0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and
               initial_state[new_state[0]][new_state[1]] != 1):
               # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required
               new_cost = g + 1


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, goal_pos)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance between the current state and the goal state
   # This heuristic relaxes the constraint that Alex must make exactly 3 diagonal jumps, as the heuristic estimate for the goal state is 0, as the distance of each tile from its goal position would be 0 in the goal state
   h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
   return h


print(a_star())
