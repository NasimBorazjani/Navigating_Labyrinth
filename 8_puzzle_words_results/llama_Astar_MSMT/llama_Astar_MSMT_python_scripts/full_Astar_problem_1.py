
import heapq


def initialize():
   # Define the initial state of the board, the target words, and the initial state of the blank space
   initial_state = (['i', 'c', 'a', 'm'], ['h', 'p', 'l', 'o'], ['_', 'r', 'a', 'y'], ['d', 'l', 'e', 'r'])
   target_words = ['cam', 'hill', 'pray', 'doer']
   blank_space = (0, 0)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, target_words, blank_space, visited_costs, queue
  
def a_star():
  
   initial_state, target_words, blank_space, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == target_words:
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
           new_row, new_col = blank_space[0] + d_row, blank_space[1] + d_col
           # Check if the new position is valid, ie if the new position is within the bounds of the board
           if 0 <= new_row < len(state) and 0 <= new_col < len(state[0]):
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[blank_space[0]][blank_space[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_space[0]][blank_space[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, target_words), new_cost, actions + [(blank_space, (new_row, new_col))], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a count of the number of characters in the current state that are not in their correct positions in the target words
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as each mismatched character must be moved at least once
   # The heuristic is consistent as the estimated cost of the next node is higher if a character is moved from its correct position, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum amount of characters that can be moved to their correct positions in the heuristic is by moving the characters in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] != '_' and state[i][j] != target_words[i][j - i]:
               h += 1
   return h


print(a_star())
