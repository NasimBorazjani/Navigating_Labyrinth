
import heapq


def initialize():
   # Define the initial state of the puzzle as a 2d tuple
   initial_state = (('12', '55', '_'),
                   ('35', '97', '43'),
                   ('17', '25', '9'))


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, visited_costs, queue
  
def a_star():
  
   initial_state, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == (('9', '8', '7'), ('6', '5', '4'), ('3', '2', '1')):
           return actions


       # Generate all possible actions from the current state, which includes swapping the empty spot with any of the 8 neighboring tiles
       for row in range(3):
           for col in range(3):
               if state[row][col] == '_':
                   for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                       new_row, new_col = row + d_row, col + d_col
                       # Check if the new state is valid, ie the new position of the empty spot is within the bounds of the grid
                       if 0 <= new_row < 3 and 0 <= new_col < 3:
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the number of moves made, as the task is to minimize the number of moves required
                           new_cost = g + 1


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               # The heuristic is not used in this problem as the goal state is always reachable from any state and the cost of moving from one state to another is always equal to 1
                               heapq.heappush(queue, (new_cost, new_cost, actions + [int(state[row][col])], new_state))
   return None


print(a_star())
