
import heapq


def a_star():
   # Define the initial state of the stacks as a tuple of tuples
   initial_state = ((), ('Green', 'Blue', 'Yellow', 'Green'), ('Yellow', 'Red', 'Red', 'Blue'), (), ('Blue', 'Green', 'Yellow', 'Red'), ())
   num_stacks = 6
   stack_capacity = 4
   # Define the cost of moving a block to each stack
   stack_costs = {0: 4, 1: 3, 2: 2, 3: 4, 4: 2, 5: 5}


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state is when all stacks are either empty or contain 3 blocks of the same shade
       if all(len(stack) == 0 or (len(stack) == 3 and len(set(stack)) == 1) for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes moving the top block from any stack to any other stack
       for from_stack_ind in range(num_stacks):
           # Check if the from_stack is not empty
           if state[from_stack_ind]:
               for to_stack_ind in range(num_stacks):
                   # Check if the to_stack is not full and if it is either empty or the top block is of the same shade as the block to be moved
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
                           # The heuristic is the sum of the costs of moving the top block of each stack to another stack, if the stack is not sorted
                           h = heuristic(new_state, stack_costs)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, stack_costs):
   # The heuristic function can be the sum of the costs of moving the top block of each stack to another stack, if the stack is not sorted
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the most blocks, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is moved to a stack with a higher cost, or equal or less by at most the cost of moving a block to the stack with the lowest cost (equal to the cost of reaching the successor node, ie one action) as the maximum number of blocks that can be sorted in the heuristic is by moving a block to the stack with the lowest cost, which is exactly the stack used to sort the blocks in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to the cost of moving a block to the stack with the lowest cost) + h(n’)
   h = 0
   for stack in state:
       if stack and (len(stack) != 3 or len(set(stack)) != 1):
           h += min(stack_costs.values())
   return h


print(a_star())
