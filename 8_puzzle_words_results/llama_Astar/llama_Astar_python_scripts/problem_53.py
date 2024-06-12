
import heapq


def a_star():
   # Define the initial state of the board
   initial_state = (['o', 'l', 's', 'm', '_', 'n'],
                   ['s', 'o', 'm', 'e', 'r', 'k'],
                   ['s', 'p', 'i', 'o', 'e', 'y'],
                   ['d', 'o', 'g', 't', 'i', 'e'])
   # Define the target words
   target_words = ['limen', 'somers', 'spooky', 'dogtie']
   # Define the possible directions for swapping
   directions = ['ur', 'dr', 'ul', 'dl']
   # Define the initial cost and the heuristic cost
   initial_cost = 0
   heuristic_cost = 0


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == tuple(word[::-1] for word in target_words):
           return actions


       # Generate all possible actions from the current state
       for direction in directions:
           # Generate the new state
           new_state = [list(word[::-1]) for word in state]
           # Swap the blank space according to the direction
           if direction == 'ur':
               new_state[0][0], new_state[1][1] = new_state[1][1], new_state[0][0]
           elif direction == 'dr':
               new_state[1][0], new_state[2][1] = new_state[2][1], new_state[1][0]
           elif direction == 'ul':
               new_state[0][1], new_state[1][0] = new_state[1][0], new_state[0][1]
           elif direction == 'dl':
               new_state[1][1], new_state[2][0] = new_state[2][0], new_state[1][1]
           # The new state is a tuple
           new_state = tuple(tuple(word) for word in new_state)
           # The cost so far is the number of actions taken
           new_cost = g + 1


           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
               visited_costs[new_state] = new_cost
               # The heuristic cost is the sum of the differences between the current state and the target state
               h = heuristic(state, target_words)
               heapq.heappush(queue, (new_cost + h, new_cost, actions + [direction], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function calculates the sum of the differences between the current state and the target state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent because the estimated cost of the next node is higher if a swap results in a further distance from the goal, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum distance that can be reduced by a swap is by using the swap that reduces the distance the most
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           h += abs(state[i][j] - target_words[i][j])
   return h


print(a_star())
