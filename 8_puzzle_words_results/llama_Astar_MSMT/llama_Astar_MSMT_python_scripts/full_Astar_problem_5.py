
import heapq


def initialize():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('a', 's', 't', 'x'),
                   ('t', 'r', 's', 'a'),
                   ('s', 'u', '_', 'p'),
                   ('c', 'a', 'd', 'e'))
   num_rows = 4
   num_cols = 4
   target_words = ['sax', 'tass', 'turp', 'cade']


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, target_words, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, target_words, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == tuple(word.split() for word in target_words):
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for d_row, d_col in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
           new_row, new_col = state[3][1] + d_row, state[3][1] + d_col
           # Check if the new coordinate is valid, ie if the new position is within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[state[3][0]][state[3][1]], new_state[3][0], new_state[3][1] = new_state[3][0], new_state[new_row][new_col]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic function is not needed in this problem as the goal state is always reachable and the cost of reaching the goal is always known
                   heapq.heappush(queue, (new_cost, new_cost, actions + [(state[3][0], state[3][1], new_row, new_col)], new_state))
   return None


print(a_star())
