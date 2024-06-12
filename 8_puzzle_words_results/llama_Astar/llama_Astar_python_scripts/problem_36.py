
import heapq


def a_star():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('h', 'b', 'c', 't', 'h'),
                   ('k', 'n', 'i', 'o', 'a'),
                   ('a', 's', '_', 'o', 'a'),
                   ('c', 'l', 'a', 's', 't'))
   target_words = ['bath', 'khila', 'ascon', 'coast']
   num_rows = 4
   num_cols = 5


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if all(state[i][1:] == list(target_words[i]) for i in range(num_rows)):
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] == '_':
                   for new_row, new_col in [(row - 1, col - 1), (row - 1, col + 1), (row + 1, col - 1), (row + 1, col + 1)]:
                       # Check if the new position is valid
                       if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the number of swaps made
                           new_cost = g + 1


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               # The direction of the swap is the direction in which the blank space was swapped
                               direction = (new_row - row, new_col - col)
                               heapq.heappush(queue, (new_cost + heuristic(state, target_words), new_cost, actions + [direction], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a count of the number of characters in the current state that are not in their correct positions in the target state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a character is moved away from its correct position in the target state, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum number of swaps that can be made to move a character to its correct position in the target state is by swapping it with a character that is in its correct position in the target state, which is exactly the character used to swap it in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != '_' and state[i][j] != target_words[i][j - 1]:
               h += 1
   return h


print(a_star())
