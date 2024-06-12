
import heapq
from collections import deque


def a_star():
   # Define the initial state of the puzzle, as a 2d tuple of numbers in the puzzle
   initial_state = ((54, 100, 91, 80, 56), (19, '_', 38, 74, 29), (14, 36, 44, 13, 10))
   num_rows = 3
   num_cols = 5
   # The goal state is the sorted list of numbers in the puzzle in descending order, with the empty spot at the end
   goal_state = tuple(tuple(sorted([cell for row in initial_state for cell in row if cell != '_'], reverse=True)[i*num_cols:(i+1)*num_cols]) for i in range(num_rows))
   # Get the initial coordinate of the empty spot
   initial_empty_spot = [(i, j) for i in range(num_rows) for j in range(num_cols) if initial_state[i][j] == '_'][0]


   visited_costs = {}
   visited_costs[(initial_state, initial_empty_spot)] = 0


   queue = [(0, 0, [], (initial_state, initial_empty_spot))]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Unpack the information encoded in each state
       state_puzzle, state_empty_spot = state


       # If the puzzle in the current state is the goal state, return the actions taken
       if state_puzzle == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes moving the empty spot to any of the 4 neighboring cells
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state_empty_spot[0] + d_row, state_empty_spot[1] + d_col
           # Check if the new coordinate is valid, ie if the new cell is within the bounds of the puzzle
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state_puzzle = [list(row[:]) for row in state_puzzle]
               # Swap the empty spot with the new cell
               new_state_puzzle[new_row][new_col], new_state_puzzle[state_empty_spot[0]][state_empty_spot[1]] = new_state_puzzle[state_empty_spot[0]][state_empty_spot[1]], new_state_puzzle[new_row][new_col]
               new_state_puzzle = tuple(tuple(row) for row in new_state_puzzle)
               new_state = (new_state_puzzle, (new_row, new_col))
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic is the sum of the Manhattan distances from each cell to its position in the goal state
                   h = heuristic(new_state_puzzle, goal_state)
                   # The number on the tile that the empty spot is swapped with is the number in the new cell
                   heapq.heappush(queue, (g + h, g + 1, actions + [new_state_puzzle[state_empty_spot[0]][state_empty_spot[1]]], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances from each cell to its position in the goal state
   # The heuristic relaxes the constraint that only the empty spot can be moved, ie It presumes we can move any cell directly to its goal position
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of moving the empty spot to an adjacent cell is 1, which is always greater than or equal to the decrease in the Manhattan distance of the cell swapped with the empty spot
   # Also the cost of the goal state is 0, as all cells are in their goal positions
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] != '_':
               goal_i, goal_j = [(k, l) for k in range(len(goal)) for l in range(len(goal[0])) if goal[k][l] == state[i][j]][0]
               h += abs(i - goal_i) + abs(j - goal_j)
   return h


print(a_star())
