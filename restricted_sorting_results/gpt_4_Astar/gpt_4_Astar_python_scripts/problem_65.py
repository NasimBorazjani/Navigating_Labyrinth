
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = ([], ['Yellow', 'White', 'Blue', 'Yellow', 'Red', 'White'], [], [], ['Blue', 'Blue', 'Green', 'Black', 'Black', 'Red'], ['Black', 'Green', 'Yellow', 'Yellow', 'Blue', 'Black'], [], ['White', 'Blue', 'Green', 'White', 'Yellow', 'Red'], [], ['Green', 'White', 'Black', 'Red', 'Green', 'Red'])
   num_stacks = 10
   stack_capacity = 6
   # Define the cost of moving a block to each stack
   stack_costs = {0: 3, 1: 6, 2: 3, 3: 6, 4: 9, 5: 6, 6: 6, 7: 10, 8: 2, 9: 5}


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
                       new_state = [stack[:] for stack in state]
                       new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                       new_state = tuple(tuple(stack) for stack in new_state)
                       # The cost of moving a block is the cost of moving a block to the destination stack
                       new_cost = g + stack_costs[to_stack_ind]


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is the sum of the number of blocks in each stack that are not of the same shade as the top block in the stack, as these blocks will need to be moved
                           h = heuristic(new_state)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state):
   # The heuristic function can be the sum of the number of blocks in each stack that are not of the same shade as the top block in the stack, as these blocks will need to be moved
   # This heuristic is admissible because it never overestimates the cost to reach the goal state, as it assumes that we can move the blocks to any stack without any cost, thus reporting a lower cost estimate to reach the goal state
   # The heuristic is consistent because the estimated cost of the next node is higher if a block is moved to a stack with blocks of a different shade, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of blocks that can be moved to a stack is the number of blocks in the stack that are not of the same shade as the top block, which is exactly the number of blocks moved in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for stack in state:
       if stack:
           h += len([block for block in stack if block != stack[-1]])
   return h


print(a_star())
