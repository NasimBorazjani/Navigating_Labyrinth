
import heapq
from collections import deque


def a_star():
   # Define the initial state of the puzzle, as a 2d tuple of the numbers on the tiles
   initial_state = ((60, 66, 46, 8, 36), (81, '_', 88, 70, 24), (20, 17, 6, 62, 28))
   # Define the goal state of the puzzle
   goal_state = ((88, 81, 70, 66, 62), (60, 46, 36, 28, 24), (20, 17, 8, 6, '_'))
   num_rows = 3
   num_cols = 5


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes moving the empty tile to any of the 4 neighboring tiles
       # First, find the coordinates of the empty tile
       empty_tile_coord = [(i, j) for i, row in enumerate(state) for j, tile in enumerate(row) if tile == '_'][0]
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = empty_tile_coord[0] + d_row, empty_tile_coord[1] + d_col
           # Check if the new coordinate is valid, ie if the new tile is within the bounds of the puzzle
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               # Swap the empty tile with the new tile
               new_state[empty_tile_coord[0]][empty_tile_coord[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_tile_coord[0]][empty_tile_coord[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The action is the number on the tile that the empty tile is swapped with
                   action = int(state[new_row][new_col])
                   heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [action], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances from each tile in its current position to its goal position
   # This heuristic relaxes the constraint that only the empty tile can be moved
   # It is admissible because it never overestimates the cost to reach the goal, as each tile must be moved at least once for each unit of Manhattan distance
   # It's consistent because moving a tile reduces the Manhattan distance of that tile by a max of 1 (if the move is toward the goal position), which is equal to the cost of reaching the successor node
   # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
   # And the cost of the goal state is 0, as all tiles will be in their goal positions
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] != '_':
               goal_i, goal_j = [(x, y) for x, row in enumerate(goal) for y, tile in enumerate(row) if tile == state[i][j]][0]
               h += abs(i - goal_i) + abs(j - goal_j)
   return h


print(a_star())
