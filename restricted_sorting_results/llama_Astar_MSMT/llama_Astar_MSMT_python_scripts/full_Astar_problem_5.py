
import heapq


def initialize():
   # Define the initial state of the stacks as a list of lists
   initial_state = [['Red', 'Green', 'Green', 'Yellow'], [], ['Blue', 'Blue', 'Green', 'Red'], [], ['Blue', 'Yellow', 'Red', 'Yellow'], []]
   num_stacks = 6
   stack_capacity = 4
   # The cost of moving one block to the top of each stack
   move_costs = {0: 4, 1: 1, 2: 7, 3: 3, 4: 2, 5: 2}


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_stacks, stack_capacity, move_costs, visited_costs, queue
  
def a_star():
  
   initial_state, num_stacks, stack_capacity, move_costs, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the state is the goal state, return the actions taken
       if all(len(stack) == 1 or len(stack) == stack_capacity for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from one stack to another
       for from_stack_ind in range(num_stacks):
           for to_stack_ind in range(num_stacks):
               # Check if the transfer is valid, ie if the from_stack is not empty and the to_stack is either empty or has only blocks of the same shade
               if state[from_stack_ind] and (not state[to_stack_ind] or state[to_stack_ind][-1] == state[from_stack_ind][-1]):
                   # Generate the new state
                   new_state = [stack[:] for stack in state]
                   new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                   new_state = [stack for stack in new_state if stack]
                   # The cost so far is the number of transfers made, as our objective is to minimize the number of transfers required to sort the blocks
                   new_cost = g + 1
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[tuple(tuple(stack) for stack in new_state)] = new_cost
                       h = heuristic(new_state, stack_capacity)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, stack_capacity):
   # The heuristic function can be a simulation of sorting the blocks greedily, using the next smallest shade block repeatedly as long as the stack does not overflow
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is removed from a stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of blocks that can be added to the stack is by using the smallest shade block that won't cause an overflow, which is exactly the block used to fill the stack in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the blocks in each stack by shade
   state = [sorted(stack, key=lambda block: ('Red', 'Green', 'Blue', 'Yellow').index(block)) for stack in state]
   # Iterate through the stacks
   for i in range(len(state)):
       stack = state[i]
       # Fill the stack with the next smallest shade block repeatedly as long as the stack does not overflow
       while len(stack) < stack_capacity:
           # Increment the estimated cost to the goal by 1 actions
           h += 1
   return h


print(a_star())
