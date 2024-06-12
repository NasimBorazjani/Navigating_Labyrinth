
import heapq


def a_star():
   # Define the initial state of the puzzle as a 2d tuple
   initial_state = (('60', '70', '88', '51', '72'),
                   ('87', '43', '39', '85', '30'),
                   ('_', '64', '27', '84', '47'))
   # Define the goal state
   goal_state = (('88', '72', '60', '51', '70'),
                 ('87', '85', '64', '47', '30'),
                 ('_', '39', '27', '43', '44'))
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


       # Generate all possible actions from the current state, which includes moving the empty spot to any of the 4 neighboring positions
       for move in moves:
           new_row, new_col = state[1][1] + move[0], state[1][1] + move[1]
           # Check if the new position is valid, ie if the new position is within the bounds of the grid
           if 0 <= new_row < len(state) and 0 <= new_col < len(state[0]):
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[state[1][1] // len(state[0])][state[1][1] % len(state[0])], new_state[new_row][new_col] = new_state[new_row][new_col], '_'
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic function is the Manhattan distance from the current state to the goal state
                   h = heuristic(state, goal_state)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state[1][1]], new_state))
   return None




def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the Manhattan distance from the current state to the goal state
   # The heuristic relaxes the constraints that the tiles can only move in 4 directions, and the tiles can only move to the empty spot, and the tiles can only move to the empty spot; ie It presumes we can move directly to any given tile to the empty spot
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of the cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one tile to an adjacent tile is the Manhattan distance between the tiles, which is always greater than or equal to 1, the decrease in the Manhattan distance
   return sum(abs(state[i][j] - goal[i][j]) for i in range(len(state)) for j in range(len(state[0])) if state[i][j] != '_')




print(a_star())
