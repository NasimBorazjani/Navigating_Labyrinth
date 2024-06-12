
import heapq

def initialize():
   # Define the initial state of the board, where the blank space is represented as '_'
   initial_state = [['m', 'p', 'l', 's', 's'],
                    ['s', 'a', 'o', 's', 'e'],
                    ['c', 'a', '_', 'e', 'k'],
                    ['h', 'i', 'r', 'o', 'm']]
  
   # Define the target words that we need to rearrange the board to form
   target_words = ['poss', 'smoke', 'casel', 'hiram']
  
   # Encoding other variables given in the problem
   num_rows = len(initial_state)
   num_cols = len(initial_state[0])
   blank_space = '_'

   visited_costs = {}
   visited_costs[tuple(tuple(row) for row in initial_state)] = 0

   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, target_words, num_rows, num_cols, blank_space, visited_costs, queue


def a_star():
  
   initial_state, target_words, num_rows, num_cols, blank_space, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heapq.heappop(queue)

       # Check if the current state is the goal state, ie the words formed in each row match the corresponding target words
       if all(''.join(row) == target_words[i] for i, row in enumerate(state)):
           return actions

       # Find the position of the blank space in the current state
       blank_position = [(i, row.index(blank_space)) for i, row in enumerate(state) if blank_space in row][0]

       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
       for d_row, d_col in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
           new_row, new_col = blank_position[0] + d_row, blank_position[1] + d_col
           # Check if the new position is within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state by swapping the blank space with the neighbor
               new_state = [list(row[:]) for row in state]
               new_state[blank_position[0]][blank_position[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_position[0]][blank_position[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost of this state is 1, as each swap action costs 1
               new_cost = g + 1

               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # Estimate the cost to reach the goal state by counting the number of characters that are not in the correct position in each row
                   h = sum(sum(a != b for a, b in zip(row, target_words[i])) for i, row in enumerate(new_state))
                   heapq.heappush(queue, (g + h, new_cost, actions + [(d_row, d_col)], new_state))
   return None

print(a_star())
