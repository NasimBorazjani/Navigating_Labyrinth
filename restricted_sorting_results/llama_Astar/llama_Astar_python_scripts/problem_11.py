
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = ([], ['Blue', 'Blue', 'Green', 'Red'], [], ['Green', 'Red', 'Yellow', 'Yellow'], [], ['Green', 'Red', 'Blue', 'Yellow'])
   # Define the cost of moving one block to the top of each stack
   cost_dict = {0: 3, 1: 5, 2: 1, 3: 6, 4: 7, 5: 4}
   # Define the goal state, where each stack has 3 blocks of a single shade
   goal_state = (['Blue', 'Blue', 'Blue'], ['Green', 'Green', 'Green'], ['Red', 'Red', 'Red'], ['Yellow', 'Yellow', 'Yellow'])


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from a non-empty stack to an empty stack or a stack with the same shade
       for from_stack_ind, from_stack in enumerate(state):
           if from_stack:
               for to_stack_ind, to_stack in enumerate(state):
                   if not to_stack or to_stack[-1] == from_stack[-1]:
                       # Check if the new state, with the block transfer, would be valid
                       if len(to_stack) < 3:
                           # Generate the new state
                           new_state = [list(stack[:]) for stack in state]
                           new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                           new_state = tuple(tuple(stack) for stack in new_state)
                           # The cost so far is the number of actions taken, as the task is to minimize the cost of the actions required to sort the blocks
                           new_cost = g + cost_dict[to_stack_ind]


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               h = heuristic(state, goal_state, cost_dict)
                               heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, goal_state, cost_dict):
   # The heuristic function can be a simulation of sorting the blocks greedily, using the next most common shade of block repeatedly as long as the stack does not exceed its capacity
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is removed from a stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of blocks that can be added to the stack is by using the most common shade of block, which is exactly the shade used to fill the stack in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Calculate the frequency of each shade of block in the current state
   shade_freq = {shade: sum(stack.count(shade) for stack in state) for shade in set(block for stack in state for block in stack)}
   # Sort the shades by frequency
   shades = sorted(shade_freq.keys(), key=lambda shade: -shade_freq[shade])
   # Iterate through the stacks
   for stack_ind, stack in enumerate(state):
       # Fill the stack with the next most common shade of block until it reaches its capacity
       while len(stack) < 3 and shades:
           shade = shades.pop(0)
           # Increment the estimated cost to the goal by the cost of moving a block to the top of the stack
           h += cost_dict[stack_ind]
   return h


print(a_star())
