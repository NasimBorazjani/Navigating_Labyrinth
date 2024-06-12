
import heapq


def a_star():
   # Define the initial state of the board and the target words
   initial_state = [['l', 'c', '_', 'o'], ['s', 'c', 'o', 'h'], ['d', 'y', 'a', 'e'], ['h', 's', 'l', 't']]
   target_words = ['cho', 'slod', 'syce', 'halt']


   # Define the possible directions for swapping the blank space
   directions = [(0, 1), (1, 1), (1, 0), (1, -1)]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == target_words:
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for direction in directions:
           new_state = [list(row[:]) for row in state]
           # Get the coordinates of the blank space
           blank_row, blank_col = next(i for i, row in enumerate(new_state) if '_' in row)
           blank_col = new_state[blank_row].index('_')
           # Get the coordinates of the new blank space
           new_blank_row, new_blank_col = blank_row + direction[0], blank_col + direction[1]
           # Check if the new state is valid, ie the new blank space must be within the bounds of the board
           if 0 <= new_blank_row < len(new_state) and 0 <= new_blank_col < len(new_state[0]):
               # Swap the blank spaces
               new_state[blank_row][blank_col], new_state[new_blank_row][new_blank_col] = new_state[new_blank_row][new_blank_col], new_state[blank_row][blank_col]
               new_state = [''.join(row) for row in new_state]
               # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic function is the sum of the distances between the current state and the goal state
                   h = heuristic(state, target_words)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [direction], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function is the sum of the distances between the current state and the goal state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if the blank space is moved further from the goal, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum distance that the blank space can be moved is by using the largest step in a direction, which is exactly the step used to move the blank space in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] == '_':
               for target_word in target_words:
                   for k in range(len(target_word)):
                       if i + j - k >= 0 and i + j - k < len(target_word) and state[i][j] != target_word[i + j - k]:
                           h += 1
   return h


print(a_star())
