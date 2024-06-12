
import heapq

def initialize():
   # Define the target words and initial state of the board
   target_words = ['hat', 'skag', 'alit', 'mand']
   initial_state = [['k', 'h', 'a', 't'], ['s', 'a', 'a', 'a'], ['i', 'l', '_', 't'], ['m', 'g', 'n', 'd']]
   num_rows = len(initial_state)
   num_cols = len(initial_state[0])

   visited_costs = {}
   visited_costs[str(initial_state)] = 0

   queue = []
   queue.append((0, 0, [], initial_state))
  
   return target_words, initial_state, num_rows, num_cols, visited_costs, queue

def a_star():
   target_words, initial_state, num_rows, num_cols, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heapq.heappop(queue)

       # Convert the state to a string to use it as a key in the visited_costs dictionary
       state_str = str(state)

       # Check if the current state matches the target words
       if all(''.join(row).replace('_', '') == target_words[i] for i, row in enumerate(state)):
           return actions

       # Find the position of the blank space
       blank_row, blank_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == '_'][0]

       # Generate all possible actions from the current state, which includes moving the blank space in any diagonal direction
       for d_row, d_col in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
           new_row, new_col = blank_row + d_row, blank_col + d_col
           # Check if the new position is within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state by swapping the blank space with the tile in the diagonal direction
               new_state = [list(row) for row in state]
               new_state[blank_row][blank_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_row][blank_col]
               # Calculate the new cost and update the visited states
               new_state_str = str(new_state)
               new_cost = g + 1
               if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                   visited_costs[new_state_str] = new_cost
                   heapq.heappush(queue, (g + 1, new_cost, actions + [(d_row, d_col)], new_state))

   return None

print(a_star())
