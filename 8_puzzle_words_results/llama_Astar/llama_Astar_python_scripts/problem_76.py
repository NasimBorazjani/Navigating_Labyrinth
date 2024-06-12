
import heapq


def a_star():
   # Define the initial state of the board and the target words
   initial_state = [['h', 'q', 'n', 'a', '_'],
                   ['b', 'y', 'a', 'd', 'g'],
                   ['d', 'e', 'c', 'a', 'o'],
                   ['h', 'o', 'n', 'u', 'r'],
                   ['p', 'i', 'c', 'k', 'y']]
   target_words = ['quad', 'bhang', 'decay', 'honor', 'picky']


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
           new_state = [list(row) for row in state]
           new_state[move[0]][move[1]] = state[0][0]
           new_state[0][0] = '_'
           # The cost so far is the number of actions taken
           new_cost = g + 1


           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
               visited_costs[new_state] = new_cost
               # The heuristic is the number of characters in the current state that are not in their correct position in the goal state
               h = heuristic(new_state, target_words)
               heapq.heappush(queue, (new_cost + h, new_cost, actions + [move], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic is the number of characters in the current state that are not in their correct position in the goal state
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != '_' and state[i][j] != target_words[i][j]:
               h += 1
   return h


print(a_star())
