
import heapq


def a_star():
   # Define the initial state of the board
   initial_state = (['e', 'c', 'o', 'r', 'e'],
                   ['r', 'e', 'u', 't', 'l'],
                   ['r', 'i', 'i', 'c', 'i'],
                   ['k', 'n', 'z', 'e', 'l'],
                   ['i', 'z', 'h', 'l', '_'])
   # Define the target words
   target_words = ['core', 'reuel', 'rinch', 'kizil', 'iztle']
   # Define the possible swap directions
   swap_directions = [(-1, 1), (1, 1), (-1, -1), (1, -1)]
   # Define the initial cost and the heuristic cost
   initial_cost = 0
   heuristic_cost = 0


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == tuple(list(word) for word in target_words):
           return actions


       # Generate all possible actions from the current state
       for swap_direction in swap_directions:
           # Get the new state by swapping the blank space with its neighbor in the given direction
           new_state = [list(row[:]) for row in state]
           blank_row, blank_col = next(i for i, row in enumerate(new_state) if '_' in row)
           new_state[blank_row][blank_col], new_state[blank_row + swap_direction[0]][blank_col + swap_direction[1]] = new_state[blank_row + swap_direction[0]][blank_col + swap_direction[1]], new_state[blank_row][blank_col]
           new_state = tuple(tuple(row) for row in new_state)
           # The cost so far is the number of swaps made
           new_cost = g + 1


           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
               visited_costs[new_state] = new_cost
               # The heuristic cost is the sum of the distances between the current state and the goal state
               h = heuristic(state, target_words)
               heapq.heappush(queue, (new_cost + h, new_cost, actions + [swap_direction], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function calculates the sum of the distances between the current state and the goal state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # The heuristic is consistent because the estimated cost of the next node is higher if a swap results in a further distance from the goal, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum distance that can be obtained by swapping with a neighboring tile is by swapping with the tile that is farthest from the goal
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != target_words[i][j]:
               h += 1
   return h


print(a_star())
