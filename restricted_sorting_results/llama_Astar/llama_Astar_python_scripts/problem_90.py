
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = (['Pink', 'Black', 'Red', 'White', 'White', 'Black', 'Pink'], [], [], ['Green', 'Green', 'Blue', 'White', 'Pink', 'Pink', 'White'], [], ['Blue', 'Yellow', 'Yellow', 'Black', 'White', 'Green', 'Red'], ['Blue', 'Yellow', 'Blue', 'White', 'Green', 'Red', 'Pink'], ['Pink', 'Yellow', 'Yellow', 'Green', 'Green', 'Black', 'Blue'], [], ['Blue', 'Red', 'Red', 'Black', 'Black', 'Red', 'Yellow'], [], [])
   # Define the cost of moving one block to the top of each stack
   cost_dict = {0: 2, 1: 7, 2: 2, 3: 2, 4: 4, 5: 13, 6: 4, 7: 6, 8: 8, 9: 6, 10: 10, 11: 10}
   # Define the number of stacks and the capacity of each stack
   num_stacks = 12
   capacity = 7


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the state is the goal state, return the actions taken
       if all(len(stack) == 0 or len(set(stack)) == 1 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from a stack to another stack
       for from_stack_ind in range(num_stacks):
           for to_stack_ind in range(num_stacks):
               # Check if the transfer is valid, ie if the from_stack is not empty and the to_stack is empty or has only blocks of the same shade as the top block of the from_stack
               if state[from_stack_ind] and (not state[to_stack_ind] or state[to_stack_ind][-1] == state[from_stack_ind][-1]) and len(state[to_stack_ind]) < capacity:
                   # Generate the new state
                   new_state = [list(stack[:]) for stack in state]
                   new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                   new_state = tuple(tuple(stack) for stack in new_state)
                   # The cost so far is the number of transfers made, as the goal is to minimize the number of transfers required to sort the blocks
                   new_cost = g + cost_dict[from_stack_ind]


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(state, cost_dict)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, cost_dict):
   # The heuristic function can be a simulation of sorting the blocks greedily, using the next most common shade of block as the shade to fill the stacks with, starting from the stack with the most blocks of that shade
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is removed from a stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of blocks that can be added to the stack is by using the most common shade of block in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Count the number of blocks of each shade in each stack
   shade_counts = {shade: sum(stack.count(shade) for stack in state) for shade in set(block for stack in state for block in stack)}
   # Sort the shades by the number of blocks in the stacks, in descending order
   shades = sorted(shade_counts, key=shade_counts.get, reverse=True)
   # Iterate through the stacks
   for stack_ind in range(len(state)):
       # Fill the stack with the next most common shade of block as long as the stack does not overflow
       for shade in shades:
           while len(state[stack_ind]) < capacity and state[stack_ind].count(shade) < shade_counts[shade]:
               # Increment the estimated cost to the goal by 1 actions
               h += cost_dict[stack_ind]
   return h


print(a_star())
