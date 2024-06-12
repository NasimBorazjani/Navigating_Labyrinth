
import heapq


def a_star():
   # Define the initial state of the board
   initial_state = (['r', 's', 'w', 'o', 'g'],
                   ['t', 'n', 'e', 'm', 'a'],
                   ['m', 'o', '_', 'u', 's'],
                   ['a', 'w', 'i', 'r', 'i'])
   target_words = ['snog', 'trema', 'mosur', 'awiwi']
   num_rows = 4
   num_cols = 5
   # Define the possible swap directions
   swap_directions = [(0, 1), (1, 1), (1, 0), (1, -1)]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if all(state[i][j] == c for i, word in enumerate(target_words) for j, c in enumerate(word) if j != 1):
           return actions


       # Generate all possible actions from the current state
       for row, col in [(i, j) for i, row in enumerate(state) for j, cell in enumerate(row) if cell == '_']:
           for swap_direction in swap_directions:
               new_row, new_col = row + swap_direction[0], col + swap_direction[1]
               # Check if the new state is valid, ie the new position of the blank space is within the bounds of the board
               if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The heuristic function can be a simple count of the number of characters in the wrong position
                       h = heuristic(state, target_words)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(row, col, swap_direction)], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a simple count of the number of characters in the wrong position
   h = 0
   for i, word in enumerate(target_words):
       for j, c in enumerate(word):
           if state[i][j] != c:
               h += 1
   return h


print(a_star())
