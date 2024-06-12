
import heapq


def initialize():
   # Define the initial state of the board, with '_' representing the blank space
   initial_state = (['_', 'a', 't', 'n'], ['b', 'i', 'r', 'n'], ['k', 'r', 'e', 'y'], ['b', 'a', 'l', 'i'])
   num_rows = 4
   num_cols = 4
   target_words = ['ann', 'birk', 'trey', 'bali']


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, target_words, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, target_words, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == tuple(word[::-1] for word in target_words):
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for row_shift, col_shift in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
           new_row, new_col = state[0].index('_') + row_shift, state[0].index('_') + col_shift
           # Check if the new state would be valid, ie the new_row and new_col must be within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[0][state[0].index('_')], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[0][state[0].index('_')]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic function is not needed in this problem as the goal state is always reachable and the cost of reaching the goal state is 0
                   heapq.heappush(queue, (new_cost, new_cost, actions + [(row_shift, col_shift)], new_state))
   return None


print(a_star())
