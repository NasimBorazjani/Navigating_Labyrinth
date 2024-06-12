
import heapq


def a_star():
   # Define the initial state of the board and the target words
   initial_state = [['g', 'f', 't', 'i', 'm'],
                   ['a', 'l', 'a', 'a', 'e'],
                   ['n', 's', '_', 'i', 'e'],
                   ['f', 'p', 'o', 'k', 'y'],
                   ['z', 'o', 'r', 'a', 'r']]
   target_words = ['frim', 'agate', 'askip', 'floey', 'zonar']


   # Define the dimensions of the board
   num_rows = 5
   num_cols = 5


   # Define the possible moves from a position
   moves = [(-1, 1), (1, 1), (-1, -1), (1, -1)]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == target_words:
           return actions


       # Generate all possible actions from the current state
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] == '_':
                   for move in moves:
                       new_row, new_col = row + move[0], col + move[1]
                       # Check if the new position is valid
                       if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
                           new_state = [tuple(row) for row in new_state]
                           # The cost so far is the number of actions taken
                           new_cost = g + 1


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               h = heuristic(new_state, target_words)
                               # The action is a tuple of the current position and the new position
                               heapq.heappush(queue, (new_cost + h, new_cost, actions + [(row, col, new_row, new_col)], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be the sum of the distances of the current words from their target words in the list
   # This heuristic is admissible because it is a lower bound on the cost to reach the goal
   # The heuristic is consistent because the estimated cost of the next node is higher if the current word is further from its target word, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum distance that can be reduced by swapping a character with the blank space is 1
   h = 0
   for i in range(len(state)):
       h += sum(abs(ord(state[i][j]) - ord(target_words[i][j])) for j in range(len(state[i])))
   return h


print(a_star())
