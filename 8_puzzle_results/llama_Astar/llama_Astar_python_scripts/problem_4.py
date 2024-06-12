
import heapq


def a_star():
   # Define the initial state of the puzzle
   initial_state = (('66', '89', '70'),
                   ('25', '42', '83'),
                   ('_', '24', '71'))
   # Define the goal state
   goal_state = (('8', '7', '6'),
                 ('5', '4', '3'),
                 ('_', '2', '1'))
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
   # An admissible and consistent heuristic for this problem is the Manhattan distance (shortest path) from the current state to the goal state
   # The heuristic relaxes the constraints that the number of moves between different states is not the same, and the goal state is in a specific order
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one state to an adjacent state is the number of moves between the states, which is always greater than or equal to 1, the decrease in the Manhattan distance
   return sum(abs(i - new_i) + abs(j - new_j) for i, row in enumerate(state) for j, cell in enumerate(row) if cell != '_' for new_i, new_j in [(i, j), (i + move[0], j + move[1])] if 0 <= new_i < len(state) and 0 <= new_j < len(state[i]) and state[new_i][new_j] == '_')




print(a_star())
