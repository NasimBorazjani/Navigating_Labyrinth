
import heapq


def a_star():
   # Define the initial state of the board and the target words
   initial_state = [['s', 'n', '_', 'e', 'y', 'e'],
                   ['a', 'e', 't', 'i', 'l', 'e'],
                   ['o', 'e', 'c', 'i', 'v', 't'],
                   ['m', 'l', 'w', 's', 'e', 'r']]
   target_words = ['nieve', 'astely', 'oecist', 'mewler']


   # Define the dimensions of the board
   num_rows = 4
   num_cols = 6


   # Define the possible directions for swapping the blank space
   directions = [(-1, 1), (1, 1), (-1, -1), (1, -1)]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == [list(word) for word in target_words]:
           return actions


       # Generate all possible actions from the current state
       for direction in directions:
           new_row, new_col = state.index('_') + direction[0], state[0].index('_') + direction[1]
           # Check if the new position of the blank space is valid
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[state.index('_')][state[0].index('_')], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[state.index('_')][state[0].index('_')]
               new_state = [tuple(row) for row in new_state]
               # The cost so far is the number of actions taken, as the task is to minimize the number of actions required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(state, target_words)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [direction], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a count of the number of characters in the current state that are not in their correct positions in the target words
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a character is moved from its correct position in the target word, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of characters that can be moved to their correct positions in the heuristic is by moving the characters that are currently in their correct positions in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != '_' and state[i][j] != target_words[i][j - (i > 0)]:
               h += 1
   return h


print(a_star())
