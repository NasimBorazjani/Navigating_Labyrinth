
import heapq
from collections import deque


def a_star():
   # Define the initial state of the puzzle, as a 2d tuple of numbers in the puzzle
   initial_state = ((100, 96, 93, 82, 6, 19), (68, 53, 50, 9, '_', 24), (16, 15, 48, 10, 76, 74))
   num_rows = 3
   num_cols = 6
   # The goal state is the puzzle sorted in descending order
   goal_state = tuple(tuple(range(100, 100 - num_cols, -1)) for _ in range(num_rows))
   # The last element of the last row of the goal state is the empty spot
   goal_state = goal_state[:-1] + (goal_state[-1][:-1] + ('_',),)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes swapping the empty spot with any of the 4 neighboring tiles
       # First, find the coordinates of the empty spot
       empty_spot_coord = [(i, j) for i, row in enumerate(state) for j, element in enumerate(row) if element == '_'][0]
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
                   heapq.heappush(queue, (g + h, g + 1, actions + [new_state[new_row][new_col]], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the count of misplaced tiles in the current state
   # This heuristic relaxes the constraint that only the empty spot can be moved
   # It is admissible because it never overestimates the cost to reach the goal, as each misplaced tile must be moved at least once
   # It's consistent because moving a tile reduces the heuristic cost of the successor node by a max of 1 (if the moved tile is in its correct position in the goal state), which is equal to the cost of reaching the successor node
   # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
   # And the cost of the goal state is 0, as all tiles are in their correct positions
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] != goal[i][j]:
               h += 1
   return h


print(a_star())
