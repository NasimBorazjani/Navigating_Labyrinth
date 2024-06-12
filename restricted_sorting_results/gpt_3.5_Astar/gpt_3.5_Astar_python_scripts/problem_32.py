
import heapq


def a_star():
   # Define the initial state of the stacks, with the colors represented as integers
   initial_state = [[0, 1, 2, 1, 3], [], [], [], [], [2, 4, 2, 4, 2], [1, 0, 4, 1, 0], [3, 3, 3, 4, 0]]
   num_stacks = 8
   stack_capacity = 5
   # Define the cost of moving a block to the top of each stack
   stack_costs = {0: 5, 1: 8, 2: 1, 3: 6, 4: 8, 5: 2, 6: 1, 7: 8}


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If all stacks are sorted, return the actions taken
       if all(stack == sorted(stack) for stack in state if stack):
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from the top of one stack to another
       for from_stack in range(num_stacks):
           for to_stack in range(num_stacks):
               if from_stack != to_stack:
                   # Check if the from_stack is not empty and the to_stack has space for another block of the same shade
                   if state[from_stack] and (not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]) and len(state[to_stack]) < stack_capacity:
                       # Generate the new state after the block transfer
                       new_state = [list(stack[:]) for stack in state]
                       new_state[from_stack].pop()
                       new_state[to_stack].append(state[from_stack][-1])
                       new_state = tuple(tuple(stack) for stack in new_state)
                       # Calculate the cost of the transfer
                       new_cost = g + stack_costs[from_stack]
                      
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None


print(a_star())
