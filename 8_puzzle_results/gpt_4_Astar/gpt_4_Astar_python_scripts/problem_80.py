
import heapq
from collections import deque


def a_star():
   # Define the initial state of the puzzle, as a 2d tuple of numbers in the puzzle
   initial_state = ((97, 78, '_', 9, 67), (18, 65, 52, 27, 66), (38, 92, 50, 14, 6))
   num_rows = 3
   num_cols = 5
   # The goal state is when all tiles are in descending order, with the largest number in the top left corner, and the empty spot is in the bottom right corner
   goal_state = ((97, 92, 78, 67, 66), (65, 52, 50, 27, 18), (14, 9, 6, '_', '_'))


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes swapping the empty spot with any of the 4 neighboring tiles
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == '_':
                   for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                       new_row, new_col = i + d_row, j + d_col
                       # Check if the new state would be valid, ie the new tile must be within the bounds of the puzzle
                       if 0 <= new_row < num_rows and 0 <= new_col < num_cols and state[new_row][new_col] != '_':
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[i][j], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[i][j]
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the number of moves made, as the task is to minimize the number of moves required
                           new_cost = g + 1


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               # The heuristic is the number of misplaced tiles in the current state
                               h = heuristic(new_state, goal_state)
                               # The tile that the empty spot is swapped with is the tile at the new_row and new_col
                               heapq.heappush(queue, (g + h, g + 1, actions + [new_state[new_row][new_col]], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the count of misplaced tiles in the current state
   # This heuristic relaxes the constraint that only the empty spot can be moved
   # It is admissible because it never overestimates the cost to reach the goal, as each misplaced tile must be moved at least once
   # It's consistent because moving a tile reduces the heuristic cost of the successor node by a max of 1 (if the moved tile is misplaced in the current state but not in the successor state), which is equal to the cost of reaching the successor node
   # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
   # And the cost of the goal state is 0, as all tiles will be in their correct positions
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] != goal[i][j] and state[i][j] != '_':
               h += 1
   return h


print(a_star())
