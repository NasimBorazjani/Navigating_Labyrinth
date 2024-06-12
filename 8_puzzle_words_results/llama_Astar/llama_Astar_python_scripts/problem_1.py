
import heapq


def a_star():
   # Define the initial state of the board
   initial_state = (['i', 'c', 'a', 'm'], ['h', 'p', 'l', 'o'], ['_', 'r', 'a', 'y'], ['d', 'l', 'e', 'r'])
   # Define the target words
   target_words = ['cam', 'hill', 'pray', 'doer']
   # Define the possible swap directions
   swap_directions = ['up-right', 'down-right', 'up-left', 'down-left']
   # Define the initial state of the board
   initial_state = (['i', 'c', 'a', 'm'], ['h', 'p', 'l', 'o'], ['_', 'r', 'a', 'y'], ['d', 'l', 'e', 'r'])
   # Define the target words
   target_words = ['cam', 'hill', 'pray', 'doer']
   # Define the possible swap directions
   swap_directions = ['up-right', 'down-right', 'up-left', 'down-left']


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == tuple(word[::-1] for word in target_words):
           return actions


       # Generate all possible actions from the current state
       for swap_direction in swap_directions:
           # Generate the new state
           new_state = [list(row[:]) for row in state]
           # Swap the blank space with its diagonal neighbor
           if swap_direction == 'up-right':
               new_state[0][1], new_state[1][0] = new_state[1][0], new_state[0][1]
           elif swap_direction == 'down-right':
               new_state[1][1], new_state[2][0] = new_state[2][0], new_state[1][1]
           elif swap_direction == 'up-left':
               new_state[0][0], new_state[1][1] = new_state[1][1], new_state[0][0]
           elif swap_direction == 'down-left':
               new_state[1][0], new_state[2][1] = new_state[2][1], new_state[1][0]
           new_state = tuple(tuple(row) for row in new_state)
           # The cost so far is the number of swaps made
           new_cost = g + 1


           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
               visited_costs[new_state] = new_cost
               heapq.heappush(queue, (new_cost + heuristic(state, target_words), new_cost, actions + [swap_direction], new_state))
   return None


def heuristic(state, target_words):
   # The heuristic function can be a count of the number of characters in the current state that are not in their correct positions in the goal state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a character is moved from its correct position, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of characters that can be moved to their correct positions in the heuristic is by moving the characters that are currently in their correct positions, which is exactly the characters used to fill the board in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != target_words[i][j]:
               h += 1
   return h


print(a_star())
