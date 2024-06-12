
import heapq


def a_star():
   # Define the initial state of the stacks, with each stack represented as a list of blocks
   initial_state = [[], ['Blue', 'Blue', 'Green', 'Red'], [], ['Green', 'Red', 'Yellow', 'Yellow'], [], ['Green', 'Red', 'Blue', 'Yellow']]
   num_stacks = 6
   stack_capacity = 4
   # Define the cost of moving a block to the top of each stack
   stack_costs = {0: 3, 1: 5, 2: 1, 3: 6, 4: 7, 5: 4}


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, where all stacks are sorted
       if all(stack == sorted(stack) for stack in state if stack):
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from one stack to another
       for from_stack in range(num_stacks):
           for to_stack in range(num_stacks):
               # Check if transferring a block from the 'from_stack' to the 'to_stack' is a valid action
               if from_stack != to_stack and state[from_stack] and (not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]):
                   new_state = [list(stack[:]) for stack in state]
                   block = new_state[from_stack].pop()
                   new_state[to_stack].append(block)
                   new_state = tuple(tuple(stack) for stack in new_state)
                   # Calculate the cost of the new state, which is the cost of moving the block from one stack to another
                   new_cost = g + stack_costs[to_stack]
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None


print(a_star())
