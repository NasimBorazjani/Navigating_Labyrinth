
import heapq


def initialize():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('_', 'm', 'u', 'p'),
                   ('c', 'e', 'r', 'a'),
                   ('d', 'r', 'e', 'b'),
                   ('v', 'e', 'l', 'o'))
   num_rows = 4
   num_cols = 4
   target_words = ['map', 'cere', 'drub', 'velo']


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, target_words, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, target_words, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == tuple(word[i] for i, word in enumerate(target_words) for _ in word):
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for row_diff in [-1, 0, 1]:
           for col_diff in [-1, 1]:
               # Check if the new state would be valid, ie the new state must maintain the constraint that the blank space must be in the top left corner of the goal board
               if 0 <= state[row_diff][col_diff] == '_':
                   new_state = [list(row[:]) for row in state]
                   new_state[row_diff][col_diff], new_state[0][0] = new_state[0][0], new_state[row_diff][col_diff]
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The heuristic function is not needed in this problem as the goal state is always reachable with a finite number of swaps, and the cost of reaching the goal state is always less than or equal to the actual cost
                       heapq.heappush(queue, (new_cost, new_cost, actions + [(row_diff, col_diff)], new_state))
   return None


print(a_star())
