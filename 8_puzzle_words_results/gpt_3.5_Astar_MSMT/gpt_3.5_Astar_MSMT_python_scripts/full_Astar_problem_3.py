
import heapq

def initialize():
   # Define the initial state of the board and the target words
   initial_state = [['v', 't', 'u', 'i'], ['o', 'w', 'e', 'i'], ['y', 'd', '_', 'c'], ['d', 'i', 'e', 'm']]
   target_words = ['twi', 'ovey', 'udic', 'diem']
   num_rows = len(initial_state)
   num_cols = len(initial_state[0])

   visited_costs = {}
   visited_costs[str(initial_state)] = 0

   queue = []
   # No actions taken in the initial state
   heapq.heappush(queue, (0, 0, [], initial_state))
  
   return initial_state, target_words, num_rows, num_cols, visited_costs, queue
  
def a_star():
  
   initial_state, target_words, num_rows, num_cols, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heapq.heappop(queue)

       # If the current state is the goal state, return the actions taken
       if check_goal_state(state, target_words):
           return actions

       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == '_':
                   for d_row, d_col in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
                       new_row, new_col = i + d_row, j + d_col
                       if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                           # Generate the new state by swapping the blank space with the neighboring tile
                           new_state = [list(row) for row in state]
                           new_state[i][j], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[i][j]
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost of the new state is the number of swaps made, as the task is to minimize the number of swaps required
                           new_cost = g + 1

                           if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                               visited_costs[str(new_state)] = new_cost
                               heapq.heappush(queue, (g + heuristic(new_state, target_words), g + 1, actions + [(i, j, new_row, new_col)], new_state))
   return None

def heuristic(state, target_words):
   # A heuristic for this problem could be the number of characters that are not in the correct position in the current state compared to the target words
   # This heuristic relaxes the constraint that only the blank space can be moved, as it considers all characters in the board
   # It is admissible because it never overestimates the cost to reach the goal state, as each character that is out of place must be moved at least once
   # It is consistent because moving a character closer to its correct position reduces the heuristic cost of the successor node by 1 (the cost of moving that character), which is equal to the cost of reaching the successor node
   # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] != '_' and state[i][j] != target_words[i][j]:
               h += 1
   return h

def check_goal_state(state, target_words):
   # Check if the current state of the board matches the target words
   for i in range(len(state)):
       if ''.join(state[i]) != target_words[i]:
           return False
   return True

print(a_star())
