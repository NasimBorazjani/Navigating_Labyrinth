
import heapq


def a_star():
   # Define the initial state of the board
   initial_state = (['h', 'b', 'n', 's', 'i', 't'],
                   ['t', 'e', 'r', 'k', 'v', 'e'],
                   ['i', 'i', '_', 'c', 'o', 'b'],
                   ['h', 'u', 'm', 'a', 't', 'e'])
   target_words = ['besit', 'thrive', 'kincob', 'humate']
   num_rows = 4
   num_cols = 6


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == tuple(word[::-1] for word in target_words):
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for row_shift in [-1, 0, 1]:
           for col_shift in [-1, 1]:
               # Check if the new state would be valid, ie the new state must not have the blank space out of the board
               if 0 <= state[0].index('_') + row_shift < num_rows and 0 <= state[0].index('_') + col_shift < num_cols:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   new_state[state[0].index('_') + row_shift][state[0].index('_') + col_shift], new_state[state[0].index('_')][state[0].index('_')] = new_state[state[0].index('_')][state[0].index('_')], new_state[state[0].index('_') + row_shift][state[0].index('_') + col_shift]
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to sort the board
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(state, target_words)
                       # In the problem statement the directions are indexed starting from 1, thus must add 1 to the direction
                       direction = (row_shift, col_shift)
                       heappush(queue, (new_cost + h, new_cost, actions + [direction], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a simulation of sorting the board greedily, using the next smallest word that can be sorted with the current state
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the board the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a word cannot be sorted with the current state, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of words that can be sorted with the current state is by using the smallest word that can be sorted with the current state. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the target words by their current distance from being sorted in the state
   target_words = sorted(target_words, key=lambda word: sum(state[i][j] != word[i - j] for i in range(len(state)) for j in range(len(word))))
   for word in target_words:
       # Check if the word can be sorted with the current state
       if all(state[i][j] == word[i - j] for i in range(len(state)) for j in range(len(word))):
           break
       h += 1
   return h


print(a_star())
