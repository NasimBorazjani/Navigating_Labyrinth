
import heapq
from collections import deque


def a_star():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('a', 'r', '_', 'c'),
                   ('h', 'a', 'v', 'e'),
                   ('a', 'g', 's', 'd'),
                   ('b', 'i', 't', 'z'))
   # Define the goal state of the board as a 2d tuple
   goal_state = (('_', 'r', 'i', 'c'),
                 ('h', 'a', 'v', 'e'),
                 ('s', 'g', 'a', 'd'),
                 ('b', 'a', 't', 'z'))
   num_rows = 4
   num_cols = 4
   # Define the 4 possible diagonal directions of movement for the blank space
   directions = [('up-right', (-1, 1)), ('down-right', (1, 1)), ('up-left', (-1, -1)), ('down-left', (1, -1))]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken to reach the goal state
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes moving the blank space in any of the 4 diagonal directions
       # First, find the coordinates of the blank space in the current state
       blank_space_coord = [(i, j) for i, row in enumerate(state) for j, element in enumerate(row) if element == '_'][0]
       for direction, (d_row, d_col) in directions:
           new_row, new_col = blank_space_coord[0] + d_row, blank_space_coord[1] + d_col
           # Check if the new coordinate is valid, ie if the blank space can be moved to the new position
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[blank_space_coord[0]][blank_space_coord[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_space_coord[0]][blank_space_coord[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic is the number of misplaced tiles in the current state
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (g + h, new_cost, actions + [direction], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the count of misplaced tiles in the current state
   # This heuristic relaxes the constraint that only the blank space can be moved, and only in the 4 diagonal directions
   # It is admissible because it never overestimates the cost to reach the goal, as each misplaced tile must be moved at least once
   # It's consistent because moving the blank space reduces the heuristic cost of the successor node by a max of 1 (if the moved tile is misplaced in the current state but not in the new state), which is equal to the cost of reaching the successor node
   # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
   # And the cost of the goal state is 0, as all tiles are in their correct positions
   return sum(s != g for s_row, g_row in zip(state, goal) for s, g in zip(s_row, g_row))


print(a_star())
