
import heapq
import numpy as np


def a_star():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('w', 'k', 'u', 'a', 'd', 'i'),
                   ('s', 'a', 'a', 'r', 'm', 'y'),
                   ('h', 'g', '_', 'i', 's', 'h'),
                   ('w', 'h', 'e', 'a', 't', 'y'))
   num_rows = 4
   num_cols = 6
   target_words = ['khadi', 'swarmy', 'aguish', 'wheaty']
   # Define the goal state of the board as a 2d tuple
   goal_state = tuple(tuple(word) for word in target_words)
   # Define the directions of the diagonal moves
   directions = {'up-right': (-1, 1), 'down-right': (1, 1), 'up-left': (-1, -1), 'down-left': (1, -1)}


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes moving the blank space to any of the 4 diagonal directions
       # Get the coordinate of the blank space
       blank_coord = [(i, j) for i, row in enumerate(state) for j, element in enumerate(row) if element == '_'][0]
       for direction, (d_row, d_col) in directions.items():
           new_row, new_col = blank_coord[0] + d_row, blank_coord[1] + d_col
           # Check if the new coordinate is valid, ie if the blank space can be moved to the new position
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[blank_coord[0]][blank_coord[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_coord[0]][blank_coord[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (g + h, new_cost, actions + [direction], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances from each tile in the current state to its position in the goal state
   # The heuristic relaxes the constraint that only the blank space can be moved and that it can only be moved diagonally, ie It presumes we can move directly to any given coordinate toward the goal
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving the blank space from one position to an adjacent position is 1, which is equal to the decrease in the Manhattan distance
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           goal_i, goal_j = np.where(np.array(goal) == state[i][j])
           h += abs(i - goal_i[0]) + abs(j - goal_j[0])
   return h


print(a_star())
