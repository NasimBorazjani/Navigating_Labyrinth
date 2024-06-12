
import heapq


def a_star():
   # Define the initial state of the stacks as a 2d tuple
   initial_state = ((), (), ('Blue', 'Yellow', 'Red', 'Black', 'White', 'Blue'), ('Blue', 'Green', 'Yellow', 'Red', 'Red', 'White'), (), ('Red', 'Black', 'White', 'Yellow', 'White', 'Green'), (), ('Black', 'Yellow', 'Green', 'Black', 'Black', 'Blue'), (), ('Red', 'Green', 'Green', 'Blue', 'Yellow', 'White'))
   num_stacks = 10
   stack_capacity = 6
   # Define the cost of moving a block to each stack
   stack_costs = {0: 6, 1: 10, 2: 8, 3: 3, 4: 5, 5: 7, 6: 10, 7: 6, 8: 3, 9: 8}


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state is when all stacks are either empty or contain blocks of a single shade
       if all(len(set(stack)) <= 1 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes moving the top block from any stack to any other stack
       for from_stack_ind in range(num_stacks):
           # Check if the from_stack is not empty
           if state[from_stack_ind]:
               for to_stack_ind in range(num_stacks):
                   # Check if the to_stack has less than 6 blocks and is either empty or the top block is of the same shade as the block to be moved
                   if len(state[to_stack_ind]) < stack_capacity and (not state[to_stack_ind] or state[to_stack_ind][-1] == state[from_stack_ind][-1]):
                       # Generate the new state
                       new_state = list(list(stack) for stack in state)
                       new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                       new_state = tuple(tuple(stack) for stack in new_state)
                       # The cost of the new state is the cost of moving a block to the to_stack
                       new_cost = g + stack_costs[to_stack_ind]


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is 0 as we don't have any information on the goal state, other than the blocks must be sorted
                           heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None


print(a_star())
