
import heapq


def a_star():
   # Define the initial state of the puzzle
   initial_state = (('11', '55', '69', '67'),
                   ('19', '31', '_', '35'),
                   ('64', '65', '88', '96'))
   # Define the goal state
   goal_state = (('96', '88', '65', '64'),
                 ('35', '31', '_', '19'),
                 ('67', '69', '55', '11'))
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
           new_row, new_col = state.index('_') + move[0], state[0].index('_') + move[1]
           # Check if the new state would be valid, ie the new position of the empty spot must be within the bounds of the grid
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




def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the Manhattan distance from the current state to the goal state
   # The heuristic relaxes the constraints that the tiles can only move in 4 directions, and that the tiles can only move into the empty spot, and that the tiles must be arranged in descending order
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving a tile to an adjacent position is the Manhattan distance between the positions, which is always greater than or equal to 1, the decrease in the Manhattan distance
   return sum(abs(state.index(str(i)) // len(state) - goal.index(str(i)) // len(goal)) + abs(state.index(str(i)) % len(state[0]) - goal.index(str(i)) % len(goal[0])) for i in range(1, 9))




print(a_star())
