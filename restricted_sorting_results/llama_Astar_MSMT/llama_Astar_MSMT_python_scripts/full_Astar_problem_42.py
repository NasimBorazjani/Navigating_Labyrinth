
import heapq


def initialize():
   # Define the initial state of the stacks as a 2d tuple
   initial_state = (('Blue', 'Black', 'Yellow', 'Black', 'Red'),
                   ('Blue', 'Blue', 'Green', 'Black', 'Yellow'),
                   (),
                   ('Yellow', 'Red', 'Red', 'Green', 'Green'),
                   (),
                   (),
                   (),
                   ('Red', 'Blue', 'Black', 'Green', 'Yellow'))
   num_stacks = 8
   stack_capacity = 5
   costs = {0: 7, 1: 5, 2: 7, 3: 2, 4: 6, 5: 7, 6: 5, 7: 3}
   empty_stacks = [i for i in range(num_stacks) if initial_state[i] == ()]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_stacks, stack_capacity, costs, empty_stacks, visited_costs, queue
  
def a_star():
  
   initial_state, num_stacks, stack_capacity, costs, empty_stacks, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If all stacks are sorted, return the actions taken
       if all(len(stack) == 1 for stack in state if stack):
           return actions


       # Generate all possible actions from the current state, which includes transferring a block to another stack
       for from_stack_ind, from_stack in enumerate(state):
           if from_stack:
               top_block = from_stack[-1]
               for to_stack_ind, to_stack in enumerate(state):
                   if to_stack_ind != from_stack_ind and (not to_stack or top_block == to_stack[-1]):
                       # Check if the new state would be valid, ie transferring the block would not exceed the stack's capacity
                       if len(to_stack) < stack_capacity:
                           new_state = [list(stack[:]) for stack in state]
                           new_state[from_stack_ind].pop()
                           new_state[to_stack_ind].append(top_block)
                           new_state = tuple(tuple(stack) for stack in new_state)
                           # The additional cost of this state is the cost of transferring the block
                           new_cost = g + costs[from_stack_ind]
                          
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               # Relaxing the constraints on the stacks to calculate the heuristic
                               h = heuristic(new_state, empty_stacks)
                               heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, empty_stacks):
   # Relax the stacks constraints to compute an admissible and consistent heuristic
   # This heuristic considers the number of blocks that need to be moved to sort the stacks
   # The heuristic is admissible because it is always greater than or equal to the cost of reaching the goal state
   # The heuristic is consistent, ie non-decreasing along the path to the goal state
   # The cost of the goal state is 0, as all stacks are sorted


   h = 0
   for stack in state:
       if len(stack) > 1:
           h += len(stack) - 1
   return h


print(a_star())
