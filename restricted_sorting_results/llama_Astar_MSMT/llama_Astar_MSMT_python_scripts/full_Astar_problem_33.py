
import heapq


def initialize():
   # Define the initial state of the stacks as a 2d tuple
   initial_state = (('Black', 'Yellow', 'Green', 'Red', 'Black'),
                   (),
                   ('Red', 'Yellow', 'Green', 'Blue', 'Green'),
                   (),
                   ('Blue', 'Red', 'Blue', 'Green', 'Yellow'),
                   ('Red', 'Blue', 'Yellow', 'Black', 'Black'),
                   (),
                   ())
   num_stacks = 8
   stack_capacity = 5
   # Create the set of the valid block shades
   shades = set(['Black', 'Yellow', 'Green', 'Red', 'Blue'])
   # Define the cost of moving one block to the top of each stack
   move_costs = {0: 1, 1: 6, 2: 6, 3: 2, 4: 9, 5: 2, 6: 9, 7: 6}


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_stacks, stack_capacity, shades, move_costs, visited_costs, queue
  
def a_star():
  
   initial_state, num_stacks, stack_capacity, shades, move_costs, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must not have any blocks in stacks with more than one shade, thus we need to get (the coordinates of) the blocks in the stacks with more than one shade to check whether the current state is the goal state
       blocks_coords = [(i, j) for i, stack in enumerate(state) for j, element in enumerate(stack) if j > 0 and element != state[i][j - 1]]
       if not blocks_coords:
           return actions


       # If the state has at least 1 remaining block in stacks with more than one shade, generate all possible actions from the current state, which includes transferring the next block to the top of a stack with the same shade or to an empty stack
       else:
           first_block_coord = blocks_coords[0]
           # The block must be unique and not be present in any other stacks of the grid
           used_shades  = set(state[i][j] for i, stack in enumerate(state) for j, element in enumerate(stack) if j > 0)
           for shade in shades:
               # Check if the new state, containing the new block, would be valid; ie the block must be unique and the stacks must not exceed their capacity
               stack_new_state = [stack for stack in state]
               stack_new_state[first_block_coord[0]].pop(first_block_coord[1])
               stack_new_state[first_block_coord[0]].append(shade)
               # If the shade of the moved block is the same as the shade of the top block in the destination stack, or the destination stack is empty
               if (shade == state[first_block_coord[0]][first_block_coord[1] - 1] or len(stack_new_state[first_block_coord[0]]) == 1) and len(stack_new_state[first_block_coord[0]]) <= stack_capacity:
              
                   # Generate the new state
                   new_state = tuple(tuple(stack) for stack in stack_new_state)
                   # The additional cost of this state is the value of the move cost
                   new_cost = g + move_costs[first_block_coord[0]]
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # Relaxing the constraints on the stacks to calculate the heuristic
                       h = heuristic(new_state, shades)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(first_block_coord[0], first_block_coord[0], shade)], new_state))
   return None




def heuristic(state, shades):
   # Relax the stacks constraints to compute an admissible and consistent heuristic
   # This heuristic considers the sum of the cost of moving the blocks to the top of the stacks with the same shade as the top block, or to an empty stack
   # The heuristic assumes blocks can be moved to the top of a stack with the same shade or to an empty stack, even if the stacks exceed their capacity, thus reporting a lower cost estimate to reach the goal state, making it admissible
   # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of moving a block is the move cost, which is always greater than or equal to the cost used to calculate the heuristic
   # Also the cost of the goal state is 0, as all blocks are sorted correctly in the stacks


   h = 0
   for i in range(len(state)):
       for j in range(len(state[i]) - 1):
           # If the shade of the moved block is the same as the shade of the top block in the destination stack, or the destination stack is empty
           if state[i][j] == state[i][j + 1] or j == len(state[i]) - 2:
               h += move_costs[i]
   return h


print(a_star())
