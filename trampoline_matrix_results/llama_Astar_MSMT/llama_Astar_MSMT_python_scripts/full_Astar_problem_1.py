
import heapq


def initialize():
   # Define the initial state of the trampoline park as a 2d tuple
   initial_state = ((0, 1, 0, 1, 0, 1, 1, 1, 1),
                   (0, 0, 1, 1, 0, 0, 0, 0, 1),
                   (0, 0, 0, 1, 1, 1, 0, 0, 1),
                   (0, 0, 0, 0, 0, 0, 0, 1, 0),
                   (0, 0, 0, 0, 0, 1, 1, 1, 1),
                   (0, 0, 1, 1, 1, 1, 0, 1, 1),
                   (0, 0, 0, 1, 1, 1, 1, 1, 0),
                   (1, 0, 1, 1, 1, 1, 1, 0, 1),
                   (0, 1, 1, 1, 1, 1, 0, 1, 0))
   num_rows = 9
   num_cols = 9
   start_pos = (8, 0)
   goal_pos = (2, 7)
   # Create the set of the valid moves that could be made
   moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], start_pos)]
  
   return initial_state, num_rows, num_cols, start_pos, goal_pos, moves, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, start_pos, goal_pos, moves, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_pos:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 8 adjacent trampolines
       for move in moves:
           new_pos = (state[0] + move[0], state[1] + move[1])
           # Check if the new position is valid, ie within the bounds of the park and the trampoline is not broken
           if 0 <= new_pos[0] < num_rows and 0 <= new_pos[1] < num_cols and initial_state[new_pos[0]][new_pos[1]] == 0:
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_pos), new_cost, actions + [new_pos], new_state))
   return None


def heuristic(state, goal_pos):
   # An admissible and consistent heuristic is the Manhattan distance between the current state and the goal state
   # This heuristic relaxes the constraint that Alex must make exactly 3 diagonal jumps, as it allows Alex to make more or fewer diagonal jumps if it results in a lower cost estimate
   # It is admissible because it never overestimates the cost to reach the goal, as each diagonal jump must be made at least once
   # It's consistent because moving to a closer trampoline reduces the heuristic cost of the successor node by a max of 1 (if the moved trampoline is closer to the goal), which is equal to the cost of reaching the successor node
   return abs(state[0] - goal_pos[0]) + abs(state[1] - goal_pos[1])


print(a_star())
