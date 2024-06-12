
import heapq

def initialize():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('u', 'k', 'd', 'x'),
                   ('t', 'e', 'r', 'b'),
                   ('w', 'a', '_', 'i'),
                   ('t', 'e', 's', 't'))
   num_rows = 4
   num_cols = 4

   visited_costs = {}
   visited_costs[initial_state] = 0

   # Encoding other variables of the problem
   num_words = 4
   words = ['kex', 'turd', 'wabi', 'test']

   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # The actions taken to reach the initial state are empty
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, visited_costs, num_words, words, queue


def a_star():
  
   initial_state, num_rows, num_cols, visited_costs, num_words, words, queue = initialize()

   while queue:
       _, g, actions, state = heapq.heappop(queue)

       # Unpack the current state to check if it matches the target words
       current_words = [''.join(row).replace('_', '') for row in state]
       if current_words == words:
           return actions

       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
           new_row, new_col = find_blank_space(state)
           new_row += d_row
           new_col += d_col
           # Check if the new coordinate is valid, ie within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state by swapping the blank space with the neighboring tile
               new_state = [list(row[:]) for row in state]
               new_state[new_row][new_col], new_state[find_blank_space(state)[0]][find_blank_space(state)[1]] = new_state[find_blank_space(state)[0]][find_blank_space(state)[1]], new_state[new_row][new_col]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost of reaching the new state is 1, as we are trying to minimize the number of swaps required
               new_cost = g + 1

               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (g + heuristic(new_state, words), new_cost, actions + [(new_row, new_col)], new_state))
   return None


def heuristic(state, words):
   # An admissible and consistent heuristic for this problem is the count of characters that are in the wrong position in the current state compared to the target words
   # This heuristic relaxes the constraint that only the blank space can be moved and that words can be spelled by rows, not columns
   # It is admissible because each move must result in at least one character moving towards the correct position, thus never overestimating the cost to reach the goal
   # It is consistent because moving a character into its correct position reduces the heuristic cost of the successor node by a max of 1 (if the moved character is in the wrong place in the target words but in the right place in the current state), which is equal to the cost of reaching the successor node
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] != '_' and state[i][j] != words[i][j]:
               h += 1
   return h


def find_blank_space(state):
   # Helper function to find the coordinates of the blank space in the current state
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] == '_':
               return i, j
   return None, None

print(a_star())
