
import heapq


def initialize():
   # Define the initial state of the trampoline park as a 2d tuple
   initial_state = ((0, 1, 1, 1, 0, 0, 0, 1, 0),
                   (0, 1, 1, 0, 1, 0, 1, 0, 0),
                   (1, 0, 1, 1, 1, 1, 0, 0, 1),
                   (0, 0, 1, 0, 1, 1, 1, 0, 1),
                   (1, 0, 1, 1, 0, 1, 1, 0, 1),
                   (1, 1, 1, 1, 1, 0, 0, 0, 0),
                   (0, 0, 1, 1, 1, 0, 0, 0, 1),
                   (1, 1, 1, 0, 0, 0, 0, 1, 1),
                   (1, 1, 1, 0, 0, 0, 0, 1, 1))
   num_rows = 9
   num_cols = 9
   start_pos = (0, 8)
   goal_pos = (8, 3)
   # Create the set of the valid moves that could be made
   moves = {(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)}


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, start_pos, goal_pos, moves, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, start_pos, goal_pos, moves, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state[goal_pos[0]][goal_pos[1]] == 0:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 8 adjacent trampolines
       for move in moves:
           new_row, new_col = start_pos[0] + move[0], start_pos[1] + move[1]
           # Check if the new state would be valid, ie the new position is within the grid and the trampoline is functional
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and state[new_row][new_col] == 0:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[new_row][new_col] = 1
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_pos), new_cost, actions + [(new_row, new_col)], new_state))
   return None


def heuristic(state, goal_pos):
   # An admissible and consistent heuristic is the Manhattan distance from the current state to the goal state
   # This heuristic relaxes the constraint that Alex must make exactly 3 diagonal jumps, as it allows Alex to make more or less diagonal jumps
   # It is admissible because it never overestimates the cost to reach the goal, as each diagonal jump must be made at least once
   # It's consistent because moving to a functional trampoline reduces the heuristic cost of the successor node by a max of 1 (if the moved trampoline is closer to the goal), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] == 0:
               h += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
   return h


print(a_star())
