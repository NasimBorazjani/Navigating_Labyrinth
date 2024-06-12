
import heapq


def initialize():
   # Define the initial state of the board, with '_' representing the blank space
   initial_state = (['v', 't', 'u', 'i'],
                   ['o', 'w', 'e', 'i'],
                   ['y', 'd', '_', 'c'],
                   ['d', 'i', 'e', 'm'])
   num_rows = 4
   num_cols = 4
   target_words = ['twi', 'ovey', 'udic', 'diem']


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, target_words, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, target_words, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == tuple(word[::-1] for word in target_words):
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
           new_row, new_col = state[3].index('_') + d_row, state[3].index('_') + d_col
           # Check if the new coordinate is valid, ie if the new blank space is within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[3][state[3].index('_')], new_state[3][new_col] = new_state[3][new_col], new_state[3][state[3].index('_')]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required to sort the board
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic is the sum of the distances of the characters from their target positions in the goal state
                   h = heuristic(state, target_words)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [(d_row, d_col)], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function calculates the sum of the distances of the characters from their target positions in the goal state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent because the estimated cost of the next node is higher if a character is moved away from its target position, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum distance that a character can be moved is by swapping it with a character that is at most 1 step away from its target position in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != '_':
               h += abs(i - target_words.index(state[i][j])) + abs(j - len(state[i]) + 1)
   return h


print(a_star())
