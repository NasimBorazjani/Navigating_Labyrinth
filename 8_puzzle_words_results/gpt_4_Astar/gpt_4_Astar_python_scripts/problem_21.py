
import heapq
from collections import deque


def a_star():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('m', 'p', 'l', 's', 's'),
                   ('s', 'a', 'o', 's', 'e'),
                   ('c', 'a', '_', 'e', 'k'),
                   ('h', 'i', 'r', 'o', 'm'))
   # Define the goal state of the board as a 2d tuple
   goal_state = (('p', 'o', 's', 's', '_'),
                ('s', 'm', 'o', 'k', 'e'),
                ('c', 'a', 's', 'e', 'l'),
                ('h', 'i', 'r', 'a', 'm'))
   num_rows = 4
   num_cols = 5
   # Define the 4 possible diagonal directions of movement for the blank space
   directions = {'up-right': (-1, 1), 'down-right': (1, 1), 'up-left': (-1, -1), 'down-left': (1, -1)}


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
       blank_space_coord = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == '_'][0]
       for direction, (d_row, d_col) in directions.items():
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
                   # The heuristic is the sum of the Manhattan distances from each tile to its goal position
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (g + h, new_cost, actions + [direction], new_state))
   return None


def heuristic(state, goal):
   # The heuristic function can be the sum of the Manhattan distances from each tile to its goal position
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as each tile must be moved at least the Manhattan distance to its goal position
   # It's consistent because moving a tile reduces the Manhattan distance of that tile to its goal position by at most 1 (equal to the cost of reaching the successor node), and the Manhattan distance of all other tiles remain the same. Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
   # And the cost of the goal state is 0, as all tiles are at their goal positions
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           goal_coord = [(x, y) for x in range(len(goal)) for y in range(len(goal[0])) if goal[x][y] == state[i][j]][0]
           h += abs(i - goal_coord[0]) + abs(j - goal_coord[1])
   return h


print(a_star())
