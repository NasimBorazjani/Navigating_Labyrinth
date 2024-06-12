
import heapq


def a_star():
   # Define the initial state of the board
   initial_state = (['_', 's', 'a', 'n'], ['q', 'u', 'o', 'u'], ['c', 'h', 'u', 't'], ['l', 't', 'r', 'e'])
   # Define the target words
   target_words = ['sun', 'quot', 'chat', 'lure']
   # Define the possible directions for swapping the blank space
   directions = ['up-right', 'down-right', 'up-left', 'down-left']
   num_rows = 4
   num_cols = 4


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == tuple(word.split() for word in target_words):
           return actions


       # Generate all possible actions from the current state
       for row in range(num_rows):
           for col in range(num_cols):
               # Check if the new state would be valid, ie the blank space must be in a diagonal position
               if state[row][col] == '_' and (row != 0 or col != 0) and (row != num_rows - 1 or col != num_cols - 1):
                   for direction in directions:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       # Swap the blank space with the neighboring tile in the given direction
                       if direction == 'up-right':
                           new_state[row][col], new_state[row - 1][col + 1] = new_state[row - 1][col + 1], new_state[row][col]
                       elif direction == 'down-right':
                           new_state[row][col], new_state[row + 1][col + 1] = new_state[row + 1][col + 1], new_state[row][col]
                       elif direction == 'up-left':
                           new_state[row][col], new_state[row - 1][col - 1] = new_state[row - 1][col - 1], new_state[row][col]
                       elif direction == 'down-left':
                           new_state[row][col], new_state[row + 1][col - 1] = new_state[row + 1][col - 1], new_state[row][col]
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(state, target_words)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(row, col, direction)], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a count of the number of characters in the current state that are not in their correct positions in the goal state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a character is moved from its correct position, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of characters that can be moved to their correct positions in the heuristic is by moving the characters that are currently in their correct positions, which is exactly the characters used to fill the board in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != '_' and state[i][j] != target_words[i][j - (i > 0)]:
               h += 1
   return h


print(a_star())
