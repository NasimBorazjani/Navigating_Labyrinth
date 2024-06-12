
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = (['Red', 'Green', 'Blue', 'Yellow', 'Yellow', 'Blue'], [], [], [], ['White', 'Black', 'White', 'Red', 'White', 'Blue'], ['Black', 'Green', 'Red', 'Black', 'Green', 'Yellow'], [], ['Red', 'White', 'Yellow', 'Black', 'Green', 'White'], [], ['Blue', 'Blue', 'Black', 'Green', 'Red', 'Yellow'])
   # Define the cost of moving one block to the top of each stack
   cost_dict = {0: 11, 1: 5, 2: 9, 3: 5, 4: 2, 5: 2, 6: 6, 7: 6, 8: 6, 9: 2}
   # Define the goal state, where each stack has 5 blocks of a single shade
   goal_state = (['Blue', 'Blue', 'Blue', 'Blue', 'Blue'], ['Green', 'Green', 'Green', 'Green', 'Green'], ['Red', 'Red', 'Red', 'Red', 'Red'], ['White', 'White', 'White', 'White', 'White'], ['Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow'])
   num_stacks = 10


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from a non-empty stack to an empty stack or a stack with the same shade
       for from_stack in range(num_stacks):
           if state[from_stack]:
               for to_stack in range(num_stacks):
                   # Check if the transfer is valid, ie if the to_stack is empty or has the same shade as the top block of the from_stack
                   if not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]:
                       # Generate the new state
                       new_state = [list(stack[:]) for stack in state]
                       new_state[to_stack].append(new_state[from_stack].pop())
                       new_state = tuple(tuple(stack) for stack in new_state)
                       # The cost so far is the number of actions taken, as the task is to minimize the cost of the actions required to sort the blocks
                       new_cost = g + cost_dict[to_stack]


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(state, goal_state, cost_dict)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None




def heuristic(state, goal_state, cost_dict):
   # The heuristic function can be a simulation of sorting the blocks greedily, using the next most common shade repeatedly as long as the stack does not exceed its capacity
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is removed from a stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of blocks that can be added to the stack is by using the next most common shade, which is exactly the shade used to fill the stack in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Count the number of blocks of each shade in the current state
   shade_counts = {}
   for stack in state:
       for block in stack:
           if block in shade_counts:
               shade_counts[block] += 1
           else:
               shade_counts[block] = 1
   # Sort the shades by the number of blocks in the current state
   shades = sorted(shade_counts.keys(), key=lambda shade: -shade_counts[shade])
   # Iterate through the stacks
   for stack in state:
       # Fill the stack with the next most common shade as long as the stack does not exceed its capacity
       while len(stack) < 5 and shades:
           shade = shades.pop(0)
           stack.append(shade)
           # Increment the estimated cost to the goal by the cost of moving a block to the stack
           h += cost_dict[state.index(stack)]
   return h


print(a_star())
