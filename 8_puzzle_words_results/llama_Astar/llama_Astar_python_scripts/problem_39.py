
import heapq


def a_star():
   # Define the initial state of the board and the target words
   initial_state = (['n', 'j', '_', 'b', 'e', 'y'],
                   ['e', 'i', 't', 'u', 'n', 'o'],
                   ['x', 'e', 'n', 'i', 'b', 'm'],
                   ['e', 'n', 'w', 'o', 'm', 'b'])
   target_words = ['jibby', 'entone', 'xenium', 'enwomb']


   # Define the possible directions for swapping the blank space
   directions = ['ur', 'dr', 'ul', 'dl']


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == tuple(list(word) for word in target_words):
           return actions


       # Generate all possible actions from the current state
       for direction in directions:
           # Generate the new state by swapping the blank space in the current state with a neighboring tile in the given direction
           new_state = [list(row[:]) for row in state]
           if direction == 'ur':
               new_state[0][2], new_state[1][1] = new_state[1][1], new_state[0][2]
           elif direction == 'dr':
               new_state[1][1], new_state[2][2] = new_state[2][2], new_state[1][1]
           elif direction == 'ul':
               new_state[0][2], new_state[1][3] = new_state[1][3], new_state[0][2]
           elif direction == 'dl':
               new_state[1][3], new_state[2][2] = new_state[2][2], new_state[1][3]
           new_state = tuple(tuple(row) for row in new_state)
           # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to sort the board
           new_cost = g + 1


           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
               visited_costs[new_state] = new_cost
               h = heuristic(state, target_words)
               heapq.heappush(queue, (new_cost + h, new_cost, actions + [direction], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a count of the number of characters in the current state that are not in their correct positions in the target words
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a character is moved from its correct position, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of characters that can be moved to their correct positions in the heuristic is by moving the characters that are currently in their correct positions, which is exactly the characters used to fill the board in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != '_' and state[i][j] != target_words[i][j - (i > 0)]:
               h += 1
   return h


print(a_star())
