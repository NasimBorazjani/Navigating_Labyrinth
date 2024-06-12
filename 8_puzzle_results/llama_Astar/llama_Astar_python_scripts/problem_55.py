
import heapq


def a_star():
   # Define the initial state of the puzzle
   initial_state = (('34', '68', '46', '20'),
                   ('12', '18', '_', '5'),
                   ('53', '7', '65', '47'))
   # Define the goal state
   goal_state = (('8', '7', '6', '5'),
                 ('4', '3', '_', '2'),
                 ('1', '15', '14', '13'))
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


       # Generate all possible actions from the current state
       for i in range(len(state)):
           for j in range(len(state[i])):
               if state[i][j] == '_':
                   for move in moves:
                       new_i, new_j = i + move[0], j + move[1]
                       # Check if the new state is valid, ie the new position of the empty spot is within the bounds of the grid
                       if 0 <= new_i < len(state) and 0 <= new_j < len(state[i]):
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
   # The heuristic relaxes the constraints that the tiles can only move in 4 directions, and that the tiles can only be swapped with the empty spot; ie it presumes we can move and swap the tiles directly to any given position
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving a tile to an adjacent position is the Manhattan distance between the positions, which is always greater than or equal to 1, the decrease in the Manhattan distance
   return sum(abs(i - new_i) + abs(j - new_j) for i, row in enumerate(state) for j, cell in enumerate(row) if cell != '_' for new_i, new_j in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)] if 0 <= new_i < len(state) and 0 <= new_j < len(state[i]) and goal[new_i][new_j] == cell)




print(a_star())
