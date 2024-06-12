
import heapq


def a_star():
   # Define the initial state of the puzzle
   initial_state = (('10', '96', '60', '_'),
                   ('98', '73', '14', '58'),
                   ('53', '3', '21', '67'))
   # Define the goal state
   goal_state = (('98', '73', '67', '_'),
                 ('60', '58', '3', '21'),
                 ('10', '53', '14', '60'))
   # Define the possible moves
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
       for row in range(len(state)):
           for col in range(len(state[row])):
               if state[row][col] == '_':
                   for move in moves:
                       new_row, new_col = row + move[0], col + move[1]
                       # Check if the new state would be valid, ie the new position is within the bounds of the grid
                       if 0 <= new_row < len(state) and 0 <= new_col < len(state[row]):
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the number of moves made, as the task is to minimize the number of moves required
                           new_cost = g + 1


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               h = heuristic(state, goal_state)
                               heapq.heappush(queue, (new_cost + h, new_cost, actions + [state[row][col]], new_state))
   return None




def heuristic(state, goal_state):
   # An admissible and consistent heuristic for this problem is the Manhattan distance (shortest path) from the current state to the goal state
   # The heuristic relaxes the constraints that the tiles can only move in 4 directions, and that the tiles can only move into the empty spot; ie It presumes we can move directly to any given tile to the goal state
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one tile to an adjacent tile is the Manhattan distance between the tiles, which is always greater than or equal to 1, the decrease in the Manhattan distance
   return sum(abs(state.index(str(i)) // 2 - goal_state.index(str(i)) // 2) + abs(state.index(str(i)) % 2 - goal_state.index(str(i)) % 2) for i in range(1, 9))




print(a_star())
