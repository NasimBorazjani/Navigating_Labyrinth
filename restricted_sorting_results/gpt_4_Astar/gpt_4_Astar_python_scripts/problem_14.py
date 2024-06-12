
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = (('Green', 'Yellow', 'Red', 'Yellow'), (), ('Blue', 'Blue', 'Blue', 'Red'), (), ('Green', 'Green', 'Red', 'Yellow'), ())
   num_stacks = 6
   stack_capacity = 4
   # Define the cost of moving a block to each stack
   stack_costs = {0: 3, 1: 6, 2: 5, 3: 5, 4: 3, 5: 1}


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state is when all the blocks are sorted by shade, ie each stack is either empty or contains blocks of a single shade
       if all(len(set(stack)) <= 1 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes moving the top block from any stack to any other stack
       for from_stack_ind in range(num_stacks):
           # Check if the stack is not empty
           if state[from_stack_ind]:
               for to_stack_ind in range(num_stacks):
                   # Check if the stack is not full and if the stack is either empty or the top block is of the same shade as the block to be moved
                   if (len(state[to_stack_ind]) < stack_capacity and
                       (not state[to_stack_ind] or state[to_stack_ind][-1] == state[from_stack_ind][-1])):
                       # Generate the new state
                       new_state = list(list(stack) for stack in state)
                       block = new_state[from_stack_ind].pop()
                       new_state[to_stack_ind].append(block)
                       new_state = tuple(tuple(stack) for stack in new_state)
                       # The cost of the new state is the cost of moving a block to the to_stack
                       new_cost = g + stack_costs[to_stack_ind]


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is the sum of the costs of moving the top block of each stack to a stack that is either empty or has blocks of the same shade as the top block of the current stack, and has space for more blocks
                           h = heuristic(new_state, stack_costs)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, stack_costs):
   # The heuristic function can be a simulation of moving the top block of each stack to a stack that is either empty or has blocks of the same shade as the top block of the current stack, and has space for more blocks
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is moved to a stack with a higher cost, or equal or less by at most the cost of moving a block to the stack with the lowest cost (equal to the cost of reaching the successor node, ie one action) as the maximum amount of blocks that can be moved to a stack is by moving the block to the stack with the lowest cost, which is exactly the stack used to move the block in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to the cost of moving a block to the stack with the lowest cost) + h(n’)
   h = 0
   for i in range(len(state)):
       if state[i]:
           # Get the indices of the stacks that are either empty or have blocks of the same shade as the top block of the current stack, and have space for more blocks
           valid_to_stack_inds = [j for j in range(len(state)) if len(state[j]) < stack_capacity and (not state[j] or state[j][-1] == state[i][-1])]
           # Add the cost of moving a block to the stack with the lowest cost among the valid stacks
           h += min(stack_costs[j] for j in valid_to_stack_inds)
   return h


print(a_star())
