
import heapq


def a_star():
   # Define the initial state of the board
   initial_state = (['a', 'n', '_', 'l', 'l', 'e'],
                   ['y', 'p', 'p', 'o', 'a', 'n'],
                   ['r', 'i', 'm', 'a', 'y', 'a'],
                   ['c', 't', 'a', 'w', 'l', 'y'])
   # Define the target words
   target_words = ['nolle', 'yapman', 'pitaya', 'crawly']
   # Define the possible swap directions
   swap_directions = ['up-right', 'down-right', 'up-left', 'down-left']
   # Define the dimensions of the board
   num_rows = 4
   num_cols = 6


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == tuple(word[::-1] for word in target_words):
           return actions


       # Generate all possible actions from the current state
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] == '_':
                   for swap_direction in swap_directions:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       # Swap the blank space with its diagonal neighbor
                       if swap_direction == 'up-right':
                           new_state[row][col], new_state[row - 1][col + 1] = new_state[row - 1][col + 1], new_state[row][col]
                       elif swap_direction == 'down-right':
                           new_state[row][col], new_state[row + 1][col + 1] = new_state[row + 1][col + 1], new_state[row][col]
                       elif swap_direction == 'up-left':
                           new_state[row][col], new_state[row - 1][col - 1] = new_state[row - 1][col - 1], new_state[row][col]
                       elif swap_direction == 'down-left':
                           new_state[row][col], new_state[row + 1][col - 1] = new_state[row + 1][col - 1], new_state[row][col]
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the number of swaps made
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is the sum of the distances of the characters in the current state to their target positions in the goal state
                           h = heuristic(state, target_words)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(row, col, swap_direction)], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic is the sum of the distances of the characters in the current state to their target positions in the goal state
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != '_':
               h += abs(i - target_words.index(state[i][j])) + abs(j - len(target_words[i]))
   return h


print(a_star())
