
import heapq
from collections import deque


def a_star():
   # Define the initial state of the puzzle, as a 2d tuple of the numbers on the tiles
   initial_state = ((89, 88, 62, 57, 79, 53), (92, 48, 61, 67, 78, 14), (32, 63, 27, '_', 19, 54))
   num_rows = 3
   num_cols = 6
   # The goal state is the tiles in descending order, with the empty spot in the bottom right corner
   goal_state = ((92, 89, 88, 79, 78, 67), (63, 62, 61, 57, 54, 53), (32, 27, 19, 14, '_', '_'))


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes moving the empty spot to any of the 4 neighboring tiles
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           # Get the coordinates of the empty spot
           empty_spot_coord = [(i, j) for i, row in enumerate(state) for j, element in enumerate(row) if element == '_'][0]
           new_row, new_col = empty_spot_coord[0] + d_row, empty_spot_coord[1] + d_col
           # Check if the new coordinate is valid, ie if the new tile is within the bounds of the puzzle
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               # Swap the empty spot with the new tile
               new_state[empty_spot_coord[0]][empty_spot_coord[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_spot_coord[0]][empty_spot_coord[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The number on the tile that the empty spot is swapped with is added to the list of actions
                   heapq.heappush(queue, (g + heuristic(new_state, goal_state), g + 1, actions + [new_state[empty_spot_coord[0]][empty_spot_coord[1]]], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances from each tile in the current state to its position in the goal state
   # This heuristic relaxes the constraint that only the empty spot can be moved
   # It is admissible because it never overestimates the cost to reach the goal, as each tile must be moved at least once
   # It's consistent because moving a tile from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved tile's position in the goal state is adjacent to the empty spot in the current state), which is equal to the cost of reaching the successor node
   # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
   # And the cost of the goal state is 0, as all tiles will be in their goal positions
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] != '_':
               goal_coord = [(k, l) for k, row in enumerate(goal) for l, element in enumerate(row) if element == state[i][j]][0]
               h += abs(i - goal_coord[0]) + abs(j - goal_coord[1])
   return h


print(a_star())
