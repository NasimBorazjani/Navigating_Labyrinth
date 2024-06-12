
import heapq


def a_star():
   # Define the initial state of the board
   initial_state = (['g', 'j', 'u', 'm', 'a'],
                   ['a', 'r', 'o', 'e', 'o'],
                   ['h', 'u', '_', 'g', 'd'],
                   ['s', 'c', 'r', 'a', 'f'])
   # Define the target words
   target_words = ['jama', 'agoho', 'rudge', 'scruf']
   # Define the possible directions for the blank space to move
   directions = ['up-right', 'down-right', 'up-left', 'down-left']
   # Define the coordinates of the blank space in the initial state
   blank_coord = (2, 2)


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
           # Calculate the new coordinates of the blank space based on the direction
           new_coord = (blank_coord[0] + {'up-right': 1, 'down-right': -1, 'up-left': 1, 'down-left': -1}.get(direction, 0),
                        blank_coord[1] + {'up-right': 1, 'down-right': 1, 'up-left': -1, 'down-left': -1}.get(direction, 0))
           # Check if the new coordinates are valid
           if 0 <= new_coord[0] < len(state) and 0 <= new_coord[1] < len(state[0]):
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[blank_coord[0]][blank_coord[1]], new_state[new_coord[0]][new_coord[1]] = new_state[new_coord[0]][new_coord[1]], new_state[blank_coord[0]][blank_coord[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of actions taken, as the task is to minimize the number of actions required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(state, target_words)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [direction], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a count of the number of characters in the current state that are not in their correct positions in the target state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a character is moved from its correct position, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of characters that can be moved to their correct positions in the heuristic is by moving the characters that are currently in their correct positions, which is exactly the characters used to fill the board in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] != target_words[i][j - (i > 0)]:
               h += 1
   return h


print(a_star())
