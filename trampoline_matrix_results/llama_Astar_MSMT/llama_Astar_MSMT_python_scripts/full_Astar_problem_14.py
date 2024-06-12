
import heapq


def initialize():
   # Define the initial state of the grid as a 2d tuple
   initial_state = ((1, 0, 0, 0, 0, 1, 1, 0, 0),
                   (1, 0, 0, 1, 0, 1, 1, 0, 0),
                   (0, 0, 1, 0, 1, 0, 0, 0, 1),
                   (1, 0, 0, 1, 1, 0, 0, 0, 0),
                   (0, 0, 0, 0, 1, 1, 1, 0, 1),
                   (0, 0, 0, 1, 1, 0, 1, 1, 0),
                   (0, 1, 1, 0, 1, 1, 0, 1, 0),
                   (0, 1, 0, 0, 1, 0, 0, 0, 0),
                   (0, 0, 0, 0, 1, 0, 1, 1, 0))
   num_rows = 9
   num_cols = 9
   start = (0, 7)
   goal = (7, 0)
   # Create the set of the valid moves that could be made by Alex
   moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, start, goal, moves, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, start, goal, moves, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if start == goal:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 8 adjacent trampolines
       for move in moves:
           new_row, new_col = start[0] + move[0], start[1] + move[1]
           # Check if the new state would be valid, ie the new position is within the grid and the trampoline is not broken
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and state[new_row][new_col] == 0:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[new_row][new_col] = 1
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal), new_cost, actions + [(new_row, new_col)], new_state))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance between the current position and the goal position
   # This heuristic relaxes the constraint that Alex must make exactly 3 diagonal jumps
   # It is admissible because it never overestimates the cost to reach the goal, as each diagonal jump must be made at least once
   # It's consistent because moving to a closer trampoline reduces the heuristic cost of the successor node by a max of 1 (if the moved trampoline is closer to the goal), which is equal to the cost of reaching the successor node
   h = abs(start[0] - goal[0]) + abs(start[1] - goal[1])
   return h


print(a_star())
