
import heapq


def a_star():
   # Define the initial state of the board
   initial_state = (['u', 'a', '_', 'r'],
                   ['h', 'e', 'm', 'e'],
                   ['m', 'i', 'i', 'p'],
                   ['v', 'a', 'v', 'j'],
                   ['f', 'i', 'm', 'i'])
   target_words = ['aer', 'hume', 'mimp', 'viva', 'fiji']
   num_rows = 5
   num_cols = 4


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if all(state[i][1:] == list(target_words[i]) for i in range(num_rows)):
           return actions


       # Generate all possible actions from the current state
       for row in range(num_rows):
           for col in range(num_cols):
               # Check if the new state would be valid, ie the blank space must not move off the board
               for dr, dc in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
                   new_row, new_col = row + dr, col + dc
                   if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the number of actions taken, as the task is to minimize the number of actions required
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic function is not needed in this problem as the goal state is always reachable and the cost to reach the goal is always the same, ie the number of swaps made
                           heapq.heappush(queue, (new_cost, new_cost, actions + [(row, col, new_row, new_col)], new_state))
   return None


print(a_star())
