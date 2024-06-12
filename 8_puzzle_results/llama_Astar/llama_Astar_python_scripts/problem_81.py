
import heapq


def a_star():
   # Define the initial state of the puzzle as a 2d tuple
   initial_state = (('12', '76', '_', '72', '53'),
                   ('61', '97', '49', '65', '52'),
                   ('89', '64', '22', '26', '13'))
   # Define the goal state
   goal_state = (('9', '8', '7', '6', '5'),
                 ('4', '3', '2', '1', '_'))
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


       # Generate all possible actions from the current state, which includes moving the empty spot in any of the 4 directions
       for move in moves:
           new_state = [list(row[:]) for row in state]
           empty_row, empty_col = next((i, j) for i, row in enumerate(new_state) for j, cell in enumerate(row) if cell == '_')
           new_empty_row, new_empty_col = empty_row + move[0], empty_col + move[1]
           # Check if the new state would be valid, ie the new empty spot must be within the bounds of the grid
           if 0 <= new_empty_row < len(new_state) and 0 <= new_empty_col < len(new_state[0]):
               # Swap the empty spot with the new spot
               new_state[empty_row][empty_col], new_state[new_empty_row][new_empty_col] = new_state[new_empty_row][new_empty_col], new_state[empty_row][empty_col]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state[empty_row][empty_col]], new_state))
   return None




def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the Manhattan distance (shortest path) from the current state to the goal state
   # The heuristic relaxes the constraints that the tiles can only move in 4 directions, and that the tiles can only be swapped with the empty spot; ie It presumes we can move directly to any given tile towards the goal
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of the cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one tile to an adjacent tile is the Manhattan distance between the tiles, which is always greater than or equal to 1, the decrease in the Manhattan distance
   return sum(abs(int(state[i][j]) - int(goal[i][j])) for i in range(len(state)) for j in range(len(state[0])) if state[i][j] != '_' and goal[i][j] != '_')




print(a_star())
