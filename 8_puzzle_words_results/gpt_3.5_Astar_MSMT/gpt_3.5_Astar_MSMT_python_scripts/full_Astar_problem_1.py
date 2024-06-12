
import heapq

def initialize():
   # Define the initial state of the board as a 2d list
   initial_state = [['i', 'c', 'a', 'm'], ['h', 'p', 'l', 'o'], ['_', 'r', 'a', 'y'], ['d', 'l', 'e', 'r']]
   num_rows = 4
   num_cols = 4
   target_words = ['cam', 'hill', 'pray', 'doer']

   visited_costs = {}
   visited_costs[str(initial_state)] = 0

   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, target_words, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, target_words, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heapq.heappop(queue)

       # If the current state is the goal state, where each row spells the corresponding word in the target list, return the actions taken
       if all(''.join(row) == word for row, word in zip(state, target_words)):
           return actions

       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == '_':
                   for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                       new_row, new_col = i + d_row, j + d_col
                       # Check if the new coordinate is within the bounds of the board
                       if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                           # Generate the new state by swapping the blank space with the neighbor
                           new_state = [list(row) for row in state]
                           new_state[i][j], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[i][j]
                           new_state_str = str(new_state)
                           # The cost of the new state is the number of swaps made, as the task is to minimize the number of swaps required to reach the goal state
                           new_cost = g + 1

                           if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                               visited_costs[new_state_str] = new_cost
                               heapq.heappush(queue, (g + 1, new_cost, actions + [(i, j, new_row, new_col)], new_state))
   return None

print(a_star())
