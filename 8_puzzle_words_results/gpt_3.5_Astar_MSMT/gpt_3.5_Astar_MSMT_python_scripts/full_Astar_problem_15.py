
import heapq

def initialize():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('a', 'r', '_', 'c'),
                      ('h', 'a', 'v', 'e'),
                      ('a', 'g', 's', 'd'),
                      ('b', 'i', 't', 'z'))
   num_rows = 4
   num_cols = 4
   target_words = ['ric', 'have', 'sgad', 'batz']

   visited_costs = {}
   visited_costs[initial_state] = 0

   queue = []
   # No actions taken in the initial state
   heapq.heappush(queue, (0, 0, [], initial_state))
  
   return initial_state, num_rows, num_cols, target_words, visited_costs, queue

def a_star():
  
   initial_state, num_rows, num_cols, target_words, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heapq.heappop(queue)

       # If the current state matches the target words, return the actions taken so far
       if all(''.join(row) == target_words[i] for i, row in enumerate(state)):
           return actions

       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for d_row, d_col in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
           new_row = None
           new_col = None
           # Find the coordinates of the blank space
           for i in range(num_rows):
               for j in range(num_cols):
                   if state[i][j] == '_':
                       new_row = i + d_row
                       new_col = j + d_col
                       break
               if new_row is not None:
                   break
           # Check if the new coordinates are within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state by swapping the blank space with the neighboring tile
               new_state = [list(row[:]) for row in state]
               new_state[new_row][new_col], new_state[i][j] = new_state[i][j], new_state[new_row][new_col]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost of moving is 1, as we are trying to minimize the number of swaps
               new_cost = g + 1

               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (g + 1, new_cost, actions + [(d_row, d_col)], new_state))
   return None

print(a_star())
