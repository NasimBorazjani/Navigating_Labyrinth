
import heapq
from copy import deepcopy


def a_star():
   # Define the initial state of the puzzle, as a 2d tuple
   initial_state = ((71, 42, 22, 90), (79, 78, '_', 68), (25, 58, 28, 12))
   num_rows = 3
   num_cols = 4
   # The goal state is the sorted version of the initial state, in descending order, with the empty spot at the end
   goal_state = tuple(sorted([cell for row in initial_state for cell in row if cell != '_'], reverse=True) + ['_'])
   goal_state = tuple(tuple(goal_state[i:i+num_cols]) for i in range(0, len(goal_state), num_cols))


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes swapping the empty spot with any of the 4 neighboring tiles
       # First, get the coordinates of the empty spot
       empty_spot_coord = [(i, j) for i, row in enumerate(state) for j, cell in enumerate(row) if cell == '_'][0]
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = empty_spot_coord[0] + d_row, empty_spot_coord[1] + d_col
           # Check if the new coordinate is valid, ie if the new tile is within the bounds of the puzzle
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               # Swap the empty spot with the new tile
               new_state[empty_spot_coord[0]][empty_spot_coord[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_spot_coord[0]][empty_spot_coord[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic is the number of misplaced tiles in the current state
                   h = heuristic(new_state, goal_state)
                   # The action is the number on the tile that was swapped with the empty spot
                   heapq.heappush(queue, (g + h, g + 1, actions + [new_state[empty_spot_coord[0]][empty_spot_coord[1]]], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the count of misplaced tiles in the current state
   # This heuristic relaxes the constraint that only the empty spot can be moved
   # It is admissible because it never overestimates the cost to reach the goal, as each misplaced tile must be moved at least once
   # It's consistent because moving a tile reduces the heuristic cost of the successor node by a max of 1 (if the moved tile is placed in its correct position), which is equal to the cost of reaching the successor node
   # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
   # And the cost of the goal state is 0, as all tiles will be in their correct positions
   return sum(s != g for s, g in zip(state, goal))


print(a_star())
