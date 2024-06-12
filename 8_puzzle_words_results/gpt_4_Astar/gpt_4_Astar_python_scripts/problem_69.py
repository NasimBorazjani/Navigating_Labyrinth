
import heapq
from collections import deque


def a_star():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('c', 'o', 'a', 'c'),
                   ('i', 'o', 'h', 'r'),
                   ('d', 'e', 'r', 'r'),
                   ('f', 'o', 'u', 'a'),
                   ('p', 'e', '_', 'i'))
   # Define the goal state of the board as a 2d tuple
   goal_state = (('o', 'r', 'c', '_'),
                ('i', 'c', 'h', 'o'),
                ('d', 'e', 'a', 'r'),
                ('f', 'o', 'u', 'r'),
                ('p', 'e', 'a', 'i'))
   num_rows = 5
   num_cols = 4
   # Define the 4 possible diagonal moves
   moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
   # Define the corresponding move names
   move_names = ['down-right', 'down-left', 'up-right', 'up-left']


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       if state == goal_state:
           return actions


       # Get the coordinates of the blank space
       blank_coord = [(i, j) for i, row in enumerate(state) for j, element in enumerate(row) if element == '_'][0]
       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
       for move, move_name in zip(moves, move_names):
           new_row, new_col = blank_coord[0] + move[0], blank_coord[1] + move[1]
           # Check if the new coordinate is valid, ie if the new tile is within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[blank_coord[0]][blank_coord[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_coord[0]][blank_coord[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [move_name], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances from each tile in its current position to its goal position
   # This heuristic relaxes the constraint that only the blank space can be moved, and that it can only be swapped with a diagonal neighbor
   # It is admissible because it never overestimates the cost to reach the goal, as each tile must be moved at least once for each unit of Manhattan distance
   # It's consistent because moving a tile reduces the Manhattan distance of that tile to the goal by 1 (if the move is toward the goal), which is equal to the cost of reaching the successor node
   # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
   # And the cost of the goal state is 0, as all tiles are in their goal positions
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           goal_coord = [(x, y) for x, row in enumerate(goal) for y, element in enumerate(row) if element == state[i][j]][0]
           h += abs(i - goal_coord[0]) + abs(j - goal_coord[1])
   return h


print(a_star())
