
import heapq

def initialize():
   # Define the initial state of the board and the list of target words
   initial_state = [['h', 'k', 't', 'n'], ['k', 'e', 'a', 'k'], ['e', 'i', '_', 'l'], ['w', 'l', 'n', 't']]
   target_words = ['ken', 'khat', 'kill', 'went']
  
   # Encoding other variables given in the problem statement
   num_rows = len(initial_state)
   num_cols = len(initial_state[0])

   visited_costs = {}
   visited_costs[str(initial_state)] = 0

   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, target_words, num_rows, num_cols, visited_costs, queue


def a_star():
  
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the board, target words, number of rows and columns, etc)
   initial_state, target_words, num_rows, num_cols, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heapq.heappop(queue)

       # Convert the state to a string to use as a key in the visited_costs dictionary
       state_str = str(state)

       # If the state is the goal state (the rows spell out the target words), return the actions taken
       if ["".join(row) for row in state] == target_words:
           return actions

       # Generate all possible actions from the current state, which includes swapping the blank space with its 4 diagonal neighbors
       for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
           new_row = None
           new_col = None
           for i in range(num_rows):
               for j in range(num_cols):
                   if state[i][j] == '_':
                       new_row = i + d_row
                       new_col = j + d_col
                       break
               if new_row is not None:
                   break
           # Check if the new position is valid and within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state by swapping the blank space with the character in the new position
               new_state = [list(row) for row in state]
               new_state[new_row][new_col], new_state[i][j] = new_state[i][j], new_state[new_row][new_col]
               # Convert the new state to a string to use as a key in the visited_costs dictionary
               new_state_str = str(new_state)
               # The cost of moving to the new state is 1, as the task is to minimize the number of swaps
               new_cost = g + 1

               # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of unvisited states
               if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                   visited_costs[new_state_str] = new_cost
                   heapq.heappush(queue, (g + 1, new_cost, actions + [(new_row, new_col, d_row, d_col)], new_state))
   return None

print(a_star())
