
import heapq

def initialize():
   # Define the initial state of the board
   initial_state = [['b', 'l', '_', 'g'],
                    ['a', 'n', 'a', 's'],
                    ['m', 'u', 'a', 'a'],
                    ['s', 'h', 'a', 'm']]
  
   # Define the target words
   target_words = ['lag', 'abas', 'numa', 'sham']
  
   # Encode other variables given in the problem
   num_rows = 4
   num_cols = 4

   visited_costs = {}
   visited_costs[str(initial_state)] = 0

   # Initialize a priority queue to keep track of states not yet visited
   queue = []
   # No actions are taken in the initial state
   heapq.heappush(queue, (0, 0, [], initial_state))
  
   return initial_state, target_words, num_rows, num_cols, visited_costs, queue


def a_star():
  
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the tubes, number of tubes, and capacity of each tube)
   initial_state, target_words, num_rows, num_cols, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)

       # Convert the state to a string to use as a key in the visited_costs dictionary
       state_str = str(state)

       # If the current state is the goal state (row i spells the i-th word in the list)
       if all(''.join(row) == word for row, word in zip(state, target_words)):
           return actions

       # Find the position of the blank space
       blank_pos = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == '_'][0]

       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
       for d_row, d_col in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
           new_row, new_col = blank_pos[0] + d_row, blank_pos[1] + d_col
           # Check if the new coordinate is valid, ie within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state by swapping the blank space with the neighboring tile
               new_state = [list(row) for row in state]
               new_state[blank_pos[0]][blank_pos[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_pos[0]][blank_pos[1]]
               # Convert the new state to a string to use as a key in the visited_costs dictionary
               new_state_str = str(new_state)
               # The cost of the new state is the number of actions taken so far, as the task is to minimize the number of swaps required
               new_cost = g + 1

               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of unvisited states
               if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                   visited_costs[new_state_str] = new_cost
                   heapq.heappush(queue, (g + 1, new_cost, actions + [(d_row, d_col)], new_state))
   return None


print(a_star())
