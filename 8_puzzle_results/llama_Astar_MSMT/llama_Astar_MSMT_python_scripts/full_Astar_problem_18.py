
import heapq


def initialize():
   # Define the initial state of the puzzle as a 2d tuple
   initial_state = (('88', '52', '85'),
                   ('98', '96', '83'),
                   ('50', '80', '_'))
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


       # Generate all possible actions from the current state, which includes swapping the empty spot with any of the 8 neighboring tiles
       for row_shift in [-1, 0, 1]:
           for col_shift in [-1, 0, 1]:
               # Check if the new state would be valid, ie the new state must not have the empty spot out of the grid or adjacent to another empty spot
               if 0 <= state[0].index('_') + row_shift < num_rows and 0 <= state[0].index('_') + col_shift < num_cols and (row_shift != 0 or col_shift != 0):
                   temp_state = [list(row) for row in state]
                   # Swap the empty spot with the tile in the new position
                   temp_state[state[0].index('_') + row_shift][state[0].index('_') + col_shift], temp_state[state[0].index('_')][state[0].index('_')] = temp_state[state[0].index('_')][state[0].index('_')], temp_state[state[0].index('_') + row_shift][state[0].index('_') + col_shift]
                   # Generate the new state
                   new_state = tuple(tuple(row) for row in temp_state)
                   # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to solve the puzzle
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(state, goal_state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [int(state[state[0].index('_') + row_shift][state[0].index('_') + col_shift])], new_state))
   return None




def heuristic(state, goal_state):
   # The heuristic function can be the Manhattan distance between the current state and the goal state
   # This heuristic is admissible because it is a lower bound on the cost to reach the goal
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of the cost from the current node to a successor node plus the estimated cost from the successor node to the goal
   return sum(abs(state[i].index('_') - goal_state[i].index('_')) for i in range(len(state)))


print(a_star())
