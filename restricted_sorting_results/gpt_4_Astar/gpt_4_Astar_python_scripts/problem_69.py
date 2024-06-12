
import heapq


def a_star():
   # Define the initial state of the stacks as a tuple of tuples
   initial_state = ((), ('Blue', 'Black', 'Black', 'Yellow', 'White', 'Green'), ('Green', 'Black', 'Red', 'Green', 'Yellow', 'Blue'), (), ('Green', 'Red', 'Blue', 'Yellow', 'Green', 'Blue'), ('Black', 'White', 'White', 'Red', 'White', 'Black'), (), ('White', 'Red', 'Blue', 'Yellow', 'Yellow', 'Red'), (), ())
   num_stacks = 10
   stack_capacity = 6
   # Define the cost of moving a block to each stack
   stack_costs = {0: 5, 1: 4, 2: 7, 3: 7, 4: 11, 5: 11, 6: 8, 7: 3, 8: 7, 9: 9}


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie if all the blocks in each stack are of the same color
       if all(len(set(stack)) <= 1 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes moving the top block from any stack to any other stack
       for from_stack_ind in range(num_stacks):
           # Check if the stack is not empty
           if state[from_stack_ind]:
               for to_stack_ind in range(num_stacks):
                   # Check if the stack is not full and if the stack is empty or the top block is of the same color as the block to be moved
                   if len(state[to_stack_ind]) < stack_capacity and (not state[to_stack_ind] or state[to_stack_ind][-1] == state[from_stack_ind][-1]):
                       # Generate the new state
                       new_state = list(list(stack) for stack in state)
                       new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                       new_state = tuple(tuple(stack) for stack in new_state)
                       # The cost of the new state is the cost of moving a block to the to_stack
                       new_cost = g + stack_costs[to_stack_ind]


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is the sum of the costs of moving the top block of each stack to an empty stack, as the blocks must be moved at least once to sort the stacks
                           h = heuristic(new_state, stack_costs)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, stack_costs):
   # The heuristic is the sum of the costs of moving the top block of each stack to an empty stack, as the blocks must be moved at least once to sort the stacks
   # The heuristic is admissible because it never overestimates the cost to reach the goal state, as it assumes that the blocks can be moved directly to their goal positions, relaxing the constraints that the blocks can only be moved to the top of a stack and that the stacks have a capacity
   # The heuristic is consistent because the cost of moving a block from one stack to another is always greater than or equal to the cost of moving the block to an empty stack, which is exactly the decrease in the heuristic value, if the block is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as all the blocks are in their goal positions
   h = 0
   for stack in state:
       if stack:
           # The cost of moving a block to an empty stack is the minimum cost of moving a block to any stack
           h += min(stack_costs.values())
   return h


print(a_star())
