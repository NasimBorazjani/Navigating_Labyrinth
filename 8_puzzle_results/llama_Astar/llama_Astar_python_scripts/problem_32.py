
import heapq


def a_star():
   # Define the initial state of the puzzle
   initial_state = (('69', '56', '8', '67'),
                   ('15', '47', '44', '30'),
                   ('73', '_', '24', '63'))
   # Define the goal state
   goal_state = (('8', '1', '2', '3'),
                 ('4', '5', '6', '7'),
                 ('_', '9', '10', '11'))
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
       for move in moves:
           # Calculate the new position of the empty spot
           new_empty_row, new_empty_col = state[0].index('_') + move[0], state[0].index('_') + move[1]
           # Check if the new position is valid
           if 0 <= new_empty_row < len(state) and 0 <= new_empty_col < len(state[0]):
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[new_empty_row][new_empty_col], new_state[state[0].index('_')][state[0].index('_')] = new_state[state[0].index('_')][state[0].index('_')], new_state[new_empty_row][new_empty_col]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to solve the puzzle
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(state, goal_state)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state[new_empty_row][new_empty_col]], new_state))
   return None




def heuristic(state, goal_state):
   # The heuristic function can be the Manhattan distance between the current state and the goal state
   # This heuristic is admissible because it is a lower bound on the cost to reach the goal state
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] != '_':
               goal_row, goal_col = next(((k, l) for k, row in enumerate(goal_state) for l, cell in enumerate(row) if cell == state[i][j]), None)
               h += abs(i - goal_row) + abs(j - goal_col)
   return h




print(a_star())
