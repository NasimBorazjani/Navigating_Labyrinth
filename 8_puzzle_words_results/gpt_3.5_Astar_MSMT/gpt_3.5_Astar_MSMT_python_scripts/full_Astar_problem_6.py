
import heapq

def initialize():
   # Define the initial state of the board and the target words
   initial_state = [['l', 'c', '_', 'o'], ['s', 'c', 'o', 'h'], ['d', 'y', 'a', 'e'], ['h', 's', 'l', 't']]
   target_words = ['cho', 'slod', 'syce', 'halt']

   # Encoding other variables of the problem
   num_rows = len(initial_state)
   num_cols = len(initial_state[0])

   visited_costs = {}
   visited_costs[str(initial_state)] = 0

   queue = []

   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state))
  
   return initial_state, target_words, num_rows, num_cols, visited_costs, queue
  
def a_star():
  
   initial_state, target_words, num_rows, num_cols, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heapq.heappop(queue)

       # Check if the current state is the goal state, where each row spells the corresponding target word
       if all(''.join(row) == target_words[i] for i, row in enumerate(state)):
           return actions

       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == '_':
                   for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                       new_row, new_col = i + d_row, j + d_col
                       # Check if the new coordinate is within the bounds of the board
                       if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                           # Generate the new state after swapping the blank space with the neighboring tile
                           new_state = [list(row[:]) for row in state]
                           new_state[i][j], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[i][j]
                           new_state = str(new_state)
                           # The cost to reach the new state is increased by 1 as each swap is considered to be of equal cost
                           new_cost = g + 1

                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of unvisited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (g + 1, g + 1, actions + [(i, j, new_row, new_col)], eval(new_state))
   return None

print(a_star())
