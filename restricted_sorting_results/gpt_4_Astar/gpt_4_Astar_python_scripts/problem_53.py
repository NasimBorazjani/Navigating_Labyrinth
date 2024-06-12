
import heapq


def a_star():
   # Define the initial state of the stacks as a 2d tuple
   initial_state = ((), ('Blue', 'Green', 'Red', 'Yellow', 'Blue'), ('Green', 'Blue', 'Yellow', 'Black', 'Red'), (), ('Red', 'Yellow', 'Yellow', 'Black', 'Black'), ('Green', 'Blue', 'Green', 'Black', 'Red'), (), ())
   num_stacks = 8
   stack_capacity = 5
   # Define the cost of moving a block to each stack
   stack_costs = {0: 7, 1: 4, 2: 1, 3: 2, 4: 6, 5: 8, 6: 7, 7: 6}


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
           # Check if the stack is not empty
           if state[from_stack_ind]:
               for to_stack_ind in range(num_stacks):
                   # Check if the stack is not full and if the stack is either empty or contains blocks of the same shade as the block to be moved
                   if (len(state[to_stack_ind]) < stack_capacity and
                       (not state[to_stack_ind] or state[to_stack_ind][-1] == state[from_stack_ind][-1])):
                       # Generate the new state
                       new_state = list(list(stack) for stack in state)
                       new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                       new_state = tuple(tuple(stack) for stack in new_state)
                       # The cost of the new state is the cost of moving a block to the to_stack
                       new_cost = g + stack_costs[to_stack_ind]


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is the sum of the costs of moving the top block of each stack to a stack that is either empty or contains blocks of the same shade
                           h = heuristic(new_state, stack_costs)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, stack_costs):
   # The heuristic is the sum of the costs of moving the top block of each stack to a stack that is either empty or contains blocks of the same shade
   # The heuristic is admissible because it assumes that we can move the top block of each stack to any other stack, even if the stack is full or contains blocks of a different shade, thus reporting a lower cost estimate to reach the goal state
   # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of moving a block from one stack to another is the cost of moving a block to the to_stack, which is always greater than or equal to the cost of moving the block to the same stack in the heuristic
   # Also the cost of the goal state is 0, as all stacks are either empty or contain blocks of a single shade and there are no blocks to move
   h = 0
   for stack in state:
       if stack:
           # Get the indices of the stacks that are either empty or contain blocks of the same shade as the top block of the current stack
           valid_to_stack_inds = [i for i, to_stack in enumerate(state) if not to_stack or to_stack[-1] == stack[-1]]
           # Add the minimum cost of moving the block to these stacks to the heuristic
           h += min(stack_costs[ind] for ind in valid_to_stack_inds)
   return h


print(a_star())
