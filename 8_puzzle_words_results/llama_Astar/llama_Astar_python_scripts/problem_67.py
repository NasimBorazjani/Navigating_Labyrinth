
import heapq


def a_star():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('e', 'l', 'u', 'w'),
                   ('k', 'k', 'c', 'e'),
                   ('f', 'l', '_', 'a'),
                   ('s', 'r', 's', 'e'),
                   ('h', 'e', 'u', 'b'))
   num_rows = 5
   num_cols = 4
   target_words = ['lew', 'keck', 'flea', 'susu', 'herb']


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == tuple(word[::-1] for word in target_words):
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for dr, dc in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
           new_row, new_col = state[1][1] + dr, state[1][1] + dc
           # Check if the new position of the blank space is valid, ie it must be within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[1][1], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[1][1]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic function can be a simple count of the number of characters in the wrong position in the current state
                   h = heuristic(state, target_words)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [(dr, dc)], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a simple count of the number of characters in the wrong position in the current state
   h = 0
   for i, word in enumerate(target_words):
       for j, char in enumerate(word):
           if state[i][j] != char:
               h += 1
   return h


print(a_star())
