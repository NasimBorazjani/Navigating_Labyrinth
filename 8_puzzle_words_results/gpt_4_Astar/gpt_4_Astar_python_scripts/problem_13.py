
import heapq
from collections import deque


def a_star():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('b', 'l', '_', 'g'),
                   ('a', 'n', 'a', 's'),
                   ('m', 'u', 'a', 'a'),
                   ('s', 'h', 'a', 'm'))
   # Define the goal state of the board as a 2d tuple
   goal_state = (('_', 'l', 'a', 'g'),
                 ('a', 'b', 'a', 's'),
                 ('n', 'u', 'm', 'a'),
                 ('s', 'h', 'a', 'm'))
   num_rows = 4
   num_cols = 4
   # Define the 4 possible diagonal directions
   directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
   # Define the direction names
   direction_names = ['down-right', 'down-left', 'up-right', 'up-left']


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       if state == goal_state:
           return actions


       # Get the coordinate of the blank space
       blank_coord = [(i, j) for i, row in enumerate(state) for j, element in enumerate(row) if element == '_'][0]
       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
       for direction, direction_name in zip(directions, direction_names):
           new_row, new_col = blank_coord[0] + direction[0], blank_coord[1] + direction[1]
           # Check if the new coordinate is valid, ie if the new tile is within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[blank_coord[0]][blank_coord[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_coord[0]][blank_coord[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to sort the board
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic is the sum of the Manhattan distances from each tile to its goal position
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (g + h, new_cost, actions + [direction_name], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances from each tile to its goal position
   # The heuristic relaxes the constraint that the blank space can only be swapped with its diagonal neighbors, ie It presumes we can move any tile directly to its goal position
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving the blank space to an adjacent tile is 1, which is always greater than or equal to the decrease in the Manhattan distance
   # Also the cost of the goal state is 0, as all tiles are in their goal positions
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           goal_coord = [(k, l) for k, row in enumerate(goal) for l, element in enumerate(row) if element == state[i][j]][0]
           h += abs(i - goal_coord[0]) + abs(j - goal_coord[1])
   return h


print(a_star())
