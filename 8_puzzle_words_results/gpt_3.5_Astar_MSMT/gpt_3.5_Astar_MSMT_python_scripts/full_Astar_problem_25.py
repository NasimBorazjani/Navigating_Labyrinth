
import heapq

def initialize():
   # Define the target words and initial state of the board
   target_words = ['guha', 'nisus', 'uncap', 'jough']
   initial_state = [['i', 'g', 'u', 'h', 'a'], ['n', 'o', 's', 'u', 's'], ['c', 'n', 'g', 'a', '_'], ['j', 'u', 'u', 'p', 'h']]
   num_rows = 4
   num_cols = 5

   visited_costs = {}
   visited_costs[str(initial_state)] = 0

   queue = [(0, 0, [], initial_state)]
  
   return initial_state, target_words, num_rows, num_cols, visited_costs, queue
  
def a_star():
  
   initial_state, target_words, num_rows, num_cols, visited_costs, queue = initialize()

   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)

       # Convert state to string to check if the current state is the goal state
       state_str = str(state)
       if all(''.join(row) == target_words[i] for i, row in enumerate(state)):
           return actions

       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == '_':
                   for d_row, d_col in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
                       new_i, new_j = i + d_row, j + d_col
                       # Check if the new coordinate is valid, ie within the bounds of the board
                       if 0 <= new_i < num_rows and 0 <= new_j < num_cols:
                           # Generate the new state by swapping the blank space with a neighboring tile
                           new_state = [list(row) for row in state]
                           new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the number of swaps made
                           new_cost = g + 1

                           # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of unvisited states
                           if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                               visited_costs[str(new_state)] = new_cost
                               heapq.heappush(queue, (g + heuristic(state, target_words), new_cost, actions + [(i, j, new_i, new_j)], new_state))
   return None


def heuristic(state, target_words):
   # An admissible and consistent heuristic for this problem calculates the total number of characters in the wrong position in each row, relative to the target words
   # This heuristic is admissible because the total number of characters in the wrong position can never be less than the number of swaps required to get to the goal state, so it never overestimates
   # It is consistent because making a swap from the current state to a successor node can only reduce the heuristic cost, as the characters get placed closer to their correct positions
   h = 0
   for i, row in enumerate(state):
       # Calculate the number of characters in the wrong position in the current row
       h += sum(1 for x, y in zip(row, target_words[i]) if x != y)
   return h


print(a_star())
