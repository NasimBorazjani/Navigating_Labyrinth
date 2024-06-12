
import heapq


def a_star():
   # Define the initial state of the board and the target words
   initial_state = [['_', 's', 's', 'h', 'o'],
                   ['r', 'i', 'l', 'o', 'y'],
                   ['j', 'o', 'l', 'i', 'p'],
                   ['d', 'r', 'a', 'i', 'n'],
                   ['n', 'i', 'v', 'a', 'l']]
   target_words = ['soho', 'rilly', 'josip', 'drain', 'nival']


   # Define the possible moves
   moves = [(-1, 1), (1, 1), (-1, -1), (1, -1)]


   visited_costs = {}
   visited_costs[tuple(map(tuple, initial_state))] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == [list(word) for word in target_words]:
           return actions


       # Generate all possible actions from the current state
       for move in moves:
           new_state = [list(row) for row in state]
           # Swap the blank space with its diagonal neighbor
           new_state[move[0]][move[1]] = state[0][0]
           new_state[0][0] = state[move[0]][move[1]]
           # The new state must be valid, ie the swapped word must be in the list of target words
           if new_state[move[0]][1:] in target_words:
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of actions taken, as the task is to minimize the number of actions required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, target_words)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [move], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a count of the number of words in the current state that are not in the correct order
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a word is not in the correct order, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of swaps that can be made to a word is by swapping it with its diagonal neighbor, which is exactly the word used to fill the blank space in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       if state[i][1:] != list(target_words[i]):
           h += 1
   return h


print(a_star())
