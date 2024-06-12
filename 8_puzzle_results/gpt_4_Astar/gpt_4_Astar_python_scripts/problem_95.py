
import heapq
from collections import deque


def a_star():
   # Define the initial state of the puzzle, as a 2d tuple of numbers in the puzzle
   initial_state = ((92, 72, 91, 79, 62, 24), (93, 67, 65, 63, 83, 74), (41, 34, 29, 27, 58, '_'))
   num_rows = 3
   num_cols = 6
   # The goal state is the sorted list of numbers in the puzzle in descending order, with the empty spot at the end
   goal_state = tuple(tuple(sorted([cell for row in initial_state for cell in row if cell != '_'], reverse=True)[i*num_cols:(i+1)*num_cols]) for i in range(num_rows))
   # Get the coordinates of the empty spot in the initial state
   empty_spot = [(i, j) for i, row in enumerate(initial_state) for j, cell in enumerate(row) if cell == '_'][0]


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
                   # The heuristic is the sum of the Manhattan distances of each tile from its position in the goal state
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (g + h, g + 1, actions + [new_state[new_row][new_col]], new_state, (new_row, new_col)))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances of each tile from its position in the goal state
   # This heuristic relaxes the constraint that only the tile adjacent to the empty spot can be moved
   # It is admissible because it never overestimates the cost to reach the goal, as each tile must be moved at least the Manhattan distance to reach its goal position
   # It's consistent because moving a tile reduces the Manhattan distance of that tile by 1 (equal to the cost of reaching the successor node), and does not affect the Manhattan distance of the other tiles
   # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
   # And the cost of the goal state is 0, as all tiles are in their goal positions
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] != '_':
               goal_i, goal_j = [(x, y) for x, row in enumerate(goal) for y, cell in enumerate(row) if cell == state[i][j]][0]
               h += abs(i - goal_i) + abs(j - goal_j)
   return h


print(a_star())
