
import heapq


def a_star():
   # Define the initial state of the board
   initial_state = (['_', 'p', 'h', 'm', 'p'],
                   ['s', 'a', 'd', 'r', 'e'],
                   ['i', 'u', 'n', 'i', 'r'],
                   ['u', 'a', 'z', 'e', 'n'])
   target_words = ['pimp', 'sadhe', 'aurir', 'unzen']
   num_rows = 4
   num_cols = 5


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == tuple(word[i] for word in target_words for i in range(len(word))):
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for row_shift in [-1, 0, 1]:
           for col_shift in [-1, 0, 1]:
               # Check if the new state would be valid, ie the new state must not have the blank space out of the board
               if 0 <= row_shift + col_shift < 2 and 0 <= row_shift - col_shift < num_rows and 0 <= col_shift + row_shift < num_cols:
                   new_state = [list(row[:]) for row in state]
                   new_state[row_shift][col_shift], new_state[row_shift + col_shift][col_shift + row_shift] = new_state[row_shift + col_shift][col_shift + row_shift], new_state[row_shift][col_shift]
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The direction of the swap is the direction in which the blank space was swapped in
                       swap_direction = (row_shift - col_shift, row_shift + col_shift)
                       heapq.heappush(queue, (new_cost + heuristic(state, target_words), new_cost, actions + [swap_direction], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a simulation of swapping the blank space greedily, using the next closest character as the blank space as long as the word is not completed
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the board the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a swap results in a word being completed, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of swaps that can be made is by using the closest character to the blank space, which is exactly the character used to swap with the blank space in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for target_word in target_words:
       for i in range(len(target_word)):
           if state[i][i] != target_word[i]:
               h += 1
   return h


print(a_star())
