
import heapq

def initialize():
   # Define the target words and initial state of the board as a 2d tuple
   target_words = ['pimp', 'sadhe', 'aurir', 'unzen']
   initial_state = [['_', 'p', 'h', 'm', 'p'],
                    ['s', 'a', 'd', 'r', 'e'],
                    ['i', 'u', 'n', 'i', 'r'],
                    ['u', 'a', 'z', 'e', 'n']]

   num_rows = 4
   num_cols = 5

   visited_costs = {}
   visited_costs[str(initial_state)] = 0

   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state))
  
   return target_words, initial_state, num_rows, num_cols, visited_costs, queue


def a_star():
  
   target_words, initial_state, num_rows, num_cols, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, where each row spells the corresponding word
       current_words = [''.join(row).replace('_', '') for row in state]
       if current_words == target_words:
           return actions

       # Find the coordinates of the blank space '_'
       blank_row, blank_col = [(i, j) for i, row in enumerate(state) for j, letter in enumerate(row) if letter == '_'][0]

       # Generate all possible actions by swapping the blank space with any of its 4 diagonal neighboring tiles
       for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
           new_row, new_col = blank_row + d_row, blank_col + d_col
           # Check if the new coordinate is valid, ie within the bounds of the table
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state after swapping
               new_state = [list(row) for row in state]
               new_state[new_row][new_col], new_state[blank_row][blank_col] = new_state[blank_row][blank_col], new_state[new_row][new_col]
               # For the purposes of this problem, a board state is uniquely identified by the characters of the board, hence stringifying the 2d list
               new_state_str = str(new_state)
               # The cost of the new state is the length of the target_words as the task is to minimize the number of letters out of place
               new_cost = g + sum(len(target_word) for target_word in target_words)

               if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                   visited_costs[new_state_str] = new_cost
                   heapq.heappush(queue, (g + 1, g + 1, actions + [(d_row, d_col)], new_state))
   return None

print(a_star())
