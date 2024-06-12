
import heapq


def a_star():
   # Define the initial state of the stacks, with the leftmost item being the shade of the topmost block in each stack
   initial_state = [['Yellow', 'Yellow', 'Red', 'Red'], [], ['Blue', 'Yellow', 'Red', 'Green'], [], ['Green', 'Blue', 'Green', 'Blue'], []]
   num_stacks = 6
   stack_capacity = 4
   # Define the cost of moving one block to the top of each stack
   stack_costs = {0: 7, 1: 1, 2: 4, 3: 7, 4: 4, 5: 4}


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If all stacks are sorted, return the actions taken
       if all(stack == sorted(stack, key=lambda x: {'Yellow': 0, 'Red': 1, 'Blue': 2, 'Green': 3}[x]) for stack in state if stack):
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from one stack to another
       for from_stack in range(num_stacks):
           for to_stack in range(num_stacks):
               # Check if transferring a block from the from_stack to the to_stack is valid
               if from_stack != to_stack and state[from_stack] and (not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]):
                   new_state = [list(stack[:]) for stack in state]
                   new_state[to_stack].append(new_state[from_stack].pop())
                   new_state = tuple(tuple(stack) for stack in new_state)
                   # Calculate the cost of the new state
                   new_cost = g + stack_costs[from_stack]
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None


print(a_star())
