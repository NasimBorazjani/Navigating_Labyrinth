
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = (['Black', 'Blue', 'Red', 'White', 'Red', 'Green'],
                   ['Red', 'Black', 'Red', 'Green', 'Blue', 'Black'],
                   ['Black', 'Yellow', 'Yellow', 'White', 'White', 'Yellow'],
                   [],
                   [],
                   ['White', 'Green', 'Green', 'Red', 'Green', 'Yellow'],
                   [],
                   ['Blue', 'Blue', 'Blue', 'Black', 'White', 'Yellow'],
                   [],
                   [])
   # Define the cost of moving one block to the top of each stack
   cost_dict = {0: 3, 1: 8, 2: 5, 3: 10, 4: 8, 5: 2, 6: 3, 7: 4, 8: 11, 9: 3}
   num_stacks = 10


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the state is the goal state, return the actions taken
       if all(len(stack) == 0 or len(set(stack)) == 1 for stack in state):
           return actions


       # Generate all possible actions from the current state
       for from_stack_ind, from_stack in enumerate(state):
           if from_stack:
               for to_stack_ind, to_stack in enumerate(state):
                   if not to_stack or to_stack[-1] == from_stack[-1]:
                       # Check if the new state is valid, ie the stacks do not exceed their capacity
                       if len(to_stack) < 6:
                           # Generate the new state
                           new_state = [stack[:] for stack in state]
                           new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                           new_state = tuple(new_state)
                           # The cost so far is the number of actions taken
                           new_cost = g + cost_dict[from_stack_ind]


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               h = heuristic(new_state)
                               heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state):
   # The heuristic function can be a simulation of moving blocks greedily, using the next most common shade of block to fill the empty stacks
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is moved to a stack that is not empty, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of blocks that can be added to a stack is by using the next most common shade of block, which is exactly the block used to fill the stack in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Count the number of blocks of each shade in the state
   shade_counts = {}
   for stack in state:
       for shade in stack:
           if shade in shade_counts:
               shade_counts[shade] += 1
           else:
               shade_counts[shade] = 1
   # Sort the shades by the number of blocks of that shade in the state
   shades = sorted(shade_counts.keys(), key=lambda shade: -shade_counts[shade])
   # Iterate through the stacks
   for stack_ind, stack in enumerate(state):
       # If the stack is not empty, fill it with the next most common shade of block
       if stack:
           while len(stack) < 6 and shades:
               shade = shades.pop(0)
               stack.append(shade)
               # Increment the estimated cost to the goal by 1 actions
               h += 1
   return h


print(a_star())
