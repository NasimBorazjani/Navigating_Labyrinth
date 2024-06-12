
import heapq


def initialize():
   # Define the initial state of the board, with '_' representing the blank space
   initial_state = (['a', 'r', '_', 'c'], ['h', 'a', 'v', 'e'], ['a', 'g', 's', 'd'], ['b', 'i', 't', 'z'])
   num_rows = 4
   num_cols = 4
   target_words = ['ric', 'have', 'sgad', 'batz']


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, target_words, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, target_words, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == tuple(word[i] if i < len(word) else '_' for word in target_words for i in range(num_cols)):
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for d_row, d_col in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
           new_row, new_col = state.index('_') + d_row, state.index('_') + d_col
           # Check if the new coordinate is valid, ie if the new position is within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[state.index('_')][state.index('_')], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[state.index('_')][state.index('_')]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic function can be a simple count of the number of characters in the current state that are not in their correct position in the goal state
                   h = heuristic(state, target_words)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [(state.index('_'), new_row, new_col)], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a simple count of the number of characters in the current state that are not in their correct position in the goal state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a character is moved away from its correct position, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum number of swaps that can be made is by moving a character to its correct position, which is exactly the character used to fill the blank space in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i, row in enumerate(state):
       for j, char in enumerate(row):
           if char != target_words[i][j]:
               h += 1
   return h


print(a_star())
