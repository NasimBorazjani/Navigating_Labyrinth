
import heapq


def a_star():
   # Define the initial state of the stacks, with the leftmost item being the shade of the topmost block in each stack
   initial_state = [[], ['Blue', 'Black', 'Blue', 'Yellow', 'Red'], ['Red', 'Green', 'Black', 'Green', 'Black'], [], ['Red', 'Red', 'Green', 'Yellow', 'Yellow'], [], [], ['Blue', 'Yellow', 'Green', 'Black', 'Blue']]
   num_stacks = 8
   stack_capacity = 5
   # Define the cost of moving one block to the top of each stack
   stack_costs = {0: 3, 1: 2, 2: 1, 3: 7, 4: 5, 5: 5, 6: 6, 7: 4}


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If all stacks are sorted, return the list of transfer pairs
       if all(all(stack[i] == stack[0] for i in range(len(stack))) for stack in state if stack):
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from the top of one stack to another
       for from_stack in range(num_stacks):
           for to_stack in range(num_stacks):
               # Check if transferring a block from the top of the from_stack to the to_stack is valid
               if from_stack != to_stack and state[from_stack] and (not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]):
                   new_state = [list(stack[:]) for stack in state]
                   new_state[from_stack].pop()
                   new_state[to_stack].append(state[from_stack][-1])
                   new_state = tuple(tuple(stack) for stack in new_state)
                   # Calculate the cost of the transfer based on the cost of moving a block to the top of the stack
                   new_cost = g + stack_costs[to_stack]
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None


print(a_star())
