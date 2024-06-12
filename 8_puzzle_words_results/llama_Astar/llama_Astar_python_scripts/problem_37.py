
import heapq


def a_star():
   # Define the initial state of the board and the target words
   initial_state = [['e', 'u', 'n', 'a', '_', 'e'],
                   ['d', 'r', 'a', 'v', 'i', 'e'],
                   ['m', 'a', 'n', 'u', 'k', 'a'],
                   ['k', 'h', 'a', 't', 'u', 'm']]
   target_words = ['uvate', 'dearie', 'manuka', 'khanum']


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
           # Calculate the new coordinates of the blank space after swapping
           new_coord = (blank_coord[0] + direction[0], blank_coord[1] + direction[1])
           # Check if the new coordinates are valid, ie within the bounds of the board
           if 0 <= new_coord[0] < len(new_state) and 0 <= new_coord[1] < len(new_state[0]):
               # Swap the blank space with the new cell
               new_state[blank_coord[0]][blank_coord[1]], new_state[new_coord[0]][new_coord[1]] = new_state[new_coord[0]][new_coord[1]], new_state[blank_coord[0]][blank_coord[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to sort the board
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic function is not needed in this problem as the goal state is always reachable and the cost to reach the goal is always the same, ie the number of swaps made
                   heapq.heappush(queue, (new_cost, new_cost, actions + [direction], new_state))
   return None


print(a_star())
