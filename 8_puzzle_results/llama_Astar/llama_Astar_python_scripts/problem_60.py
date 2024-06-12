
import heapq


def a_star():
   # Define the initial state of the puzzle
   initial_state = (('31', '92', '67', '69'),
                   ('87', '35', '42', '72'),
                   ('53', '_', '28', '19'))
   # Define the goal state
   goal_state = (('8', '7', '6', '5'),
                 ('4', '3', '2', '1'),
                 ('_', 'A', 'B', 'C'))
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
       for i in range(len(state)):
           for j in range(len(state[i])):
               if state[i][j] == '_':
                   for move in moves:
                       new_i, new_j = i + move[0], j + move[1]
                       # Check if the new state is valid, ie the new position is within the bounds of the grid and not a wall
                       if 0 <= new_i < len(state) and 0 <= new_j < len(state[i]) and state[new_i][new_j] != 'x':
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to solve the puzzle
                           new_cost = g + 1


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               h = heuristic(state, goal_state)
                               heapq.heappush(queue, (new_cost + h, new_cost, actions + [state[i][j]], new_state))
   return None




def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the Manhattan distance from the current state to the goal state
   # The heuristic relaxes the constraints that the tiles can only move in 4 directions, and that the tiles can only move into the empty spot, by presuming we can move any tile to any position
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving a tile to an adjacent position is the Manhattan distance between the positions, which is always greater than or equal to 1, the decrease in the Manhattan distance
   return sum(abs(i - new_i) + abs(j - new_j) for i, row in enumerate(state) for j, cell in enumerate(row) if cell != '_' and (new_i, new_j) != (i, j))




print(a_star())
