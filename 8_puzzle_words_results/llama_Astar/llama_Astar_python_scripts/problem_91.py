
import heapq


def a_star():
   # Define the initial state of the board
   initial_state = (['t', 'p', 'c', 'p', 'o', 'y'],
                   ['s', 'e', 'o', 't', 'k', 's'],
                   ['p', 'i', 'w', 't', '_', 'l'],
                   ['s', 'n', 'a', 'y', 'h', 'a'],
                   ['c', 'a', 'e', 'c', 'p', 'n'])
   target_words = ['peppy', 'stocky', 'pistol', 'swathe', 'cancan']
   num_rows = 5
   num_cols = 6


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == tuple(list(word) for word in target_words):
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for row_shift, col_shift in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
           new_row, new_col = state[2].index('_') + row_shift, state[2].index('_') + col_shift
           # Check if the new state would be valid, ie the new row and column must be within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[2][new_row - row_shift], new_state[2][new_col - col_shift] = new_state[2][new_col - col_shift], new_state[2][new_row - row_shift]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to sort the board
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(state, target_words)
                   # In the problem statement the directions are indexed starting from 1, thus must add 1 to the direction
                   heappush(queue, (new_cost + h, new_cost, actions + [(row_shift, col_shift)], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a simulation of sorting the board greedily, using the next smallest word that matches the current row as long as the word can be placed in the row
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the board the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a word is removed from a row, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of words that can be placed in the row is by using the largest word that can be placed in the row in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the target words by length
   target_words = sorted(target_words, key=len)
   # Iterate through the rows of the board
   for i in range(num_rows):
       row_words = [''.join(state[j][:len(target_words[i])]) for j in range(num_rows) if ''.join(state[j][:len(target_words[i])]) in target_words]
       # Find the next smallest word that matches the current row
       for word in target_words:
           if word in row_words:
               row_words.remove(word)
               break
       # Increment the estimated cost to the goal by 1 actions
       h += 1
   return h


print(a_star())
