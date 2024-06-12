
import heapq
from copy import deepcopy


def a_star():
   # Define the initial state of the puzzle, as a 2d tuple
   initial_state = ((41, 36, 82), (29, 97, 43), ('_', 51, 61))
   num_rows = 3
   num_cols = 3
   # The goal state is when all tiles are in descending order, with the largest number in the top left corner, and the empty spot is in the bottom right corner
   goal_state = ((97, 82, 61), (51, 43, 41), (36, 29, '_'))


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes moving the empty spot to any of the 4 neighboring positions
       # First, find the position of the empty spot
       empty_spot = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == '_'][0]
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = empty_spot[0] + d_row, empty_spot[1] + d_col
           # Check if the new position of the empty spot is valid, ie if it is within the bounds of the puzzle
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               # Swap the empty spot with the tile at the new position
               new_state[empty_spot[0]][empty_spot[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_spot[0]][empty_spot[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The action taken is the number on the tile that the empty spot is swapped with
                   heapq.heappush(queue, (g + heuristic(new_state, goal_state), g + 1, actions + [new_state[empty_spot[0]][empty_spot[1]]], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances from each tile in its current position to its position in the goal state
   # This heuristic relaxes the constraint that only the empty spot can be moved, and assumes that each tile can be moved to its goal position independently of the others
   # Thus the heuristic never overestimates the cost to reach the goal, as each tile must be moved at least the Manhattan distance to reach its goal position, making it admissible
   # The heuristic is consistent because moving the empty spot to a new position reduces the Manhattan distance of the tile at the new position to its goal position by 1, which is equal to the cost of reaching the successor node
   # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
   # And the cost of the goal state is 0, as all tiles are in their goal positions
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] != '_':
               goal_position = [(x, y) for x in range(len(goal)) for y in range(len(goal[0])) if goal[x][y] == state[i][j]][0]
               h += abs(i - goal_position[0]) + abs(j - goal_position[1])
   return h


print(a_star())
