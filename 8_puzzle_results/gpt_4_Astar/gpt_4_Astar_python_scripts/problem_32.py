
import heapq
from collections import deque


def a_star():
   # Define the initial state of the puzzle, as a 2d tuple
   initial_state = ((69, 56, 8, 67), (15, 47, 44, 30), (73, '_', 24, 63))
   num_rows = 3
   num_cols = 4
   # The goal state is the sorted list of all the numbers in the puzzle in descending order, with the empty spot at the end
   goal_state = tuple(tuple(sorted([cell for row in initial_state for cell in row if cell != '_'], reverse=True)[i*num_cols:(i+1)*num_cols] for i in range(num_rows)))
   # The empty spot is represented as '_'
   empty_spot = '_'


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken to reach the goal state
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes moving the empty spot to any of the 4 neighboring cells
       # First, find the coordinates of the empty spot in the current state
       empty_spot_coord = [(i, j) for i, row in enumerate(state) for j, cell in enumerate(row) if cell == empty_spot][0]
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = empty_spot_coord[0] + d_row, empty_spot_coord[1] + d_col
           # Check if the new coordinate is valid, ie if the new cell is within the bounds of the puzzle
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               # Swap the empty spot with the cell at the new coordinate
               new_state[empty_spot_coord[0]][empty_spot_coord[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_spot_coord[0]][empty_spot_coord[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic is the sum of the Manhattan distances of each cell from its position in the goal state
                   h = heuristic(new_state, goal_state)
                   # The action taken is the number on the tile that the empty spot is swapped with
                   heapq.heappush(queue, (g + h, g + 1, actions + [int(new_state[empty_spot_coord[0]][empty_spot_coord[1]])], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances of each cell from its position in the goal state
   # The heuristic relaxes the constraint that only the empty spot can be moved, and that the tiles can only be moved to the empty spot
   # It is admissible because it never overestimates the cost to reach the goal, as each tile must be moved at least the Manhattan distance to reach its position in the goal state
   # It's consistent because moving a tile reduces the Manhattan distance of that tile to its goal position by 1 (equal to the cost of reaching the successor node), and does not change the Manhattan distance of any other tile. Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
   # And the cost of the goal state is 0, as all tiles are in their goal positions
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] != '_':
               goal_coord = [(x, y) for x, row in enumerate(goal) for y, cell in enumerate(row) if cell == state[i][j]][0]
               h += abs(i - goal_coord[0]) + abs(j - goal_coord[1])
   return h


print(a_star())
