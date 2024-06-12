
def initialize():
   # Define the initial state of the board, the list of target words, and other variables given in the problem
   initial_state = [['_', 's', 'a', 'n'],
                    ['q', 'u', 'o', 'u'],
                    ['c', 'h', 'u', 't'],
                    ['l', 't', 'r', 'e']]
   target_words = ['sun', 'quot', 'chat', 'lure']
   num_rows = 4
   num_cols = 4

   visited_costs = {}
   visited_costs[tuple(tuple(row) for row in initial_state)] = 0

   queue = []

   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   # Encode the initial state as a tuple of tuples for immutability
   queue.append((0, 0, [], tuple(tuple(row) for row in initial_state)))

   return initial_state, target_words, num_rows, num_cols, visited_costs, queue

def a_star():
  
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the board, target words, number of rows and columns of the board)
   initial_state, target_words, num_rows, num_cols, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = queue.pop(0)

       # Unpack the state to a list for easier manipulation
       state_list = [list(row) for row in state]

       # Check if the current state matches the target words
       if all(''.join(row).replace('_', '') == target_words[i] for i, row in enumerate(state)):
           return actions

       # Find the position of the blank space
       blank_row, blank_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state_list[i][j] == '_'][0]

       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
           new_row, new_col = blank_row + d_row, blank_col + d_col
           # Check if the new position is within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Perform the swap
               state_list[blank_row][blank_col], state_list[new_row][new_col] = state_list[new_row][new_col], state_list[blank_row][blank_col]
               new_state = tuple(tuple(row) for row in state_list)
               # Cost of the new state is the number of swaps made, as the task is to minimize the number of swaps required
               new_cost = g + 1

               # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of unvisited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   queue.append((g + 1, new_cost, actions + [(d_row, d_col)], new_state))

               # Swap back to original state to explore other paths
               state_list[blank_row][blank_col], state_list[new_row][new_col] = state_list[new_row][new_col], state_list[blank_row][blank_col]

   return None

print(a_star())
