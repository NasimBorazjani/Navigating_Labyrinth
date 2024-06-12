
import heapq


def initialize():
   # Define the initial state of the board and the target words
   initial_state = [['k', 'h', 'a', 't'], ['s', 'a', 'a', 'a'], ['i', 'l', '_', 't'], ['m', 'g', 'n', 'd']]
   target_words = ['hat', 'skag', 'alit', 'mand']
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
       if state == target_words:
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for row_diff in [-1, 0, 1]:
           for col_diff in [-1, 1]:
               # Check if the new state would be valid, ie the swap must not result in the blank space being out of the board
               if 0 <= state[0][0] + row_diff < num_rows and 0 <= state[0][1] + col_diff < num_cols:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   new_state[state[0][0]][state[0][1]], new_state[state[0][0] + row_diff][state[0][1] + col_diff] = new_state[state[0][0] + row_diff][state[0][1] + col_diff], new_state[state[0][0]][state[0][1]]
                   new_state = [tuple(row) for row in new_state]
                   # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The heuristic function can be a simple count of the number of characters that are not in their correct positions in the new state
                       h = heuristic(new_state, target_words)
                       # The direction of the swap is added to the actions taken
                       heappush(queue, (new_cost + h, new_cost, actions + [(row_diff, col_diff)], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a simple count of the number of characters that are not in their correct positions in the new state
   h = sum(state[i][j] != target_words[i][j] for i in range(len(state)) for j in range(len(state[i])))
   return h


print(a_star())
