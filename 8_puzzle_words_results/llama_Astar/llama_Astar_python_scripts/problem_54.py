
import heapq


def a_star():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('r', 'u', 'p', 'f', 'y', 'w'),
                   ('b', 'l', 'o', 'e', 'l', 'o'),
                   ('n', 'r', '_', 'g', 'h', 't'),
                   ('u', 'b', 'r', 'i', 'o', 't'))
   num_rows = 4
   num_cols = 6
   target_words = ['unfew', 'brolly', 'bright', 'uproot']


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == tuple(word[::-1] for word in target_words):
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for row_shift in [-1, 0, 1]:
           for col_shift in [-1, 1]:
               new_state = [list(row[:]) for row in state]
               blank_row, blank_col = next(i for i, cell in enumerate(new_state[0]) if cell == '_')
               new_state[0][blank_row], new_state[0][blank_col] = new_state[0][blank_col], new_state[0][blank_row]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic function is the sum of the distances of the characters in the current state to their positions in the goal state
                   h = heuristic(state, target_words)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [(row_shift, col_shift)], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function is the sum of the distances of the characters in the current state to their positions in the goal state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a character is moved further from its goal position, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum distance that a character can be moved is by swapping it with a character that is at most 1 step away from its goal position. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != '_':
               goal_row, goal_col = next(k for k, cell in enumerate(target_words[i][::-1]) if cell == state[i][j])
               h += abs(i - goal_row) + abs(j - goal_col)
   return h


print(a_star())
