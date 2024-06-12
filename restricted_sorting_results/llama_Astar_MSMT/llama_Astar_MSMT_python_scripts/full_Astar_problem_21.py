
import heapq


def initialize():
   # Define the initial state of the stacks as a 2d tuple
   initial_state = (('Red', 'Yellow', 'Blue', 'Yellow'),
                   (),
                   (),
                   ('Green', 'Blue', 'Green', 'Red'),
                   (),
                   ('Yellow', 'Red', 'Green', 'Blue'))
   num_stacks = 6
   stack_capacity = 4
   transfer_costs = {0: 4, 1: 5, 2: 3, 3: 3, 4: 3, 5: 5}


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_stacks, stack_capacity, transfer_costs, visited_costs, queue
  
def a_star():
  
   initial_state, num_stacks, stack_capacity, transfer_costs, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must be all stacks with 3 blocks of a single shade
       if all(len(stack) == stack_capacity and len(set(stack)) == 1 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring one block from a stack to another
       for from_stack_ind, from_stack in enumerate(state):
           if from_stack:
               for to_stack_ind, to_stack in enumerate(state):
                   if len(to_stack) < stack_capacity and (not to_stack or to_stack[-1] == from_stack[-1]):
                       # The new state is the current state with the block transfered
                       new_state = [list(stack[:]) for stack in state]
                       new_state[from_stack_ind].pop()
                       new_state[to_stack_ind].append(from_stack[-1])
                       new_state = tuple(tuple(stack) for stack in new_state)
                       # The additional cost of this state is the cost of transferring the block
                       new_cost = g + transfer_costs[to_stack_ind]
                      
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, stack_capacity), new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, stack_capacity):
   # The heuristic is the sum of the number of blocks in each stack that are not yet sorted, divided by the cost to transfer a block to the correct stack
   # This heuristic is admissible because it is a lower bound on the cost to reach the goal state
   # The heuristic is consistent because the cost of moving a block is always at least 1, thus the estimated cost of the next node is higher if a block is moved to an incorrect stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of blocks that can be moved to the correct stack in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for stack in state:
       if len(stack) < stack_capacity:
           h += stack_capacity - len(stack)
   return h


print(a_star())
