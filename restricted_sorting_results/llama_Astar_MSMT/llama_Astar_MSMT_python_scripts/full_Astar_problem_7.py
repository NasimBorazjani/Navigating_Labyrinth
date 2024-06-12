
import heapq


def initialize():
   # Define the initial state of the stacks as a list of lists
   initial_state = [[], [], [], ['Yellow', 'Green', 'Blue', 'Blue'], ['Red', 'Blue', 'Green', 'Green'], ['Red', 'Red', 'Yellow', 'Yellow']]
   num_stacks = 6
   stack_capacity = 4
   # The cost of moving one block to the top of each stack
   cost_dict = {0: 5, 1: 3, 2: 5, 3: 6, 4: 5, 5: 7}


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_stacks, stack_capacity, cost_dict, visited_costs, queue
  
def a_star():
  
   initial_state, num_stacks, stack_capacity, cost_dict, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the state is the goal state, return the actions taken
       if all(len(stack) == 1 or len(stack) == 0 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from one stack to another
       for from_stack_ind in range(num_stacks):
           for to_stack_ind in range(num_stacks):
               # Check if the transfer is valid, ie if the from_stack is not empty and the to_stack is either empty or has blocks of the same shade
               if state[from_stack_ind] and (not state[to_stack_ind] or state[to_stack_ind][-1] == state[from_stack_ind][-1]):
                   # Generate the new state
                   new_state = [stack[:] for stack in state]
                   new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                   new_state = [stack[:] for stack in new_state]
                   # The cost so far is the number of transfers made, as our objective is to minimize the number of transfers required to sort the blocks
                   new_cost = g + cost_dict[to_stack_ind]
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[tuple(tuple(stack) for stack in new_state)] = new_cost
                       h = heuristic(new_state, cost_dict)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, cost_dict):
   # The heuristic function can be a simulation of sorting the blocks greedily, using the next most expensive stack as the destination for each block
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is transferred to a less expensive stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum cost of transferring a block to a more expensive stack is by using the most expensive stack that won't cause an overflow, which is exactly the stack used to transfer the block in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the stacks by decreasing cost
   stacks = sorted(range(len(state)), key=lambda i: cost_dict[i], reverse=True)
   # Iterate through the stacks
   for i in range(len(state)):
       # Sort the blocks in the stack
       state[i].sort()
       # Transfer the blocks to the next most expensive stack
       for block in state[i]:
           while state[stacks[0]] and state[stacks[0]][-1] != block:
               # Increment the estimated cost to the goal by 1 actions
               h += 1
   return h


print(a_star())
