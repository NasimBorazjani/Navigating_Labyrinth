
import heapq


def a_star():
   # Define the initial state of the puzzle
   initial_state = (('100', '96', '93', '82', '6', '19'),
                   ('68', '53', '50', '9', '_', '24'),
                   ('16', '15', '48', '10', '76', '74'))
   # Define the goal state
   goal_state = (('_', '_', '_', '_', '_', '_'),
                 ('_', '_', '_', '_', '_', '_'),
                 ('_', '_', '_', '_', '_', '_'))
   # Define the possible moves
   moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state
       for move in moves:
           new_row, new_col = state[1][4], state[1][5]
           # Check if the new state would be valid, ie the empty spot can move to the new position
           if 0 <= new_row + move[0] < 3 and 0 <= new_col + move[1] < 6:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[new_row + move[0]][new_col + move[1]], new_state[1][4], new_state[1][5] = new_state[1][4], new_state[1][5], new_state[new_row + move[0]][new_col + move[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(state, goal_state)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state[1][5]], new_state))
   return None




def heuristic(state, goal_state):
   # An admissible and consistent heuristic for this problem is the Manhattan distance from the current state to the goal state
   # The heuristic relaxes the constraints that the tiles can only move in 4 directions, and that the tiles can only move into the empty spot
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving a tile to an adjacent position is the Manhattan distance between the positions, which is always greater than or equal to 1, the decrease in the Manhattan distance
   return sum(abs(int(state[i][j]) - int(goal_state[i][j])) for i in range(3) for j in range(6) if state[i][j] != '_' and goal_state[i][j] != '_')




print(a_star())
