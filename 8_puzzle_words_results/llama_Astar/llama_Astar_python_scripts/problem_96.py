
import heapq


def a_star():
   # Define the initial state of the board and the target words
   initial_state = [['o', 's', 'n', 'e', 'd', 'a'],
                   ['l', 'k', 'c', 'c', 'e', 'h'],
                   ['t', 'o', '_', 'c', 'n', 'e'],
                   ['c', 'i', 'l', 'a', 'i', 'c'],
                   ['b', 'l', 'e', 'n', 'c', 'o']]
   target_words = ['siena', 'locked', 'conche', 'celtic', 'blanco']


   # Define the possible moves
   moves = [(-1, 1), (1, 1), (-1, -1), (1, -1)]


   visited_costs = {}
   visited_costs[tuple(map(tuple, initial_state))] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state
       if state == [list(word) for word in target_words]:
           return actions


       # Generate all possible actions from the current state
       for move in moves:
           new_state = [list(row) for row in state]
           blank_row, blank_col = next(i for i, row in enumerate(new_state) if '_' in row)
           new_blank_row, new_blank_col = blank_row + move[0], blank_col + move[1]
           # Check if the new state is valid
           if 0 <= new_blank_row < len(new_state) and 0 <= new_blank_col < len(new_state[0]):
               # Swap the blank space with the neighboring tile
               new_state[blank_row][blank_col], new_state[new_blank_row][new_blank_col] = new_state[new_blank_row][new_blank_col], new_state[blank_row][blank_col]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of actions taken
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic is the number of characters in the current state that are not in their correct position in the goal state
                   h = heuristic(state, target_words)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [move], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic is the number of characters in the current state that are not in their correct position in the goal state
   h = 0
   for i, word in enumerate(target_words):
       for j, char in enumerate(word):
           if state[i][j] != char:
               h += 1
   return h


print(a_star())
