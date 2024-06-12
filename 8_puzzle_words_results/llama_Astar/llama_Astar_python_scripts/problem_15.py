
import heapq


def a_star():
   # Define the initial state of the board
   initial_state = (['a', 'r', '_', 'c'],
                   ['h', 'a', 'v', 'e'],
                   ['a', 'g', 's', 'd'],
                   ['b', 'i', 't', 'z'])
   # Define the target words
   target_words = ['ric', 'have', 'sgad', 'batz']
   # Define the possible directions for swapping
   directions = ['ur', 'dr', 'ul', 'dl']
   # Define the coordinates of the blank space
   blank_coord = (3, 1)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == tuple(word[::-1] for word in target_words):
           return actions


       # Generate all possible actions from the current state
       for direction in directions:
           # Calculate the new coordinates of the blank space after the swap
           new_blank_coord = blank_coord[:]
           if direction == 'ur':
               new_blank_coord[0] -= 1
               new_blank_coord[1] += 1
           elif direction == 'dr':
               new_blank_coord[0] += 1
               new_blank_coord[1] += 1
           elif direction == 'ul':
               new_blank_coord[0] -= 1
               new_blank_coord[1] -= 1
           elif direction == 'dl':
               new_blank_coord[0] += 1
               new_blank_coord[1] -= 1


           # Check if the new coordinates are valid
           if 0 <= new_blank_coord[0] < len(state) and 0 <= new_blank_coord[1] < len(state[0]):
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[blank_coord[0]][blank_coord[1]], new_state[new_blank_coord[0]][new_blank_coord[1]] = new_state[new_blank_coord[0]][new_blank_coord[1]], new_state[blank_coord[0]][blank_coord[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of actions taken, as the task is to minimize the number of actions required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic function can be a simple count of the number of characters that are not in their correct positions
                   h = heuristic(state, target_words)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [direction], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a simple count of the number of characters that are not in their correct positions
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] != '_' and state[i][j] != target_words[i][j - (i > 0)]:
               h += 1
   return h


print(a_star())
