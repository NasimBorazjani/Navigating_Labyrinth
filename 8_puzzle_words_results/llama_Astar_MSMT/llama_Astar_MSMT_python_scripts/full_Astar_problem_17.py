
import heapq


def initialize():
   # Define the initial state of the board, with '_' representing the blank space
   initial_state = [['e', 'h', 'r', 'y'], ['w', 'f', 'r', 'r'], ['_', 'u', 'd', 'd'], ['f', 'a', 'i', 'b']]
   # Define the target words
   target_words = ['hay', 'werf', 'rudd', 'frib']
   # Define the dimensions of the board
   num_rows = 4
   num_cols = 4
   # Define the possible directions for swapping the blank space
   directions = [(0, 1), (1, 1), (1, 0), (1, -1)]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, target_words, num_rows, num_cols, directions, visited_costs, queue
  
def a_star():
  
   initial_state, target_words, num_rows, num_cols, directions, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == [list(word) for word in target_words]:
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for direction in directions:
           new_row, new_col = state.index('_') + direction[0], state.index('_') + direction[1]
           # Check if the new position is valid, ie within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[state.index('_')][state.index('_')], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[state.index('_')][state.index('_')]
               new_state = [tuple(row) for row in new_state]
               # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to sort the board
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic function is not needed in this problem as the goal state is always reachable and the cost to reach the goal is always the same, making the problem uninformed
                   heapq.heappush(queue, (new_cost, new_cost, actions + [direction], new_state))
   return None


print(a_star())
