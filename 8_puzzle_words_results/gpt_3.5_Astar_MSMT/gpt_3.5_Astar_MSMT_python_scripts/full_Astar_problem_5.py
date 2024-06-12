
import heapq

def initialize():
   # Define the initial state of the board, target words, and other variables
   initial_state = [['a', 's', 't', 'x'], ['t', 'r', 's', 'a'], ['s', 'u', '_', 'p'], ['c', 'a', 'd', 'e']]
   target_words = ['sax', 'tass', 'turp', 'cade']
   num_rows = 4
   num_cols = 4

   visited_costs = {}
   visited_costs[str(initial_state)] = 0

   # Initialize a priority queue to store the states not yet visited, with the initial state as the first element
   # The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, target_words, num_rows, num_cols, visited_costs, queue


def a_star():
  
   initial_state, target_words, num_rows, num_cols, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)

       # Check if the current state is the goal state, where each row spells out the corresponding word
       if all(''.join(row) == target_words[i] for i, row in enumerate(state)):
           return actions

       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for d_row, d_col in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
           new_row, new_col = None, None
           # Find the position of the blank space in the current state
           for i in range(num_rows):
               for j in range(num_cols):
                   if state[i][j] == '_':
                       new_row, new_col = i + d_row, j + d_col
                       break
               if new_row is not None:
                   break
           # Check if the new position is within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state by swapping the blank space with the neighboring tile
               new_state = [list(row) for row in state]
               new_state[new_row][new_col], new_state[i][j] = new_state[i][j], new_state[new_row][new_col]
               new_state = str(new_state)  # Convert the new state to a string to use it as a key in the visited_costs dictionary
               # The cost to reach the new state is the number of swaps made, as the task is to minimize the number of swaps required
               new_cost = g + 1

               # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of unvisited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (g + 1, new_cost, actions + [(d_row, d_col)], new_state))
   return None


print(a_star())
