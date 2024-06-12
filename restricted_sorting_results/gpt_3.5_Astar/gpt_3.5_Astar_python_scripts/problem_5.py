
import heapq


def a_star():
   # Define the initial state of the stacks, with the colors represented as strings
   initial_state = [['Red', 'Green', 'Green', 'Yellow'], [], ['Blue', 'Blue', 'Green', 'Red'], [], ['Blue', 'Yellow', 'Red', 'Yellow'], []]
   num_stacks = 6
   stack_capacity = 4
   # Define the cost of moving a block to the top of each stack
   stack_costs = {0: 4, 1: 1, 2: 7, 3: 3, 4: 2, 5: 2}


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If all stacks are sorted, return the actions taken
       if all(stack == sorted(stack, key=lambda x: {'Red': 0, 'Green': 1, 'Blue': 2, 'Yellow': 3}[x]) for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from one stack to another
       for from_stack in range(num_stacks):
           for to_stack in range(num_stacks):
               # Check if transferring a block from the from_stack to the to_stack is valid
               if state[from_stack] and (not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]):
                   new_state = [list(stack[:]) for stack in state]
                   new_state[from_stack].pop()
                   new_state[to_stack].append(state[from_stack][-1])
                   new_state = tuple(tuple(stack) for stack in new_state)
                   # Calculate the cost of the new state
                   new_cost = g + stack_costs[from_stack]
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None


print(a_star())
