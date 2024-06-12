
import heapq


def a_star():
   # Define the initial state of the board
   initial_state = (['o', 'c', 'a', 'a', 'n', 'k'],
                   ['h', 'm', 'r', 'l', 'i', 'g'],
                   ['h', 'i', 'o', 't', 'u', 'g'],
                   ['t', 'n', 'r', 't', 'a', 'c'],
                   ['z', 'y', 't', 'h', '_', 'm'])
   num_rows = 5
   num_cols = 6
   target_words = ['chank', 'hormic', 'tigtag', 'tornal', 'zythum']


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == tuple(word[::-1] for word in target_words):
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for row_shift, col_shift in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
           new_row, new_col = state.index('_') + row_shift, state.index('_') + col_shift
           # Check if the new state would be valid, ie the new row and column must be within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[state.index('_')][state.index('_')], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[state.index('_')][state.index('_')]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(state, target_words)
                   # In the problem statement the directions are indexed starting from 1, thus must add 1 to the direction
                   heappush(queue, (new_cost + h, new_cost, actions + [(row_shift, col_shift)], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a simulation of swapping the blank space greedily, using the next closest character as the blank space repeatedly
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the board the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a character is swapped with the blank space, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of swaps that can be made is by using the closest character to the blank space, which is exactly the character used to swap with the blank space in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] == '_':
               continue
           min_dist = float('inf')
           for k in range(len(state)):
               for l in range(len(state[k])):
                   if state[k][l] != '_':
                       dist = abs(i - k) + abs(j - l)
                       if dist < min_dist:
                           min_dist = dist
           h += min_dist
   return h


print(a_star())
