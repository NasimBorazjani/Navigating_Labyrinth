
import heapq
from collections import deque


def a_star():
   # Define the initial state of the puzzle, as a 2d tuple
   initial_state = ((94, 93, 84, 27, 6), (55, 18, 91, 82, 8), (19, 32, 37, 30, '_'))
   num_rows = 3
   num_cols = 5
   # The goal state is when all tiles are in descending order, with the largest number in the top left corner, and the empty spot is in the bottom right corner
   goal_state = ((94, 93, 91, 84, 82), (55, 37, 32, 30, 27), (19, 18, 8, 6, '_'))


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes moving the empty spot to any of the 4 neighboring positions
       # First, find the position of the empty spot
       empty_spot_coord = [(i, j) for i, row in enumerate(state) for j, element in enumerate(row) if element == '_'][0]
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = empty_spot_coord[0] + d_row, empty_spot_coord[1] + d_col
           # Check if the new position of the empty spot is valid, ie if it is within the bounds of the puzzle
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               # Swap the empty spot with the tile at the new position
               new_state[empty_spot_coord[0]][empty_spot_coord[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_spot_coord[0]][empty_spot_coord[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the goal state
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The action taken is the number on the tile that the empty spot is swapped with
                   heapq.heappush(queue, (g + heuristic(new_state, goal_state), g + 1, actions + [int(state[new_row][new_col])], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances from each tile in its current position to its position in the goal state
   # This heuristic relaxes the constraint that only the empty spot can be moved, and assumes that each tile can be moved to its goal position independently of the others
   # Thus the heuristic never overestimates the cost to reach the goal, as each tile must be moved at least the Manhattan distance to reach its goal position, making it admissible
   # The heuristic is consistent because moving the empty spot to a new position reduces the Manhattan distance of the tile at the new position to its goal position by 1 (equal to the cost of reaching the successor node), and does not increase the Manhattan distance of any other tile. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   # And the cost of the goal state is 0, as all tiles are in their goal positions
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] != '_':
               goal_coord = [(k, l) for k, row in enumerate(goal) for l, element in enumerate(row) if element == state[i][j]][0]
               h += abs(i - goal_coord[0]) + abs(j - goal_coord[1])
   return h


print(a_star())
