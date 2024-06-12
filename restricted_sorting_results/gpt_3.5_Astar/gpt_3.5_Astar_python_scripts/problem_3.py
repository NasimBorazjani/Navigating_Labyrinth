
import heapq


def a_star():
   # Define the initial state of the stacks, with the topmost block in each stack represented by the leftmost item in the list
   initial_state = [[], ['Yellow', 'Green', 'Red', 'Red'], ['Blue', 'Green', 'Red', 'Green'], ['Yellow', 'Blue', 'Yellow', 'Blue'], [], []]
   num_stacks = 6
   stack_capacity = 4
   # Define the cost of moving a block to the top of each stack
   stack_costs = {0: 3, 1: 6, 2: 5, 3: 6, 4: 1, 5: 1}


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If all the blocks are sorted, return the actions taken
       if all(all(stack[i] == stack[0] for i in range(len(stack))) for stack in state if stack):
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from the top of one stack to another
       for from_stack in range(num_stacks):
           for to_stack in range(num_stacks):
               # Check if the transfer is valid, ie if the from_stack is not empty, the to_stack is not full, and the top block of the from_stack matches the top block of the to_stack or the to_stack is empty
               if state[from_stack] and (not state[to_stack] or state[from_stack][0] == state[to_stack][0]) and len(state[to_stack]) < stack_capacity:
                   # Generate the new state after the transfer
                   new_state = [list(stack[:]) for stack in state]
                   new_state[from_stack].pop(0)
                   new_state[to_stack].insert(0, state[from_stack][0])
                   new_state = tuple(tuple(stack) for stack in new_state)
                   # The cost of the new state is the cost of moving the block from the from_stack to the to_stack
                   new_cost = g + stack_costs[to_stack]
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None


print(a_star())
