
import heapq
from collections import deque


def a_star():
   # Define the initial state of the puzzle, as a 2d tuple
   initial_state = ((81, 10, 54, '_'), (89, 77, 33, 29), (26, 44, 61, 18))
   # Define the goal state of the puzzle
   goal_state = ((89, 81, 77, 61), (54, 44, 33, 29), (26, 18, 10, '_'))
   num_rows = 3
   num_cols = 4


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes moving the empty spot to any of the 4 neighboring tiles
       # First, find the coordinates of the empty spot
       empty_spot_coord = [(i, j) for i, row in enumerate(state) for j, element in enumerate(row) if element == '_'][0]
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = empty_spot_coord[0] + d_row, empty_spot_coord[1] + d_col
           # Check if the new coordinate is valid, ie if the new tile is within the bounds of the puzzle
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               # Swap the empty spot with the tile at the new coordinate
               new_state[empty_spot_coord[0]][empty_spot_coord[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_spot_coord[0]][empty_spot_coord[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic is the number of misplaced tiles in the current state
                   h = heuristic(new_state, goal_state)
                   # The number on the tile that the empty spot is swapped with is added to the list of actions
                   heapq.heappush(queue, (g + h, g + 1, actions + [new_state[empty_spot_coord[0]][empty_spot_coord[1]]], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the count of misplaced tiles in the current state
   # This heuristic relaxes the constraint that only the empty spot can be moved
   # It is admissible because it never overestimates the cost to reach the goal, as each misplaced tile must be moved at least once
   # It's consistent because moving the empty spot reduces the heuristic cost of the successor node by a max of 1 (if the moved tile is misplaced in the current state but not in the new one), which is equal to the cost of reaching the successor node
   # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
   # And the cost of the goal state is 0, as all tiles will be in their correct positions
   return sum(s != g for s_row, g_row in zip(state, goal) for s, g in zip(s_row, g_row) if s != '_')


print(a_star())