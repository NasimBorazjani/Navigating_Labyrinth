
import heapq


def a_star():
   # Define the initial state of the board and the target words
   initial_state = [['y', 't', 's', 'n', 'a', 'r'],
                   ['m', 'r', 'r', 't', 'o', 'e'],
                   ['l', 'o', '_', 'd', 'l', 'n'],
                   ['e', 'u', 'v', 'i', 'r', 'a'],
                   ['h', 'e', 'l', 'm', 'a', 'n']]
   target_words = ['tuner', 'myrtol', 'soldan', 'elvira', 'herman']


   # Define the possible directions for swapping the blank space
   directions = ['up-right', 'down-right', 'up-left', 'down-left']


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == [list(word) for word in target_words]:
           return actions


       # Generate all possible actions from the current state
       for direction in directions:
           # Generate the new state by swapping the blank space in the current state
           new_state = [list(row[:]) for row in state]
           if direction == 'up-right':
               new_state[i][j], new_state[i - 1][j + 1] = new_state[i - 1][j + 1], new_state[i][j]
           elif direction == 'down-right':
               new_state[i][j], new_state[i + 1][j + 1] = new_state[i + 1][j + 1], new_state[i][j]
           elif direction == 'up-left':
               new_state[i][j], new_state[i - 1][j - 1] = new_state[i - 1][j - 1], new_state[i][j]
           elif direction == 'down-left':
               new_state[i][j], new_state[i + 1][j - 1] = new_state[i + 1][j - 1], new_state[i][j]
           new_state = tuple(tuple(row) for row in new_state)
           # The cost so far is the number of actions taken, as the task is to minimize the number of actions required
           new_cost = g + 1


           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
               visited_costs[new_state] = new_cost
               h = heuristic(state, target_words)
               heapq.heappush(queue, (new_cost + h, new_cost, actions + [direction], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a count of the number of characters in the current state that are not in their correct positions in the target words
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a character is moved from its correct position, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of characters that can be moved to their correct positions in the heuristic is by moving the characters that are not in their correct positions in the current state. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != '_' and state[i][j] != target_words[i][j - (i > 0)]:
               h += 1
   return h


print(a_star())
