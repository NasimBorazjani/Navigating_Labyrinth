
import heapq
from collections import deque


def a_star():
   # Define the initial state of the puzzle, as a 2d tuple of numbers in the puzzle
   initial_state = ((85, 96, 29, 80, 12), (60, '_', 76, 42, 82), (27, 89, 72, 37, 55))
   num_rows = 3
   num_cols = 5
   # The goal state is the sorted list of numbers in the puzzle in descending order, with the empty spot at the end
   goal_state = tuple(tuple(sorted([cell for row in initial_state for cell in row if cell != '_'], reverse=True)[i*num_cols:(i+1)*num_cols] for i in range(num_rows)))
   # Get the initial coordinate of the empty spot
   initial_empty_spot = [(i, j) for i, row in enumerate(initial_state) for j, cell in enumerate(row) if cell == '_'][0]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, deque(), initial_state, initial_empty_spot)]


   while queue:
       _, g, actions, state, empty_spot = heapq.heappop(queue)


       if state == goal_state:
           return list(actions)


       # Generate all possible actions from the current state, which includes swapping the empty spot with any of the 4 neighboring cells
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = empty_spot[0] + d_row, empty_spot[1] + d_col
           # Check if the new coordinate is valid, ie if the new cell is within the bounds of the puzzle
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               # Swap the empty spot with the new cell
               new_state[empty_spot[0]][empty_spot[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_spot[0]][empty_spot[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The number on the tile that the empty spot is swapped with must be added to the actions
                   heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + deque([int(new_state[empty_spot[0]][empty_spot[1]])]), new_state, (new_row, new_col)))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances from each cell to its goal position
   # This heuristic relaxes the constraint that only the empty spot can be moved
   # It is admissible because it never overestimates the cost to reach the goal, as each cell must be moved at least once
   # It's consistent because moving a cell from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved cell's goal position is in the direction of the move), which is equal to the cost of reaching the successor node
   # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
   # And the cost of the goal state is 0, as all cells will be in their goal positions
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] != '_':
               goal_i, goal_j = [(k, l) for k, row in enumerate(goal) for l, cell in enumerate(row) if cell == state[i][j]][0]
               h += abs(i - goal_i) + abs(j - goal_j)
   return h


print(a_star())
