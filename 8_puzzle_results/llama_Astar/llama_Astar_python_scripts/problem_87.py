
import heapq


def a_star():
   # Define the initial state of the puzzle as a 2d tuple
   initial_state = (('_', '94', '43', '58', '77'),
                   ('96', '100', '75', '84', '52'),
                   ('50', '29', '60', '27', '74'))
   # Define the goal state
   goal_state = (('8', '7', '6', '5', '4'),
                 ('3', '2', '1', '_', '9'),
                 ('10', '11', '12', '13', '14'))
   # Convert the states to lists for easier manipulation
   initial_state = [list(row) for row in initial_state]
   goal_state = [list(row) for row in goal_state]


   visited_costs = {}
   visited_costs[tuple(initial_state)] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes swapping the empty spot with any of the 4 neighboring tiles
       for i in range(len(state)):
           for j in range(len(state[i])):
               if state[i][j] == '_':
                   for d_i, d_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                       new_i, new_j = i + d_i, j + d_j
                       # Check if the new state would be valid, ie the new tile must not be out of the bounds of the grid
                       if 0 <= new_i < len(state) and 0 <= new_j < len(state[i]):
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
                           new_state = [tuple(row) for row in new_state]
                           # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to solve the puzzle
                           new_cost = g + 1


                           if tuple(new_state) not in visited_costs or new_cost < visited_costs[tuple(new_state)]:
                               visited_costs[tuple(new_state)] = new_cost
                               h = heuristic(new_state, goal_state)
                               heapq.heappush(queue, (new_cost + h, new_cost, actions + [int(state[i][j])], new_state))
   return None




def heuristic(state, goal_state):
   # An admissible and consistent heuristic for this problem is the Manhattan distance (shortest path) from the current state to the goal state
   # The heuristic relaxes the constraints that the tiles can only move in 4 directions, and that the tiles can only be swapped with the empty spot; ie It presumes we can move directly to any given tile toward the goal
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of the cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one tile to an adjacent tile is the Manhattan distance between the tiles, which is always greater than or equal to 1, the decrease in the Manhattan distance
   return sum(abs(i - new_i) + abs(j - new_j) for i, row in enumerate(state) for j, cell in enumerate(row) if cell != '_' for new_i, new_row in enumerate(goal_state) for new_j, new_cell in enumerate(new_row) if new_cell == cell)




print(a_star())
