
import heapq


def a_star():
   # Define the initial state of the puzzle as a 2d tuple
   initial_state = (('93', '83', '50', '21', '67'),
                   ('59', '_', '60', '19', '8'),
                   ('14', '12', '92', '54', '9'))
   # Define the goal state
   goal_state = (('9', '8', '7', '6', '5'),
                 ('4', '_', '3', '2', '1'),
                 ('10', '11', '12', '13', '14'))
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
           new_row, new_col = state[1][0] + move[0], state[1][1] + move[1]
           # Check if the new state would be valid, ie the new spot must be within the bounds of the grid and not be a wall
           if 0 <= new_row < len(state) and 0 <= new_col < len(state[0]) and state[new_row][new_col] != '_':
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[1][0], new_state[1][1] = new_row, new_col
               new_state[state[1][0]][state[1][1]], new_state[new_row][new_col] = new_state[new_row][new_col], '_'
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(state, goal_state)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [state[1][0] * len(state[0]) + state[1][1]], new_state))
   return None




def heuristic(state, goal_state):
   # The heuristic function can be the Manhattan distance between the current state and the goal state
   # This heuristic is admissible because it is a lower bound on the cost to reach the goal state
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] != '_':
               goal_i, goal_j = divmod(state[i][j], len(state[0]))
               h += abs(i - goal_i) + abs(j - goal_j)
   return h




print(a_star())
