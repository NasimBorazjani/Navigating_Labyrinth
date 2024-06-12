
import heapq


def a_star():
   # Define the initial state of the board
   initial_state = (['a', 's', 't', 'x'], ['t', 'r', 's', 'a'], ['s', 'u', '_', 'p'], ['c', 'a', 'd', 'e'])
   # Define the target words
   target_words = ['sax', 'tass', 'turp', 'cade']
   # Define the possible swap directions
   swap_directions = ['up-right', 'down-right', 'up-left', 'down-left']
   # Define the initial cost and the heuristic cost
   initial_cost = 0
   heuristic_cost = 0


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == tuple(word[::-1] for word in target_words):
           return actions


       # Generate all possible actions from the current state
       for swap_direction in swap_directions:
           # Generate the new state by swapping the blank space in the current state
           new_state = [list(row[:]) for row in state]
           # Locate the blank space in the current state
           for i in range(len(state)):
               for j in range(len(state[i])):
                   if state[i][j] == '_':
                       # Swap the blank space with its diagonal neighbor in the new state
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
               h = heuristic(state, target_words)
               heapq.heappush(queue, (new_cost + h, new_cost, actions + [swap_direction], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a count of the number of characters in the current state that are not in their correct positions in the goal state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a character is moved from its correct position, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of characters that can be moved to their correct positions in the heuristic is by moving the characters that are currently in their correct positions in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != target_words[i][j]:
               h += 1
   return h


print(a_star())
