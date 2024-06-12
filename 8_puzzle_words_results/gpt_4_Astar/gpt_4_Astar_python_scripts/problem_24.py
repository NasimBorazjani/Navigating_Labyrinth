
import heapq
from collections import deque


def a_star():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('_', 'p', 'h', 'm', 'p'),
                   ('s', 'a', 'd', 'r', 'e'),
                   ('i', 'u', 'n', 'i', 'r'),
                   ('u', 'a', 'z', 'e', 'n'))
   # Define the goal state of the board as a 2d tuple
   goal_state = (('p', 'i', 'm', 'p', '_'),
                 ('s', 'a', 'd', 'h', 'e'),
                 ('a', 'u', 'r', 'i', 'r'),
                 ('u', 'n', 'z', 'e', 'n'))
   num_rows = 4
   num_cols = 5
   # Define the initial position of the blank space
   blank_space = (0, 0)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state, blank_space)]


   while queue:
       _, g, actions, state, blank_space = heapq.heappop(queue)


       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
       for d_row, d_col, direction in [(1, 1, 'down-right'), (-1, -1, 'up-left'), (-1, 1, 'up-right'), (1, -1, 'down-left')]:
           new_row, new_col = blank_space[0] + d_row, blank_space[1] + d_col
           # Check if the new position of the blank space is valid, ie if it is within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[blank_space[0]][blank_space[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_space[0]][blank_space[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic is the sum of the Manhattan distances from each character to its goal position
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (g + h, new_cost, actions + [direction], new_state, (new_row, new_col)))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances from each character to its goal position
   # The heuristic relaxes the constraint that the blank space can only be swapped with its diagonal neighbors, ie It presumes we can move directly to any given position toward the goal
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving the blank space from one position to an adjacent position is 1, which is always greater than or equal to the decrease in the Manhattan distance
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           goal_i, goal_j = next((x, y) for x, row in enumerate(goal) for y, cell in enumerate(row) if cell == state[i][j])
           h += abs(i - goal_i) + abs(j - goal_j)
   return h


print(a_star())
