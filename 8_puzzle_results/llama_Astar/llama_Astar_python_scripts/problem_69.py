
import heapq


def a_star():
   # Define the initial state of the puzzle as a 2d tuple
   initial_state = (('_', '83', '11', '57', '59'),
                   ('89', '61', '99', '76', '63'),
                   ('42', '35', '25', '48', '54'))
   # Define the goal state
   goal_state = (('89', '83', '76', '63', '59'),
                 ('57', '61', '54', '48', '51'),
                 ('42', '35', '25', '11', '_'))
   # Define the possible moves of the empty spot
   moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes moving the empty spot to any of the 4 neighboring positions
       for move in moves:
           new_row, new_col = state.index('_') + move[0], state[0].index('_') + move[1]
           # Check if the new position is valid, ie within the bounds of the grid and not out of the row or column
           if 0 <= new_row < len(state) and 0 <= new_col < len(state[0]):
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[state.index('_')][state[0].index('_')], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[state.index('_')][state[0].index('_')]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state[new_row][new_col]], new_state))
   return None




def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the Manhattan distance (shortest path) from the current state to the goal state
   # The heuristic relaxes the constraints that the tiles can only move in 4 directions, and the goal state is when all tiles are in descending order, with the largest number in the top left corner, and the empty spot is in the bottom right corner
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one tile to an adjacent tile is the Manhattan distance between the tiles, which is always greater than or equal to 1, the decrease in the Manhattan distance
   return sum(abs(state.index(str(i)) - goal.index(str(i))) for i in range(1, 9))




print(a_star())
