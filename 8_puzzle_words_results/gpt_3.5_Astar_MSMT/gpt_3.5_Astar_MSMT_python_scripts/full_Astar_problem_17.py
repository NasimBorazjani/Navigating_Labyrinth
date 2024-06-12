
import heapq

def initialize():
   # Define the target words and initial state of the board
   target_words = ['hay', 'werf', 'rudd', 'frib']
   initial_board = [['e', 'h', 'r', 'y'],
                   ['w', 'f', 'r', 'r'],
                   ['_', 'u', 'd', 'd'],
                   ['f', 'a', 'i', 'b']]
   num_rows = 4
   num_cols = 4

   visited_costs = {}
   visited_costs[str(initial_board)] = 0

   queue = [(0, 0, [], initial_board)]
  
   return target_words, initial_board, num_rows, num_cols, visited_costs, queue
  
def a_star():
  
   target_words, initial_board, num_rows, num_cols, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heapq.heappop(queue)

       # Unpack the initial board to access the position of the blank space
       blank_row, blank_col = [(i, j) for i, row in enumerate(state) for j, tile in enumerate(row) if tile == '_'][0]

       # Convert the state to a string to store the visited states
       state_str = str(state)

       # If the current state spells out the target words, return the actions taken
       if all(''.join(row).replace('_', '') == word for row, word in zip(state, target_words)):
           return actions

       # Generate all possible actions from the current state, which includes swapping the blank space with its 4 diagonal neighboring tiles
       for dr, dc in [(1, -1), (1, 1), (-1, -1), (-1, 1)]:
           new_row, new_col = blank_row + dr, blank_col + dc
           # Check if the new position of the blank space is within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state by swapping the blank space with the neighboring tile
               new_state = [list(row) for row in state]
               new_state[blank_row][blank_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_row][blank_col]
               new_state_str = str(new_state)
               # The cost of moving to the new state is 1, as each swap action costs 1
               new_cost = g + 1

               if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                   visited_costs[new_state_str] = new_cost
                   heapq.heappush(queue, (g + 1, new_cost, actions + [(dr, dc)], new_state))
   return None

print(a_star())
