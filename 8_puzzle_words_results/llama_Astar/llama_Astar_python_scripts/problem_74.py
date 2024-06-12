
import heapq


def a_star():
   # Define the initial state of the board
   initial_state = (['u', 'z', 's', 't', 'a'],
                   ['s', 'e', 'm', 'o', 'c'],
                   ['a', 'h', '_', 'w', 'y'],
                   ['s', 'a', 'e', 'm', 'k'],
                   ['a', 'j', 'e', 'v', 'a'])
   target_words = ['zeta', 'sumac', 'showy', 'smeek', 'ajava']
   num_rows = 5
   num_cols = 5
   # Define the possible directions for the blank space to swap
   directions = [(-1, 1), (1, 1), (-1, -1), (1, -1)]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == tuple(word[::-1] for word in target_words):
           return actions


       # Generate all possible actions from the current state
       for direction in directions:
           new_row, new_col = state[3].index('_') + direction[0], state[3].index('_') + direction[1]
           # Check if the new position is valid
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[3][state[3].index('_')], new_state[3][new_col] = new_state[3][new_col], new_state[3][state[3].index('_')]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of actions taken
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic is the sum of the distances of the blank space to the goal positions of each word
                   h = heuristic(state, target_words)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [(direction)], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function calculates the sum of the distances of the blank space to the goal positions of each word
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if the blank space is moved further from the goal positions, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum distance that the blank space can be moved is by 1 tile in one action
   h = 0
   for i, word in enumerate(target_words):
       for j, char in enumerate(word):
           if char == '_':
               h += abs(state[i].index('_') - j)
   return h


print(a_star())
