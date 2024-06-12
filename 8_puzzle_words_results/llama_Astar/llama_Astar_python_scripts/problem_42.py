
import heapq


def a_star():
   # Define the initial state of the board
   initial_state = (['_', 'j', 'a', 'r', 'e', 'b'],
                   ['z', 'o', 'y', 's', 'i', 'i'],
                   ['r', 'e', 'r', 's', 't', 'y'],
                   ['g', 'e', 'i', 'q', 'u', 'a'])
   target_words = ['jerib', 'zoysia', 'reesty', 'griqua']
   num_rows = 4
   num_cols = 6


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == tuple(list(word) for word in target_words):
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for row_shift in [-1, 0, 1]:
           for col_shift in [-1, 1]:
               # Check if the new state would be valid, ie the new state must not have the blank space out of the board
               if 0 <= row_shift + col_shift < num_rows and 0 <= row_shift - col_shift < num_cols:
                   new_state = [list(row[:]) for row in state]
                   new_state[row_shift][col_shift], new_state[row_shift + col_shift][col_shift + row_shift] = new_state[row_shift + col_shift][col_shift + row_shift], new_state[row_shift][col_shift]
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The heuristic function is not needed in this problem as the goal state is always reachable and the cost to reach the goal is always the same, ie the number of swaps made
                       heapq.heappush(queue, (new_cost, new_cost, actions + [(row_shift, col_shift)], new_state))
   return None


print(a_star())
