
import heapq


def a_star():
   # Define the initial state of the board and the target words
   initial_state = [['r', 's', 'c', 'v', 'a'],
                   ['b', 'b', 'y', 'r', 'e'],
                   ['u', 'i', '_', 'n', 'i'],
                   ['p', 'n', 'g', 'i', 'l'],
                   ['l', 'i', 'y', 'n', 'e']]
   target_words = ['siva', 'bryce', 'birny', 'pugil', 'linne']


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
           # Swap the blank space with its diagonal neighbor
           new_state[move[0] + 1][move[1] + 1], new_state[move[0]][move[1]] = new_state[move[0]][move[1]], new_state[move[0] + 1][move[1] + 1]
           # The new state must be valid, ie the blank space must be within the bounds of the board
           if 0 <= move[0] + 1 < len(state) and 0 <= move[1] + 1 < len(state[0]):
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of actions taken, as the task is to minimize the number of actions required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(state, target_words)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [move], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a count of the number of characters in the current state that are not in their correct positions in the target words
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a character is moved from its correct position in the target word, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum number of characters that can be moved to their correct positions in the heuristic is by moving the characters that are currently in their correct positions in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[0])):
           if state[i][j] != '_' and state[i][j] != target_words[i][j - i]:
               h += 1
   return h


print(a_star())
