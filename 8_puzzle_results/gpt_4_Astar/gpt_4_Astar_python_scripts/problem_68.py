
import heapq
from collections import deque


def a_star():
   # Define the initial state of the puzzle, as a 2d tuple of numbers and '_'
   initial_state = ((72, 92, '_', 78, 74), (70, 67, 85, 75, 66), (48, 42, 32, 26, 50))
   num_rows = 3
   num_cols = 5
   # The goal state is the sorted list of numbers in the initial state, in descending order, with '_' at the end
   goal_state = tuple(tuple(sorted([cell for row in initial_state for cell in row if cell != '_'], reverse=True)[i*num_cols:(i+1)*num_cols]) for i in range(num_rows))
   goal_state = tuple(tuple(row + ('_',) if i == num_rows - 1 else row) for i, row in enumerate(goal_state))


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes moving the empty spot to any of the 4 neighboring cells
       # Get the coordinate of the empty spot
       empty_spot_coord = [(i, j) for i, row in enumerate(state) for j, cell in enumerate(row) if cell == '_'][0]
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = empty_spot_coord[0] + d_row, empty_spot_coord[1] + d_col
           # Check if the new coordinate is valid, ie if the new cell is within the bounds of the puzzle
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               # Swap the empty spot with the new cell
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
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances from each cell to its position in the goal state
   # This heuristic relaxes the constraint that only the empty spot can be moved
   # It is admissible because it never overestimates the cost to reach the goal, as each cell must be moved at least once
   # It's consistent because moving a cell from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved cell's position in the new state is closer to its position in the goal state than in the old state), which is equal to the cost of reaching the successor node
   # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
   # And the cost of the goal state is 0, as all cells will be in their goal positions
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] != '_':
               goal_coord = [(k, l) for k, row in enumerate(goal) for l, cell in enumerate(row) if cell == state[i][j]][0]
               h += abs(i - goal_coord[0]) + abs(j - goal_coord[1])
   return h


print(a_star())
