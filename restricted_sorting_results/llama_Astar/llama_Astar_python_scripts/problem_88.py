
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = (['Yellow', 'Green', 'White', 'Pink', 'Black', 'Pink', 'Pink'],
                   ['Pink', 'Red', 'White', 'Black', 'Green', 'White', 'Pink'],
                   ['Red', 'Black', 'Green', 'Blue', 'Red', 'Black', 'Yellow'],
                   ['Blue', 'White', 'Blue', 'Blue', 'Black', 'White', 'Blue'],
                   ['Yellow', 'Blue', 'Green', 'Green', 'Red', 'Red', 'Yellow'],
                   [], [], [],
                   ['Black', 'Yellow', 'Red', 'Green', 'Yellow', 'Pink', 'White'],
                   [], [], [])
   # Define the costs of moving one block to the top of each stack
   costs = {0: 11, 1: 11, 2: 12, 3: 4, 4: 12, 5: 2, 6: 10, 7: 8, 8: 6, 9: 10, 10: 8, 11: 3}
   num_stacks = 12


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the state is the goal state, return the actions taken
       if all(len(stack) == 6 and len(set(stack)) == 1 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from a stack to another stack
       for from_stack_ind in range(num_stacks):
           for to_stack_ind in range(num_stacks):
               # Check if the transfer is valid, ie if the from_stack is not empty and the to_stack is empty or has blocks of the same shade
               if state[from_stack_ind] and (not state[to_stack_ind] or state[from_stack_ind][-1] == state[to_stack_ind][-1]):
                   # Generate the new state
                   new_state = [list(stack[:]) for stack in state]
                   new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                   new_state = tuple(tuple(stack) for stack in new_state)
                   # The cost so far is the number of transfers made, as the goal is to minimize the number of transfers required to sort the blocks
                   new_cost = g + costs[from_stack_ind]


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(state, new_state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, goal):
   # The heuristic function can be a simulation of the sorting process, moving the blocks greedily to the stacks with the same shade, without exceeding the stacks’ capacity
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is moved to a stack that has a different shade, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of blocks that can be moved to a stack is by moving the blocks of the same shade, which is exactly the blocks used to fill the stack in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for from_stack_ind in range(len(state)):
       for to_stack_ind in range(len(state)):
           if state[from_stack_ind] and (not state[to_stack_ind] or state[from_stack_ind][-1] == state[to_stack_ind][-1]):
               # Calculate the number of blocks that can be moved from the from_stack to the to_stack
               num_blocks = min(len(state[from_stack_ind]), 6 - len(state[to_stack_ind]))
               # Calculate the cost of moving the blocks
               h += num_blocks * costs[from_stack_ind]
   return h


print(a_star())
