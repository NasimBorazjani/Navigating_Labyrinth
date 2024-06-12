
import heapq


def a_star():
   # Define the initial state of the stacks, with the topmost block of each stack represented by the leftmost item in the list
   initial_state = [[], [], ['Green', 'Yellow', 'Green', 'Red'], ['Green', 'Red', 'Blue', 'Yellow'], [], ['Blue', 'Red', 'Yellow', 'Blue']]
   num_stacks = 6
   stack_capacity = 4
   # Define the cost of moving a block to the top of each stack
   move_costs = {0: 5, 1: 1, 2: 6, 3: 7, 4: 7, 5: 7}


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If all the blocks are sorted, return the actions taken
       if all(stack == sorted(stack) for stack in state if stack):
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from the top of one stack to another
       for from_stack in range(num_stacks):
           for to_stack in range(num_stacks):
               # Check if transferring a block from the top of the from_stack to the to_stack is valid
               if from_stack != to_stack and (not state[from_stack] or state[from_stack][-1] == state[to_stack][-1] or not state[to_stack] or len(state[to_stack]) < stack_capacity):
                   # Generate the new state after transferring the block
                   new_state = [list(stack[:]) for stack in state]
                   new_state[to_stack].append(new_state[from_stack].pop())
                   new_state = tuple(tuple(stack) for stack in new_state)
                   # Calculate the cost of the transfer
                   new_cost = g + move_costs[from_stack]
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None


print(a_star())
