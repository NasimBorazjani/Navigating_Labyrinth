
import heapq


def initialize():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('o', 'g', 'h', 'a'),
                   ('y', 'c', 'd', 'l'),
                   ('o', 'a', '_', 'l'),
                   ('a', 'w', 'l', 'e'))
   num_rows = 4
   num_cols = 4
   target_words = ['goa', 'yodh', 'wall', 'acle']


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, target_words, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, target_words, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == tuple(word[::-1] for word in target_words):
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for row_shift, col_shift in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
           new_row, new_col = state.index('_') + row_shift, state.index('_') + col_shift
           # Check if the new state would be valid, ie the new state must be within the bounds of the board and the new position of the blank space must be a valid position
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[state.index('_')][state.index('_')] = new_state[new_row][new_col]
               new_state[new_row][new_col] = '_'
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required to sort the board
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(state, target_words)
                   # In the problem statement the directions are indexed starting from 1, thus must add 1 to the direction index
                   heappush(queue, (new_cost + h, new_cost, actions + [(row_shift, col_shift)], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a simulation of sorting the board greedily, using the next closest word as the goal for the next swap
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the board the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a swap results in a further word from the goal, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum distance that can be covered by the blank space in a swap is by using the largest possible shift, which is exactly the shift used to cover the blank space in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i, word in enumerate(target_words):
       for j, char in enumerate(word):
           current_char = state[i][j]
           if current_char != char:
               # The heuristic is the sum of the number of shifts required to move the blank space to the correct position in each word
               h += abs(state.index('_') - i) + abs(state.index('_') - j)
   return h


print(a_star())
