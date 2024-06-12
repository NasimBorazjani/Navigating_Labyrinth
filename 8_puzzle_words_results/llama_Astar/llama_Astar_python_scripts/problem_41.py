
import heapq


def a_star():
   # Define the initial state of the board
   initial_state = (['o', 'a', '_', 'i', 't', 's'],
                   ['d', 'r', 'o', 'o', 'o', 'a'],
                   ['c', 'e', 'm', 'i', 'l', 'e'],
                   ['c', 'c', 'm', 't', 'i', 'e'])
   target_words = ['alias', 'doocot', 'cerite', 'commie']
   num_rows = 4
   num_cols = 6


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == tuple(list(word) for word in target_words):
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for row_shift in [-1, 0, 1]:
           for col_shift in [-1, 1]:
               new_state = [list(row[:]) for row in state]
               blank_row, blank_col = next(i for i, cell in enumerate(new_state[0]) if cell == '_')
               new_state[0][blank_row], new_state[0][blank_col] = new_state[0][blank_col], new_state[0][blank_row]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(state, target_words)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [(row_shift, col_shift)], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a count of the number of characters in the current state that are not in their correct positions in the goal state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a character is moved away from its correct position, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of characters that can be moved to their correct positions in the heuristic is by moving the characters that are currently in their correct positions, which is exactly the characters used to fill the board in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(num_rows):
       for j in range(num_cols):
           if state[i][j] != target_words[i][j - i]:
               h += 1
   return h


print(a_star())
