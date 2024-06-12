
import heapq
from copy import deepcopy


def a_star():
   # Define the initial state of the puzzle, as a 2d tuple
   initial_state = ((94, 92, 77, 88, '_'), (82, 43, 76, 85, 87), (24, 66, 17, 79, 75))
   num_rows = 3
   num_cols = 5
   # The goal state is a descending order of the numbers in the initial state, with the empty spot at the end
   goal_state = tuple(tuple(sorted([cell for row in initial_state for cell in row if cell != '_'], reverse=True)[i*num_cols:(i+1)*num_cols]) for i in range(num_rows))
   # The empty spot is at the end of the goal state
   goal_empty_spot = (num_rows - 1, num_cols - 1)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes moving the empty spot to any of the 4 neighboring cells
       # First, find the coordinates of the empty spot in the current state
       empty_spot = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == '_'][0]
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = empty_spot[0] + d_row, empty_spot[1] + d_col
           # Check if the new coordinate is valid, ie if the new cell is within the bounds of the puzzle
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               # Swap the empty spot with the new cell
               new_state[empty_spot[0]][empty_spot[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_spot[0]][empty_spot[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic is the Manhattan distance from the empty spot to its position in the goal state
                   h = abs(empty_spot[0] - goal_empty_spot[0]) + abs(empty_spot[1] - goal_empty_spot[1])
                   heapq.heappush(queue, (g + h, g + 1, actions + [new_state[empty_spot[0]][empty_spot[1]]], new_state))
   return None


print(a_star())
