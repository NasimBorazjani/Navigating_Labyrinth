
import heapq

def initialize():
   # Define the initial state of the board
   initial_board = [['o', 'j', '_', 'h', 'u'], 
                    ['w', 'l', 'r', 'e', 'y'], 
                    ['n', 'i', 'l', 't', 'a'], 
                    ['i', 'y', 'i', 'm', 'l']]
   num_rows = 4
   num_cols = 5
   target_words = ['jehu', 'wormy', 'linty', 'ilial']

   visited_costs = {}
   visited_costs[tuple(map(tuple, initial_board))] = 0

   queue = []
   # No actions taken in the initial state
   heapq.heappush(queue, (0, 0, [], initial_board))

   return initial_board, num_rows, num_cols, target_words, visited_costs, queue

def a_star():
  
   initial_board, num_rows, num_cols, target_words, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heapq.heappop(queue)

       # Check if the current state is the goal state where the rows spell out the words in the target list
       current_words = [''.join(row).replace('_', '') for row in state]
       if current_words == target_words:
           return actions

       # Generate all possible actions from the current state, which is swapping the blank space with any of its 4 diagonal neighboring tiles
       for d_row, d_col in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
           new_row = None
           new_col = None
           for r in range(num_rows):
               for c in range(num_cols):
                   if state[r][c] == '_':
                       new_row = r + d_row
                       new_col = c + d_col
                       break
               if new_row is not None:
                   break
          
           # Check if the new position of the blank space is within the boundaries of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Perform the swapping by creating a new board state
               new_state = [list(row) for row in state]
               new_state[new_row][new_col], new_state[r][c] = new_state[r][c], new_state[new_row][new_col]
               new_state = tuple(map(tuple, new_state))
               # The cost of the new state is 1, as each swap is considered as 1 move
               new_cost = g + 1
  
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (g + 1, new_cost, actions + [(d_row, d_col)], new_state))

   return None

print(a_star())
