
import heapq


def initialize():
   # Define the initial state of the board and the target words
   initial_state = [['b', 'l', '_', 'g'], ['a', 'n', 'a', 's'], ['m', 'u', 'a', 'a'], ['s', 'h', 'a', 'm']]
   target_words = ['lag', 'abas', 'numa', 'sham']


   # Define the dimensions of the board
   num_rows = 4
   num_cols = 4


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, target_words, num_rows, num_cols, visited_costs, queue
  
def a_star():
  
   initial_state, target_words, num_rows, num_cols, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == [list(word) for word in target_words]:
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for row_diff in [-1, 0, 1]:
           for col_diff in [-1, 1]:
               new_state = [list(row) for row in state]
               blank_row, blank_col = [i for i, row in enumerate(state) for j, cell in enumerate(row) if cell == '_'][0]
               new_blank_row, new_blank_col = blank_row + row_diff, blank_col + col_diff
               # Check if the new state is valid, ie the new blank tile must be within the bounds of the board
               if 0 <= new_blank_row < num_rows and 0 <= new_blank_col < num_cols:
                   # Swap the blank spaces in the new state
                   new_state[blank_row][blank_col], new_state[new_blank_row][new_blank_col] = new_state[new_blank_row][new_blank_col], new_state[blank_row][blank_col]
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required to sort the board
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The heuristic function is not needed in this problem as the goal state is always reachable and the cost to reach the goal is the minimum possible
                       heapq.heappush(queue, (new_cost, new_cost, actions + [(blank_row, blank_col, new_blank_row, new_blank_col)], new_state))
   return None


print(a_star())
