
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = ([], ['Yellow', 'Red', 'Black', 'Yellow', 'Green'], [], [], ['Green', 'Red', 'Blue', 'Blue', 'Black'], ['Green', 'Blue', 'Yellow', 'Red', 'Yellow'], [], ['Blue', 'Green', 'Black', 'Red', 'Black'])
   # Define the costs of moving one block to the top of each stack
   costs = {0: 5, 1: 5, 2: 5, 3: 6, 4: 5, 5: 5, 6: 9, 7: 6}
   # Define the capacities of the stacks
   capacities = [5, 5, 5, 5, 5, 5, 5, 5]
   # Define the goal state, where each stack has 4 blocks of a single shade
   goal_state = (['Yellow', 'Yellow', 'Yellow', 'Yellow'], ['Red', 'Red', 'Red', 'Red'], ['Black', 'Black', 'Black', 'Black'], ['Green', 'Green', 'Green', 'Green'], ['Blue', 'Blue', 'Blue', 'Blue'])


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from a non-empty stack to an empty stack or a stack with only blocks of the same shade
       for from_stack_ind, from_stack in enumerate(state):
           if from_stack:
               for to_stack_ind, to_stack in enumerate(state):
                   if not to_stack or to_stack[-1] == from_stack[-1]:
                       # Check if the transfer would not exceed the capacity of the receiving stack
                       if len(to_stack) < capacities[to_stack_ind]:
                           # Generate the new state
                           new_state = [list(stack[:]) for stack in state]
                           new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                           new_state = tuple(tuple(stack) for stack in new_state)
                           # The cost so far is the number of actions taken, as the task is to minimize the cost of transferring blocks
                           new_cost = g + costs[from_stack_ind]


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               h = heuristic(state, goal_state, capacities)
                               heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, goal_state, capacities):
   # The heuristic function can be a simulation of moving blocks greedily, using the next most common shade of block repeatedly as long as the stack does not exceed its capacity
   # This heuristic is admissible because it is greedy, always opting for the action that moves the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is removed from a stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of blocks that can be added to the stack is by using the next most common shade of block, which is exactly the shade used to fill the stack in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Count the number of blocks of each shade in the current state
   shade_counts = {}
   for stack in state:
       for block in stack:
           if block not in shade_counts:
               shade_counts[block] = 0
           shade_counts[block] += 1
   # Sort the shades by the number of blocks of that shade in the current state
   shades = sorted(shade_counts.keys(), key=lambda shade: -shade_counts[shade])
   # Iterate through the stacks
   for stack_ind, stack in enumerate(state):
       # Fill the stack with the next most common shade of block as long as the stack does not exceed its capacity
       while len(stack) < capacities[stack_ind] and shades:
           shade = shades.pop(0)
           stack.append(shade)
           # Increment the estimated cost to the goal by 1 actions
           h += 1
   return h


print(a_star())
