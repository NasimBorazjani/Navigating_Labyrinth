
import heapq


def a_star():
   # Define the initial state of the stacks, with the colors represented as integers
   initial_state = [[0, 1, 2, 3], [], [1, 3, 3, 2], [], [0, 0, 2, 1], []]
   num_stacks = 6
   stack_capacity = 4
   # Define the cost of moving a block to the top of each stack
   stack_costs = {0: 2, 1: 3, 2: 3, 3: 6, 4: 1, 5: 6}


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If all stacks are sorted, return the actions taken
       if all(stack == sorted(stack) for stack in state if stack):
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from one stack to another
       for from_stack in range(num_stacks):
           for to_stack in range(num_stacks):
               if from_stack != to_stack:
                   # Check if the from_stack is not empty and the to_stack has space for another block
                   if state[from_stack] and len(state[to_stack]) < stack_capacity:
                       new_state = [list(stack[:]) for stack in state]
                       # Get the color of the block being transferred
                       block_color = new_state[from_stack][-1]
                       # Check if the block can be transferred to the to_stack based on the color of the block and the blocks already present in the to_stack
                       if not new_state[to_stack] or new_state[to_stack][-1] == block_color:
                           new_state[to_stack].append(new_state[from_stack].pop())
                           new_state = tuple(tuple(stack) for stack in new_state)
                           # Calculate the cost of the transfer based on the cost of moving a block to the top of the to_stack
                           new_cost = g + stack_costs[to_stack]
                          
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None


print(a_star())
