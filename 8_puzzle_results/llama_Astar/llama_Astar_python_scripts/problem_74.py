
import heapq


def a_star():
   # Define the initial state of the puzzle as a 2d tuple
   initial_state = (('49', '20', '77', '78', '57'),
                   ('41', '_', '52', '44', '72'),
                   ('27', '81', '45', '16', '46'))
   # Define the goal state
   goal_state = (('8', '7', '6', '5', '4'),
                 ('3', '_', '2', '1', '0'),
                 ('15', '14', '13', '12', '11'))
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


       # Generate all possible actions from the current state, which includes moving the empty spot in any of the 4 directions
       for move in moves:
           new_row, new_col = state[1]
           # Check if the new position is valid, ie within the bounds of the grid and not blocked by another tile
           while 0 <= new_row + move[0] < len(state) and 0 <= new_col + move[1] < len(state[0]) and state[new_row + move[0]][new_col + move[1]] != '_':
               new_row += move[0]
               new_col += move[1]
           # Generate the new state
           new_state = [list(row[:]) for row in state]
           new_state[1][0], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[1][0]
           new_state = tuple(tuple(row) for row in new_state)
           # The cost so far is the number of moves made, as the task is to minimize the number of moves required
           new_cost = g + 1


           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
               visited_costs[new_state] = new_cost
               h = heuristic(state, goal_state)
               heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state[1][0]], new_state))
   return None




def heuristic(state, goal_state):
   # An admissible and consistent heuristic for this problem is the Manhattan distance (shortest path) from the current state to the goal state
   # The heuristic relaxes the constraints that the tiles can only move in 4 directions, and that the tiles can only move if the empty spot is not blocked by another tile
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one tile to an adjacent tile is the Manhattan distance between the tiles, which is always greater than or equal to 1, the decrease in the Manhattan distance
   return sum(abs(state[i][j] - goal_state[i][j]) for i in range(len(state)) for j in range(len(state[0])) if state[i][j] != '_')




print(a_star())
