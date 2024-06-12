
import heapq


def initialize():
   # Define the initial state of the puzzle, as a 2d tuple
   initial_state = (('46', '82', '90'),
                   ('36', '41', '38'),
                   ('28', '55', '_'))
   num_rows = 3
   num_cols = 3
   goal_state = (('9', '8', '7'),
                 ('6', '5', '4'),
                 ('3', '2', '1'))


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, goal_state, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, goal_state, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes swapping the empty spot with any of the 8 neighboring spots
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[2].index('_') + d_row, state[2].index('_') + d_col
           # Check if the new state is valid, ie the new empty spot is within the bounds of the grid
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[2][new_row][new_col], new_state[2][2][2] = new_state[2][2][2], new_state[2][new_row][new_col]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to solve the puzzle
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state[2][2][2]], new_state))
   return None




def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the Manhattan distance (shortest path) from the current state to the goal state
   # The heuristic relaxes the constraints that the tiles can only move in 4 directions; ie It presumes we can move directly to any given tile toward the goal
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of the cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one tile to an adjacent tile is the Manhattan distance between the tiles, which is always greater than or equal to 1, the decrease in the Manhattan distance
   return sum(abs(state[i][j] - goal[i][j]) for i in range(3) for j in range(3))


print(a_star())
