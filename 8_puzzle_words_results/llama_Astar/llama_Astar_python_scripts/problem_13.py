
import heapq


def a_star():
   # Define the initial state of the board
   initial_state = (['b', 'l', '_', 'g'],
                   ['a', 'n', 'a', 's'],
                   ['m', 'u', 'a', 'a'],
                   ['s', 'h', 'a', 'm'])
   # Define the target words
   target_words = ['lag', 'abas', 'numa', 'sham']
   # Define the possible swap directions
   swap_directions = ['ur', 'dr', 'ul', 'dl']
   # Define the dimensions of the board
   num_rows = 4
   num_cols = 4


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == tuple(list(word) for word in target_words):
           return actions


       # Generate all possible actions from the current state
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] == '_':
                   for swap_direction in swap_directions:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       # Swap the blank space with its neighbor in the given direction
                       if swap_direction == 'ur':
                           new_state[row][col], new_state[row - 1][col + 1] = new_state[row - 1][col + 1], new_state[row][col]
                       elif swap_direction == 'dr':
                           new_state[row][col], new_state[row + 1][col + 1] = new_state[row + 1][col + 1], new_state[row][col]
                       elif swap_direction == 'ul':
                           new_state[row][col], new_state[row - 1][col - 1] = new_state[row - 1][col - 1], new_state[row][col]
                       elif swap_direction == 'dl':
                           new_state[row][col], new_state[row + 1][col - 1] = new_state[row + 1][col - 1], new_state[row][col]
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the number of swaps made
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is the number of characters in the current state that are not in their correct position in the goal state
                           h = heuristic(state, target_words)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(row, col, swap_direction)], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be the number of characters in the current state that are not in their correct position in the goal state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a character is moved away from its correct position, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum number of swaps that can be made to move a character to its correct position is by 1
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != target_words[i][j - (i > 0)]:
               h += 1
   return h


print(a_star())
