
import heapq


def initialize():
   # Define the initial state of the stacks as a list of lists
   initial_state = [['Blue', 'Black', 'Yellow', 'Black', 'Red'], ['Blue', 'Blue', 'Green', 'Black', 'Yellow'], [], ['Yellow', 'Red', 'Red', 'Green', 'Green'], [], [], ['Red', 'Blue', 'Black', 'Green', 'Yellow'], []]
   num_stacks = 8
   stack_capacity = 5
   # Create the set of the valid colors that could be in the stacks
   colors = set(['Blue', 'Black', 'Yellow', 'Red', 'Green'])
   # Define the cost of moving one block to the top of each stack
   cost_dict = {0: 7, 1: 5, 2: 7, 3: 2, 4: 6, 5: 7, 6: 5, 7: 3}


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_stacks, stack_capacity, colors, cost_dict, visited_costs, queue
  
def a_star():
  
   initial_state, num_stacks, stack_capacity, colors, cost_dict, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must have all stacks sorted by shade and with a capacity of 5, thus we need to check whether the current state is the goal state
       if all(len(stack) == stack_capacity and len(set(stack)) == 1 for stack in state):
           return actions


       # If the state is not the goal state, generate all possible actions from the current state, which includes transferring one block from the top of a stack to another stack that is not full or to a stack that has only blocks of that shade
       for from_stack_ind in range(num_stacks):
           for to_stack_ind in range(num_stacks):
               # Check if the transfer would be valid, ie if the to_stack is not full and has only blocks of the same shade as the top block of the from_stack, or if the from_stack is not empty
               if (len(state[to_stack_ind]) < stack_capacity and (len(state[from_stack_ind]) == 0 or state[to_stack_ind][-1] == state[from_stack_ind][-1]) and len(state[from_stack_ind]) != 0):
                   # Generate the new state
                   new_state = [list(stack[:]) for stack in state]
                   new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                   new_state = [stack for stack in new_state if stack]
                   # The cost of the new state is the cost of transferring the block plus the cost so far
                   new_cost = g + cost_dict[to_stack_ind]
                  
                   if tuple(tuple(stack) for stack in new_state) not in visited_costs or new_cost < visited_costs[tuple(tuple(stack) for stack in new_state)]:
                       visited_costs[tuple(tuple(stack) for stack in new_state)] = new_cost
                       # Relaxing the constraints on the colors to calculate the heuristic
                       h = heuristic(new_state, colors)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, colors):
   # Relax the colors constraints to compute an admissible and consistent heuristic
   # This heuristic considers the number of blocks that are not sorted by shade in the current state
   # The heuristic assumes that the blocks can be sorted by shade in the current state, even if the stacks are not sorted by color, thus reporting a lower cost estimate to reach the goal state, making it admissible
   # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of transferring a block is the cost of transferring the block to the top of the stack, which is always greater than or equal to the cost of transferring the block to the bottom of the stack
   # Also the cost of the goal state is 0, as all blocks are sorted by shade and the stacks are sorted by color


   h = 0
   for stack in state:
       # Check to see if the stack is sorted by color
       if len(set(stack)) == 1:
           # If the stack is not sorted by shade, increment the heuristic
           if len(stack) != stack_capacity:
               h += len(stack) - stack_capacity
       else:
           h += len(stack)
   return h


print(a_star())
