
import heapq


def a_star():
   # Define the initial state of the board and the target words
   initial_state = [['i', 'e', 'k', 'k', 'a'],
                   ['b', 'e', 'f', 'a', 'r'],
                   ['g', 'a', '_', 'm', 'e'],
                   ['d', 'i', 'n', 'k', 'a'],
                   ['b', 'r', 'm', 't', 't']]
   target_words = ['ekka', 'bifer', 'magma', 'dinka', 'brett']


   # Define the dimensions of the board
   num_rows = 5
   num_cols = 5


   # Define the possible moves from the blank space
   moves = [(-1, 1), (1, 1), (-1, -1), (1, -1)]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == target_words:
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for move in moves:
           new_row, new_col = state.index('_') + move[0], state.index('_') + move[1]
           # Check if the new state would be valid, ie the new position of the blank space must be within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[state.index('_')], new_state[new_row][new_col] = new_state[new_row][new_col], '_'
               new_state = [''.join(row) for row in new_state]
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, target_words)
                   # In the problem statement the directions are indexed starting from 1, thus must add 1 to the move index
                   move_index = moves.index(move) + 1
                   heappush(queue, (new_cost + h, new_cost, actions + [move_index], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a count of the number of characters in the current state that are not in their correct positions in the target state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a character is moved from its correct position, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of characters that can be moved to their correct positions in the heuristic is by moving the characters that are currently in their correct positions, which is exactly the characters used to fill the board in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != target_words[i][j]:
               h += 1
   return h


print(a_star())
