
import heapq
from copy import deepcopy


def a_star():
   # Define the initial state of the puzzle, as a 2d tuple
   initial_state = ((36, 16, 48), (86, '_', 13), (89, 31, 37))
   num_rows = 3
   num_cols = 3
   # The goal state is when all tiles are in descending order, with the largest number in the top left corner, and the empty spot is in the bottom right corner
   goal_state = ((89, 86, 48), (37, 36, 31), (16, 13, '_'))


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes swapping the empty spot with any of the 4 neighboring tiles
       # First, get the coordinates of the empty spot
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
                   # The heuristic is the sum of the Manhattan distances of each tile from its position in the goal state
                   h = heuristic(new_state, goal_state)
                   # The number on the tile that the empty spot is swapped with at each turn must be added to the actions
                   heapq.heappush(queue, (g + h, g + 1, actions + [int(state[new_row][new_col])], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances of each tile from its position in the goal state
   # The heuristic relaxes the constraint that only the empty spot can be moved, ie it presumes any tile can be moved directly to its goal position
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of moving the empty spot to an adjacent tile is 1, which is always greater than or equal to the decrease in the Manhattan distance of the tile moved to the empty spot
   # Also the cost of the goal state is 0, as all tiles are in their goal positions
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != '_':
               goal_coord = [(x, y) for x, row in enumerate(goal) for y, element in enumerate(row) if element == state[i][j]][0]
               h += abs(i - goal_coord[0]) + abs(j - goal_coord[1])
   return h


print(a_star())
