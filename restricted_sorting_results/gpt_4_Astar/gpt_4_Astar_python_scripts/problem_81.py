
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = ([], ['White', 'Black', 'Yellow', 'Black', 'Green', 'Blue', 'Pink'], ['Black', 'Red', 'Yellow', 'White', 'Yellow', 'Black', 'Green'], ['Yellow', 'White', 'Green', 'White', 'White', 'Black', 'Blue'], ['Blue', 'Pink', 'Red', 'Pink', 'Green', 'Yellow', 'Black'], ['White', 'Red', 'Pink', 'Blue', 'Blue', 'Pink', 'Green'], [], [], [], ['Red', 'Pink', 'Red', 'Blue', 'Red', 'Green', 'Yellow'], [], [])
   num_stacks = 12
   stack_capacity = 7
   # Define the cost of moving a block to each stack
   stack_costs = {0: 5, 1: 3, 2: 3, 3: 4, 4: 2, 5: 2, 6: 12, 7: 9, 8: 5, 9: 11, 10: 11, 11: 10}


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
                   # Check if the stack is not full and if the stack is either empty or the top block is of the same shade as the block to be moved
                   if len(state[to_stack_ind]) < stack_capacity and (not state[to_stack_ind] or state[to_stack_ind][-1] == state[from_stack_ind][-1]):
                       # Generate the new state
                       new_state = [stack[:] for stack in state]
                       new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                       new_state = tuple(tuple(stack) for stack in new_state)
                       # The cost of the new state is the cost of moving a block to the to_stack
                       new_cost = g + stack_costs[to_stack_ind]


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is the sum of the costs of moving the remaining blocks in the stacks to the stack with the lowest cost, as we are trying to minimize the cost of sorting the blocks
                           h = heuristic(new_state, stack_costs)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, stack_costs):
   # The heuristic function can be a simulation of moving all the remaining blocks to the stack with the lowest cost
   # This heuristic is admissible because it is greedy, always opting for the action that costs the least, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is moved from a stack, or equal or less by at most the cost of moving a block to the stack with the lowest cost (equal to the cost of reaching the successor node, ie one action) as the maximum number of blocks that can be moved to a stack is the capacity of the stack, which is exactly the number of blocks moved to the stack in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to the cost of moving a block to the stack with the lowest cost) + h(n’)
   h = 0
   # Get the cost of moving a block to the stack with the lowest cost
   min_stack_cost = min(stack_costs.values())
   # Add the cost of moving all the remaining blocks to the stack with the lowest cost to the heuristic
   for stack in state:
       h += len(stack) * min_stack_cost
   return h


print(a_star())
