
import heapq


def initialize():
   # Define the initial state of the stacks as a list of lists
   initial_state = [['Green', 'Green', 'Blue', 'Green'], [], ['Yellow', 'Red', 'Red', 'Blue'], [], [], ['Yellow', 'Yellow', 'Blue', 'Red']]
   num_stacks = 6
   stack_capacity = 4
   # Define the cost of moving one block to the top of each stack
   stack_costs = {0: 6, 1: 5, 2: 2, 3: 3, 4: 3, 5: 6}
   # Create the set of the valid colors that could be in the stacks
   colors = set(['Green', 'Blue', 'Red', 'Yellow'])


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_stacks, stack_capacity, stack_costs, colors, visited_costs, queue
  
def a_star():
  
   initial_state, num_stacks, stack_capacity, stack_costs, colors, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must be all stacks with 3 blocks of a single shade, and the remaining stacks must be empty
       if all(len(stack) == 3 and len(set(stack)) == 1 for stack in state if stack) and all(not stack for stack in state if len(stack) != 3):
           return actions


       # Generate all possible actions from the current state, which includes transferring one block from a stack to another
       for from_stack_ind in range(num_stacks):
           for to_stack_ind in range(num_stacks):
               # Check if the transfer is valid, ie the from_stack is not empty, the to_stack is not full, and the top block of the from_stack is not the same as the top block of the to_stack
               if state[from_stack_ind] and len(state[to_stack_ind]) < stack_capacity and (not state[to_stack_ind] or state[from_stack_ind][-1] != state[to_stack_ind][-1]):
                   # Generate the new state
                   new_state = [list(stack[:]) for stack in state]
                   new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                   new_state = [stack for stack in new_state if stack]
                   # The cost of the new state is the cost of the transfer plus the cost so far
                   new_cost = g + stack_costs[to_stack_ind]
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[tuple(tuple(stack) for stack in new_state)] = new_cost
                       # The heuristic is the sum of the costs of moving all remaining blocks to their correct stacks
                       h = heuristic(new_state, stack_costs)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, stack_costs):
   # The heuristic is the sum of the costs of moving all remaining blocks to their correct stacks
   # This heuristic is admissible because it is a lower bound on the cost to reach the goal state
   # The heuristic is consistent because the cost of moving a block is always at least 1, and the cost of moving a block to the top of each stack is always at least 1
   h = 0
   for from_stack_ind in range(len(state)):
       for block in state[from_stack_ind]:
           # The color of the block that needs to be moved
           color = block
           # Find the correct stack for the block
           to_stack_ind = next(i for i, stack in enumerate(state) if len(stack) == 3 and len(set(stack)) == 1 and stack[0] == color)
           h += stack_costs[to_stack_ind]
   return h


print(a_star())
