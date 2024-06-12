
import heapq


def a_star():
   # Define the initial state of the stacks, with the colors represented as integers
   initial_state = [[1, 2, 2, 1], [0, 0, 4, 2], [], [], [4, 0, 4, 1], []]
   num_stacks = 6
   stack_capacity = 4
   # Define the cost of moving a block to the top of each stack
   stack_costs = {0: 2, 1: 2, 2: 3, 3: 7, 4: 1, 5: 7}


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
                   # Check if the transfer is valid, ie if the from_stack is not empty and the to_stack is either empty or the top block of the to_stack is of the same shade as the block being transferred
                   if state[from_stack] and (not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]):
                       # Generate the new state
                       new_state = [list(stack[:]) for stack in state]
                       new_state[from_stack].pop()
                       new_state[to_stack].append(state[from_stack][-1])
                       new_state = tuple(tuple(stack) for stack in new_state)
                       # The cost of the new state is the cost of moving the block from the from_stack to the to_stack
                       new_cost = g + stack_costs[to_stack]
                      
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None


print(a_star())
