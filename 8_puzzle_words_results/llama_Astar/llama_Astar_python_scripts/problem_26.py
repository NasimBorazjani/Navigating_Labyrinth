
import heapq


def a_star():
   # Define the initial state of the board and the target words
   initial_state = [['t', 'w', 'y', 'l', '_'],
                   ['s', 'a', 'u', 'f', 't'],
                   ['o', 'a', 'e', 'm', 'n'],
                   ['f', 'l', 'd', 'm', 'd']]
   target_words = ['wolf', 'stunt', 'lammy', 'faded']


   # Define the possible directions for swapping the blank space
   directions = [(-1, 1), (1, 1), (-1, -1), (1, -1)]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == [list(word) for word in target_words]:
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for direction in directions:
           new_state = [list(row[:]) for row in state]
           # Get the coordinates of the blank space
           blank_coord = [i for i, row in enumerate(new_state) for j, cell in enumerate(row) if cell == '_']
           # Get the coordinates of the cell to which the blank space would be swapped
           new_coord = (blank_coord[0] + direction[0], blank_coord[1] + direction[1])
           # Check if the new state would be valid, ie the new cell must be within the bounds of the board
           if 0 <= new_coord[0] < len(new_state) and 0 <= new_coord[1] < len(new_state[0]):
               # Swap the blank space with the new cell
               new_state[blank_coord[0]][blank_coord[1]], new_state[new_coord[0]][new_coord[1]] = new_state[new_coord[0]][new_coord[1]], new_state[blank_coord[0]][blank_coord[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The direction of the swap is added to the actions taken
                   heapq.heappush(queue, (new_cost + heuristic(state, target_words, directions), new_cost, actions + [direction], new_state))
   return None




def heuristic(state, target_words, directions):
   # The heuristic function can be a simulation of swapping the blank space greedily, using the next direction in the directions list as long as the word in the current row matches the target word
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the board the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a swap does not result in a word match, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of swaps that can be made is by using the largest direction that won't cause a word mismatch. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       word = ''.join(state[i])
       # If the word in the current row matches the target word, increment the estimated cost to the goal by 1 actions
       if word == target_words[i]:
           h += 1
   return h


print(a_star())
