
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = ([], ['Green', 'Red', 'Yellow', 'Blue'], [], ['Red', 'Blue', 'Yellow', 'Green'], ['Red', 'Yellow', 'Blue', 'Green'], [])
   num_stacks = 6
   stack_capacity = 4
   # Define the cost of moving a block to each stack
   stack_costs = {0: 4, 1: 2, 2: 5, 3: 2, 4: 4, 5: 1}


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when all stacks are either empty or contain 3 blocks of the same shade
       if all(len(stack) == 0 or (len(stack) == 3 and len(set(stack)) == 1) for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes moving the top block from any stack to any other stack
       for from_stack_ind in range(num_stacks):
           # Check if the stack has any blocks to move
           if state[from_stack_ind]:
               for to_stack_ind in range(num_stacks):
                   # Check if the stack can receive a block, ie it is either empty or contains only blocks of the same shade as the block being moved, and it is not full
                   if (not state[to_stack_ind] or
                       (state[to_stack_ind][-1] == state[from_stack_ind][-1] and len(state[to_stack_ind]) < stack_capacity)):
                       # Generate the new state
                       new_state = [list(stack[:]) for stack in state]
                       new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                       new_state = tuple(tuple(stack) for stack in new_state)
                       # The cost of the new state is the cost of moving a block to the stack
                       new_cost = g + stack_costs[to_stack_ind]


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is 0 as the cost of the goal state is not known
                           heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None


print(a_star())
