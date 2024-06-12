
import heapq


def a_star():
   # Define the initial state of the stacks as a tuple of tuples
   initial_state = ((), (), ('White', 'Yellow', 'Yellow', 'Green', 'Blue', 'Green'), ('Red', 'Yellow', 'White', 'Blue', 'Black', 'Black'), ('Black', 'Red', 'Blue', 'Black', 'Green', 'Green'), ('Green', 'Black', 'Yellow', 'Red', 'White', 'Red'), ('White', 'Blue', 'Red', 'Blue', 'White', 'Yellow'), (), (), ())
   num_stacks = 10
   stack_capacity = 6
   # Define the cost of moving a block to each stack
   stack_costs = {0: 4, 1: 1, 2: 1, 3: 9, 4: 2, 5: 9, 6: 1, 7: 9, 8: 6, 9: 4}


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If all stacks are either empty or contain blocks of a single shade, return the actions taken
       if all(len(set(stack)) <= 1 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes moving the top block from any stack to any other stack
       for from_stack_ind in range(num_stacks):
           # Check if the stack is not empty
           if state[from_stack_ind]:
               for to_stack_ind in range(num_stacks):
                   # Check if the stack is not full and if the stack is either empty or contains blocks of the same shade as the block to be moved
                   if len(state[to_stack_ind]) < stack_capacity and (not state[to_stack_ind] or state[to_stack_ind][-1] == state[from_stack_ind][-1]):
                       # Generate the new state
                       new_state = list(list(stack) for stack in state)
                       new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                       new_state = tuple(tuple(stack) for stack in new_state)
                       # The cost of the new state is the cost of moving a block to the to_stack
                       new_cost = g + stack_costs[to_stack_ind]


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is the sum of the costs of moving a block to each stack, multiplied by the number of blocks in the stack, as we are trying to minimize the total cost of moving the blocks
                           h = heuristic(new_state, stack_costs)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, stack_costs):
   # The heuristic is the sum of the costs of moving a block to each stack, multiplied by the number of blocks in the stack, as we are trying to minimize the total cost of moving the blocks
   # The heuristic is admissible because it assumes that we can move all blocks in a stack to the same stack, even if it would result in overfilling the stack or mixing different shades in the same stack, thus reporting a lower cost estimate to reach the goal state
   # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of moving a block from one stack to another is the cost of moving a block to the to_stack, which is always greater than or equal to the cost of moving a block to the same stack in the heuristic
   return sum(stack_costs[i] * len(stack) for i, stack in enumerate(state))


print(a_star())
