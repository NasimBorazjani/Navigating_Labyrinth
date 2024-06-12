
import heapq


def initialize():
   # Define the initial state of the 8-puzzle, with '_' representing the empty spot
   initial_state = (('41', '36', '82'),
                   ('29', '97', '43'),
                   ('_', '51', '61'))
   num_rows = 3
   num_cols = 3
   goal_state = (('8', '7', '6'),
                 ('5', '4', '3'),
                 ('2', '1', '_'))


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, goal_state, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, goal_state, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken to reach it
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes swapping the empty spot with any of the 8 neighboring spots
       for row_shift in [-1, 0, 1]:
           for col_shift in [-1, 0, 1]:
               if row_shift != 0 or col_shift != 0:
                   new_state = [list(row[:]) for row in state]
                   empty_row, empty_col = [i for i, row in enumerate(state) for j, cell in enumerate(row) if cell == '_'][0]
                   new_state[empty_row][empty_col], new_state[empty_row + row_shift][empty_col + col_shift] = new_state[empty_row + row_shift][empty_col + col_shift], new_state[empty_row][empty_col]
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to solve the puzzle
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(new_state, goal_state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [int(new_state[empty_row][empty_col])], new_state))
   return None




def heuristic(state, goal_state):
   # The heuristic function can be the Manhattan distance between the current state and the goal state
   # This heuristic is admissible because it is a lower bound on the cost to reach the goal state
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of the cost from the current node to a successor node plus the estimated cost from the successor node to the goal
   return sum(abs(int(state[i][j]) - int(goal_state[i][j])) for i in range(len(state)) for j in range(len(state[0])) if state[i][j] != '_' and goal_state[i][j] != '_')


print(a_star())