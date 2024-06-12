
import heapq


def a_star():
   # Define the initial state of the board
   initial_state = (['o', 'a', 'u', 'o'],
                   ['p', 'r', 'l', 'e'],
                   ['f', 'a', '_', 'f'],
                   ['m', 'k', 'd', 'd'])
   # Define the target words
   target_words = ['ako', 'pole', 'raff', 'mudd']
   # Define the possible swap directions
   swap_directions = ['up-right', 'down-right', 'up-left', 'down-left']
   # Define the coordinates of the blank space
   blank_coord = (2, 1)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == tuple(word[::-1] for word in target_words):
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for direction in swap_directions:
           new_blank_coord = None
           if direction == 'up-right':
               new_blank_coord = (blank_coord[0] - 1, blank_coord[1] + 1)
           elif direction == 'down-right':
               new_blank_coord = (blank_coord[0] + 1, blank_coord[1] + 1)
           elif direction == 'up-left':
               new_blank_coord = (blank_coord[0] - 1, blank_coord[1] - 1)
           elif direction == 'down-left':
               new_blank_coord = (blank_coord[0] + 1, blank_coord[1] - 1)


           # Check if the new blank space coordinate is valid
           if 0 <= new_blank_coord[0] < len(state) and 0 <= new_blank_coord[1] < len(state[0]):
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[blank_coord[0]][blank_coord[1]], new_state[new_blank_coord[0]][new_blank_coord[1]] = new_state[new_blank_coord[0]][new_blank_coord[1]], new_state[blank_coord[0]][blank_coord[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to sort the board
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(state, target_words)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [direction], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a count of the number of characters in the current state that are not in their correct positions in the goal state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a character is moved from its correct position, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of swaps that can be made is by moving a character from its correct position to its current position in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] != target_words[i][j - (i > 0)]:
               h += 1
   return h


print(a_star())
