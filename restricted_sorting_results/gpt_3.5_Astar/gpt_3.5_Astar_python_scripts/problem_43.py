
import heapq


def a_star():
   # Define the initial state of the stacks, with the leftmost item being the shade of the topmost block in each stack
   initial_state = [['Green', 'Green', 'Red', 'Blue', 'Red'],
                    ['Black', 'Red', 'Black', 'Red', 'Green'],
                    ['Yellow', 'Green', 'Black', 'Black', 'Blue'],
                    [],
                    ['Blue', 'Yellow', 'Blue', 'Yellow', 'Yellow'],
                    [],
                    [],
                    []]
   num_stacks = 8
   stack_capacity = 5
   # Define the cost of moving one block to the top of each stack
   costs = {0: 5, 1: 2, 2: 8, 3: 7, 4: 5, 5: 6, 6: 1, 7: 1}


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If all stacks are sorted, return the actions taken
       if all(stack == sorted(stack, key=lambda x: {'Green': 0, 'Red': 1, 'Blue': 2, 'Black': 3, 'Yellow': 4}[x]) for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from the top of one stack to another
       for from_stack in range(num_stacks):
           for to_stack in range(num_stacks):
               # Check if transferring a block from the top of the from_stack to the to_stack is valid
               if state[from_stack] and (not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]) and len(state[to_stack]) < stack_capacity:
                   # Generate the new state
                   new_state = [list(stack[:]) for stack in state]
                   new_state[from_stack].pop()
                   new_state[to_stack].append(state[from_stack][-1])
                   new_state = tuple(tuple(stack) for stack in new_state)
                   # The cost of the new state is the cost of moving the block from the from_stack to the to_stack
                   new_cost = g + costs[from_stack]
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None


print(a_star())
