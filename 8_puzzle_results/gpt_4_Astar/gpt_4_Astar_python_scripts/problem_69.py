
import heapq
from copy import deepcopy


def a_star():
   # Define the initial state of the puzzle as a 2d tuple
   initial_state = (('_', 83, 11, 57, 59),
                   (89, 61, 99, 76, 63),
                   (42, 35, 25, 48, 54))
   num_rows = 3
   num_cols = 5
   # The goal state is the sorted list of all the numbers in the puzzle in descending order, with the empty spot at the end
   goal_state = tuple(tuple(sorted([cell for row in initial_state for cell in row if cell != '_'], reverse=True)[i*num_cols:(i+1)*num_cols] for i in range(num_rows)))
   # Get the initial coordinate of the empty spot
   initial_empty_spot = [(i, j) for i, row in enumerate(initial_state) for j, cell in enumerate(row) if cell == '_'][0]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state, initial_empty_spot)]


   while queue:
       _, g, actions, state, empty_spot = heapq.heappop(queue)


       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes moving the empty spot to any of the 4 neighboring cells
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
                   # The number on the tile that the empty spot is swapped with must be added to the actions
                   heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [new_state[empty_spot[0]][empty_spot[1]]], new_state, (new_row, new_col)))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances from each cell to its goal position
   # The heuristic relaxes the constraint that only the empty spot can be moved, and assumes that any cell can be moved to its goal position in one step
   # Thus the heuristic never overestimates the cost to reach the goal, making it admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving the empty spot to an adjacent cell is 1, which is equal to the decrease in the Manhattan distance of the moved cell to its goal position
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           goal_i, goal_j = [(x, y) for x, row in enumerate(goal) for y, cell in enumerate(row) if cell == state[i][j]][0]
           h += abs(i - goal_i) + abs(j - goal_j)
   return h


print(a_star())
