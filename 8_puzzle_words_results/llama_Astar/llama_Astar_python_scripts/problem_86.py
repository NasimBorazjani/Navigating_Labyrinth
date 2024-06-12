
import heapq


def a_star():
   # Define the initial state of the board and the target words
   initial_state = [['y', 'c', 'a', 'r', 'd'],
                   ['s', 'u', 'l', 'c', 'a'],
                   ['v', 'h', '_', 'n', 'o'],
                   ['s', 'e', 'l', 's', 'm'],
                   ['b', 'i', 'u', 'h', 'y']]
   target_words = ['card', 'sylva', 'shune', 'solum', 'bichy']


   # Define the possible moves
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
       for move in moves:
           new_state = [list(row[:]) for row in state]
           blank_row, blank_col = next((i, j) for i, row in enumerate(new_state) for j, cell in enumerate(row) if cell == '_')
           new_blank_row, new_blank_col = blank_row + move[0], blank_col + move[1]
           # Check if the new state is valid, ie the blank space must not move out of the board
           if 0 <= new_blank_row < len(new_state) and 0 <= new_blank_col < len(new_state[0]):
               new_state[blank_row][blank_col], new_state[new_blank_row][new_blank_col] = new_state[new_blank_row][new_blank_col], new_state[blank_row][blank_col]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of actions taken, as the task is to minimize the number of actions required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, target_words)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [move], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a count of the number of characters in the current state that are not in their correct positions in the target state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a character is moved from its correct position, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of characters that can be moved to their correct positions in the heuristic is by moving the characters that are currently in their correct positions, which is exactly the characters used to fill the board in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] != target_words[i][j - (i > 0)]:
               h += 1
   return h


print(a_star())
