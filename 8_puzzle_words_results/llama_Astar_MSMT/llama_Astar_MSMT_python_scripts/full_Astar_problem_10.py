
import heapq


def initialize():
   # Define the initial state of the board and the target words
   initial_state = [['u', 'k', 'd', 'x'], ['t', 'e', 'r', 'b'], ['w', 'a', '_', 'i'], ['t', 'e', 's', 't']]
   target_words = ['kex', 'turd', 'wabi', 'test']


   # Encode the valid directions for the blank space
   directions = ['up-right', 'down-right', 'up-left', 'down-left']


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, target_words, directions, visited_costs, queue
  
def a_star():
  
   initial_state, target_words, directions, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == target_words:
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for direction in directions:
           # Generate the new state
           new_state = [list(row[:]) for row in state]
           # Swap the blank space with the neighboring tile in the given direction
           if direction == 'up-right':
               new_state[1][0], new_state[0][1] = new_state[0][1], new_state[1][0]
           elif direction == 'down-right':
               new_state[2][0], new_state[1][1] = new_state[1][1], new_state[2][0]
           elif direction == 'up-left':
               new_state[0][2], new_state[1][1] = new_state[1][1], new_state[0][2]
           elif direction == 'down-left':
               new_state[1][2], new_state[2][1] = new_state[2][1], new_state[1][2]
           new_state = [''.join(row) for row in new_state]
           # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
           new_cost = g + 1


           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
               visited_costs[new_state] = new_cost
               # The heuristic function is not needed in this problem as the goal state is deterministic from the initial state and the direction of the swaps
               heapq.heappush(queue, (new_cost, new_cost, actions + [direction], new_state))
   return None


print(a_star())
