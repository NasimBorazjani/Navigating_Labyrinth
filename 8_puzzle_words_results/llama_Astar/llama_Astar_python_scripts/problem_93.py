
import heapq


def a_star():
   # Define the initial state of the board and the target words
   initial_state = [['d', 'h', '_', 'l', 'e', 'n'],
                   ['a', 'a', 'e', 'b', 'e', 'u'],
                   ['m', 'u', 'i', 'b', 'e', 'e'],
                   ['i', 'o', 'd', 'm', 's', 'l'],
                   ['t', 'r', 'l', 'l', 'l', 'o']]
   target_words = ['helen', 'adelea', 'bumble', 'iodism', 'trullo']


   # Define the possible moves
   moves = [(-1, 1), (1, 1), (-1, -1), (1, -1)]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == [list(word) for word in target_words]:
           return actions


       # Generate all possible actions from the current state
       for move in moves:
           new_state = [list(row) for row in state]
           new_state[0][2], new_state[move[1]][move[0]] = new_state[move[1]][move[0]], new_state[0][2]
           new_state = tuple(tuple(row) for row in new_state)
           new_cost = g + 1


           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
               visited_costs[new_state] = new_cost
               h = heuristic(new_state, target_words)
               heapq.heappush(queue, (new_cost + h, new_cost, actions + [move], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a count of the number of characters in the current state that are not in their correct positions in the target state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a character is moved away from its correct position, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of characters that can be moved to their correct positions in the heuristic is by moving the characters that are currently in their correct positions, which is exactly the characters used to fill the board in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != target_words[i][j - 1]:
               h += 1
   return h


print(a_star())
