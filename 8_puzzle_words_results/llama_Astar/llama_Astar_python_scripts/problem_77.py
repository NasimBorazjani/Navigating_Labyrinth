
import heapq


def a_star():
   # Define the initial state of the board and the target words
   initial_state = [['l', 'g', 'a', 'n', 'g'],
                   ['c', 'o', 'o', 'e', 'n'],
                   ['e', 'r', '_', 'n', 't'],
                   ['d', 'b', 'w', 'o', 'x'],
                   ['t', 'h', 'w', 'r', 'p']]
   target_words = ['gong', 'clown', 'brent', 'dewax', 'thorp']


   # Define the possible directions for swapping the blank space
   directions = [(-1, 1), (1, 1), (-1, -1), (1, -1)]


   visited_costs = {}
   visited_costs[tuple(tuple(row) for row in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == [list(word) for word in target_words]:
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for direction in directions:
           new_state = [list(row[:]) for row in state]
           blank_row, blank_col = next((i, j) for i, row in enumerate(state) for j, cell in enumerate(row) if cell == '_')
           new_blank_row, new_blank_col = blank_row + direction[0], blank_col + direction[1]
           # Check if the new state would be valid, ie the new blank space must be within the bounds of the board
           if 0 <= new_blank_row < len(state) and 0 <= new_blank_col < len(state[0]):
               # Swap the blank spaces in the new state
               new_state[blank_row][blank_col], new_state[new_blank_row][new_blank_col] = new_state[new_blank_row][new_blank_col], new_state[blank_row][blank_col]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(state, target_words)
                   # In the problem statement the directions are indexed starting from 1, thus must add 1 to the direction index
                   heappush(queue, (new_cost + h, new_cost, actions + [(direction[0], direction[1])], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a simulation of swapping the blank space greedily, using the next direction that results in a valid state
   # This heuristic is admissible because it is greedy, always opting for the action that results in a valid state, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if the blank space is swapped to an invalid position, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of swaps that can be made is by using the direction that results in a valid state. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for direction in directions:
       new_state = [list(row[:]) for row in state]
       blank_row, blank_col = next((i, j) for i, row in enumerate(state) for j, cell in enumerate(row) if cell == '_')
       new_blank_row, new_blank_col = blank_row + direction[0], blank_col + direction[1]
       if 0 <= new_blank_row < len(state) and 0 <= new_blank_col < len(state[0]):
           new_state[blank_row][blank_col], new_state[new_blank_row][new_blank_col] = new_state[new_blank_row][new_blank_col], new_state[blank_row][blank_col]
           if new_state not in target_words:
               h += 1
   return h


print(a_star())
