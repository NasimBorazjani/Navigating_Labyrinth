
import heapq


def a_star():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('u', 'm', 'a', 'n'),
                   ('c', 'd', 't', 'e'),
                   ('o', 'a', '_', 'y'),
                   ('d', 'n', 'w', 'y'),
                   ('o', 'r', 'z', 'x'))
   # Define the target words
   target_words = ['man', 'cute', 'dazy', 'down', 'oryx']
   # Define the possible swap directions
   swap_directions = ['ur', 'dr', 'ul', 'dl']
   # Define the possible blank space positions
   blank_positions = [(2, 1), (1, 2), (0, 3), (3, 3)]


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
           for blank_position in blank_positions:
               # Check if the new state would be valid
               new_state = [list(row[:]) for row in state]
               # Swap the blank space with its neighbor in the given direction
               if swap_direction == 'ur':
                   new_state[blank_position[0]][blank_position[1]], new_state[blank_position[0] - 1][blank_position[1] + 1] = new_state[blank_position[0] - 1][blank_position[1] + 1], new_state[blank_position[0]][blank_position[1]]
               elif swap_direction == 'dr':
                   new_state[blank_position[0]][blank_position[1]], new_state[blank_position[0] + 1][blank_position[1] + 1] = new_state[blank_position[0] + 1][blank_position[1] + 1], new_state[blank_position[0]][blank_position[1]]
               elif swap_direction == 'ul':
                   new_state[blank_position[0]][blank_position[1]], new_state[blank_position[0] - 1][blank_position[1] - 1] = new_state[blank_position[0] - 1][blank_position[1] - 1], new_state[blank_position[0]][blank_position[1]]
               else:
                   new_state[blank_position[0]][blank_position[1]], new_state[blank_position[0] + 1][blank_position[1] - 1] = new_state[blank_position[0] + 1][blank_position[1] - 1], new_state[blank_position[0]][blank_position[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic function can be a simple count of the number of characters in the wrong position
                   h = heuristic(new_state, target_words)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [(swap_direction, blank_position)], new_state))
   return None




def heuristic(state, target_words):
   # The heuristic function can be a simple count of the number of characters in the wrong position
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != target_words[i][j - (i > 0)]:
               h += 1
   return h


print(a_star())
