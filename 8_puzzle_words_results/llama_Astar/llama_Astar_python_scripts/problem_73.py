
import heapq


def a_star():
   # Define the initial state of the board and the target words
   initial_state = [['o', 't', 'f', 'a', 'g'],
                   ['h', 'r', 'p', 'r', 'd'],
                   ['s', 'h', '_', 'l', 't'],
                   ['n', 'e', 'a', 'e', 'h'],
                   ['f', 'a', 'e', 's', 'e']]
   target_words = ['trag', 'hoped', 'shelf', 'neath', 'farse']


   # Define the possible directions for swapping the blank space
   directions = [(0, 1), (1, 1), (1, 0), (1, -1)]


   visited_costs = {}
   visited_costs[tuple(row[:] for row in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == [list(word) for word in target_words]:
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for direction in directions:
           new_row, new_col = initial_state.index('_') + direction[0], initial_state[0].index('_') + direction[1]
           # Check if the new state would be valid, ie the new position of the blank space must be within the bounds of the board
           if 0 <= new_row < len(state) and 0 <= new_col < len(state[0]):
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[new_row][new_col], new_state[initial_state.index('_')][initial_state[0].index('_')] = new_state[initial_state.index('_')][initial_state[0].index('_')], new_state[new_row][new_col]
               new_state = [tuple(row) for row in new_state]
               # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
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
