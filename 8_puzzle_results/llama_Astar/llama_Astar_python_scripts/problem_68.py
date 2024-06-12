
import heapq


def a_star():
   # Define the initial state of the puzzle as a 2d tuple
   initial_state = (('72', '92', '_', '78', '74'),
                   ('70', '67', '85', '75', '66'),
                   ('48', '42', '32', '26', '50'))
   # Define the goal state
   goal_state = (('8', '_', '7', '6', '5'),
                 ('4', '3', '2', '1', '7'),
                 ('6', '8', '9', '10', '11'))
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
           new_row, new_col = state.index('_') + move[0], state[0].index('_') + move[1]
           # Check if the new state would be valid, ie the new spot must be within the bounds of the grid
           if 0 <= new_row < len(state) and 0 <= new_col < len(state[0]):
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[new_row][new_col], new_state[state.index('_')][state[0].index('_')] = new_state[state.index('_')][state[0].index('_')], new_state[new_row][new_col]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state[new_row][new_col]], new_state))
   return None




def heuristic(state, goal_state):
   # The heuristic function can be the Manhattan distance between the current state and the goal state
   # This heuristic is admissible because it is a lower bound on the cost to reach the goal state
   # The heuristic is consistent as the estimated cost of the next node is higher if the empty spot is further from the goal spot, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of moves that can be made is by moving the empty spot to the goal spot in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] != '_':
               goal_row, goal_col = goal_state.index('_') // len(goal_state[0]), goal_state.index('_') % len(goal_state[0])
               h += abs(i - goal_row) + abs(j - goal_col)
   return h


print(a_star())
