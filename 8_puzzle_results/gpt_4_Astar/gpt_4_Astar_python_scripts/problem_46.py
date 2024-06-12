
import heapq
from copy import deepcopy


def a_star():
   # Define the initial state of the puzzle, as a 2d tuple
   initial_state = ((85, '_', 61, 100), (45, 77, 10, 91), (83, 57, 95, 39))
   num_rows = 3
   num_cols = 4
   # The goal state is the sorted list of all the numbers in the puzzle in descending order, with the empty spot at the end
   goal_state = tuple(tuple(sorted([cell for row in initial_state for cell in row if cell != '_'], reverse=True)[i*num_cols:(i+1)*num_cols] for i in range(num_rows)))
   # Get the coordinates of the empty spot in the initial state
   empty_spot = [(i, j) for i in range(num_rows) for j in range(num_cols) if initial_state[i][j] == '_'][0]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state, empty_spot)]


   while queue:
       _, g, actions, state, empty_spot = heapq.heappop(queue)


       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes moving any of the 4 neighboring tiles to the empty spot
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = empty_spot[0] + d_row, empty_spot[1] + d_col
           # Check if the new coordinate is valid, ie if the new tile is within the bounds of the puzzle
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               # Swap the tile with the empty spot
               new_state[empty_spot[0]][empty_spot[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_spot[0]][empty_spot[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The tile that was moved to the empty spot must be added to the actions
                   heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [new_state[empty_spot[0]][empty_spot[1]]], new_state, (new_row, new_col)))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances from each tile in its current position to its position in the goal state
   # This heuristic relaxes the constraint that only the tile adjacent to the empty spot can be moved
   # It is admissible because it never overestimates the cost to reach the goal, as each tile must be moved at least once for each unit of Manhattan distance
   # It's consistent because moving a tile from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved tile's Manhattan distance to its goal position is reduced by 1), which is equal to the cost of reaching the successor node
   # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
   # And the cost of the goal state is 0, as all tiles will be in their goal positions
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           goal_i, goal_j = [(x, y) for x in range(len(goal)) for y in range(len(goal[0])) if goal[x][y] == state[i][j]][0]
           h += abs(i - goal_i) + abs(j - goal_j)
   return h


print(a_star())
