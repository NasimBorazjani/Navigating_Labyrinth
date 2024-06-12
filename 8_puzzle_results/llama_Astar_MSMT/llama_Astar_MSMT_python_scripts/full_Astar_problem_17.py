
import heapq


def initialize():
   # Define the initial state of the puzzle as a 2d tuple
   initial_state = (('27', '18', '79'),
                   ('22', '99', '9'),
                   ('49', '53', '_'))
   num_rows = 3
   num_cols = 3
   goal_state = (('9', '8', '7'),
                 ('6', '5', '4'),
                 ('3', '2', '_'))


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, goal_state, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, goal_state, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes swapping the empty spot with any of the 8 neighboring tiles
       for row_shift in [-1, 0, 1]:
           for col_shift in [-1, 0, 1]:
               if row_shift != 0 or col_shift != 0:
                   new_state = [list(row[:]) for row in state]
                   empty_row, empty_col = [i for i, row in enumerate(state) for j, cell in enumerate(row) if cell == '_'][0]
                   new_state[empty_row][empty_col] = new_state[empty_row + row_shift][empty_col + col_shift]
                   new_state[empty_row + row_shift][empty_col + col_shift] = '_'
                   new_state = tuple(tuple(row) for row in new_state)
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The heuristic is the Manhattan distance between the current state and the goal state
                       h = heuristic(state, goal_state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [int(new_state[empty_row][empty_col])], new_state))
   return None




def heuristic(state, goal_state):
   # The heuristic is the Manhattan distance between the current state and the goal state
   # It is admissible because it never overestimates the cost to reach the goal
   # It is consistent because the estimated cost from the current state to the goal can never be greater than the sum of the cost from the current node to a successor node plus the estimated cost from the successor node to the goal
   return sum(abs(int(state[i][j]) - int(goal_state[i][j])) for i in range(len(state)) for j in range(len(state[0])) if state[i][j] != '_' and goal_state[i][j] != '_')


print(a_star())
