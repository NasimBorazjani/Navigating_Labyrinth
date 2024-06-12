
import heapq


def initialize():
   # Define the initial state of the puzzle
   initial_state = (['28', '51', '19'], ['89', '_', '21'], ['43', '39', '45'])
   num_rows = 3
   num_cols = 3


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state
       if state == (['8', '7', '6'], ['5', '4', '3'], ['2', '1', '_']):
           return actions


       # Generate all possible actions from the current state, which includes swapping the empty spot with any of the 8 neighboring tiles
       for row_shift, col_shift in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
           new_row, new_col = state[1].index('_') + row_shift, state[1].index('_') + col_shift
           # Check if the new state would be valid, ie the new state must be within the bounds of the grid
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[new_row][new_col], new_state[1][state[1].index('_')] = new_state[1][state[1].index('_')], new_state[new_row][new_col]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state[1][state[1].index('_')]], new_state))
   return None




def heuristic(state):
   # The heuristic function can be the Manhattan distance from the current state to the goal state
   # This heuristic is admissible because it is a lower bound on the actual cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if we move to a state that is further from the goal, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of tiles that can be moved to the empty spot is by moving the tile that is closest to the empty spot in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for row_ind, row in enumerate(state):
       for col_ind, cell in enumerate(row):
           if cell != '_':
               goal_row, goal_col = divmod(int(cell) - 1, num_cols)
               h += abs(row_ind - goal_row) + abs(col_ind - goal_col)
   return h


print(a_star())
