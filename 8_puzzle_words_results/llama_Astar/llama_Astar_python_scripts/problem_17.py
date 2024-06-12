
import heapq


def a_star():
   # Define the initial state of the board as a 2d tuple
   initial_state = (['e', 'h', 'r', 'y'],
                   ['w', 'f', 'r', 'r'],
                   ['_', 'u', 'd', 'd'],
                   ['f', 'a', 'i', 'b'])
   # Define the target words
   target_words = ['hay', 'werf', 'rudd', 'frib']
   # Define the possible directions for the blank space to swap
   directions = ['up-right', 'down-right', 'up-left', 'down-left']


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == tuple(word.split() for word in target_words):
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
               # The heuristic function is not needed in this problem as the goal state is always reachable and the cost to reach the goal is always the same, ie the number of swaps made
               heapq.heappush(queue, (new_cost, new_cost, actions + [direction], new_state))
   return None


print(a_star())
