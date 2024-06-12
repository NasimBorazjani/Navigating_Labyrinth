
import heapq


def a_star():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('c', 'o', 'a', 'c'),
                   ('i', 'o', 'h', 'r'),
                   ('d', 'e', 'r', 'r'),
                   ('f', 'o', 'u', 'a'),
                   ('p', 'e', '_', 'i'))
   # Define the target words
   target_words = ['orc', 'icho', 'dear', 'four', 'peai']
   # Define the possible swap directions
   swap_directions = ['up-right', 'down-right', 'up-left', 'down-left']
   # Define the initial state of the board as a 2d tuple
   initial_state = (('c', 'o', 'a', 'c'),
                   ('i', 'o', 'h', 'r'),
                   ('d', 'e', 'r', 'r'),
                   ('f', 'o', 'u', 'a'),
                   ('p', 'e', '_', 'i'))


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == tuple(list(word) for word in target_words):
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for i in range(len(state)):
           for j in range(len(state[i])):
               if state[i][j] == '_':
                   for swap_direction in swap_directions:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       # Swap the blank space with its diagonal neighbor
                       if swap_direction == 'up-right':
                           new_state[i][j], new_state[i - 1][j + 1] = new_state[i - 1][j + 1], new_state[i][j]
                       elif swap_direction == 'down-right':
                           new_state[i][j], new_state[i + 1][j + 1] = new_state[i + 1][j + 1], new_state[i][j]
                       elif swap_direction == 'up-left':
                           new_state[i][j], new_state[i - 1][j - 1] = new_state[i - 1][j - 1], new_state[i][j]
                       elif swap_direction == 'down-left':
                           new_state[i][j], new_state[i + 1][j - 1] = new_state[i + 1][j - 1], new_state[i][j]
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic function can be a simple count of the number of characters in the current state that are not in their correct position in the goal state
                           h = heuristic(state, target_words)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(i, j, swap_direction)], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a simple count of the number of characters in the current state that are not in their correct position in the goal state
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != target_words[i][j - (i > 0)]:
               h += 1
   return h


print(a_star())
