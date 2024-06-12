
import heapq


def initialize():
   # Define the initial state of the stacks, representing each stack as a list of shades, with an empty stack represented as an empty list
   initial_state = ([], [], ['Red', 'Yellow', 'Black', 'Yellow', 'Green'], ['Red', 'Red', 'Blue', 'Red', 'Black'], [], ['Black', 'Blue', 'Yellow', 'Blue', 'Black'], [], ['Green', 'Green', 'Yellow', 'Blue', 'Green'])
   num_stacks = 8
   stack_capacity = 5
   # Create a dictionary mapping the cost to transfer one block to the top of each stack
   transfer_costs = {0: 4, 1: 6, 2: 8, 3: 2, 4: 4, 5: 7, 6: 7, 7: 5}


   visited_costs = {}
   visited_costs[tuple(initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_stacks, stack_capacity, transfer_costs, visited_costs, queue
  
def a_star():
  
   initial_state, num_stacks, stack_capacity, transfer_costs, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If all stacks have exactly one shade, the blocks are sorted
       if all(len(stack) == 1 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring one block from a non-empty stack to an empty stack or to a stack that has only blocks of that shade
       for from_stack_ind in range(num_stacks):
           for to_stack_ind in range(num_stacks):
               # Check if the transfer is valid
               if state[from_stack_ind] and (not state[to_stack_ind] or state[to_stack_ind][-1] == state[from_stack_ind][-1]):
                   # Generate the new state
                   new_state = [stack[:] for stack in state]
                   new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                   new_state = tuple(tuple(stack) for stack in new_state)
                   # The additional cost of this state is the cost of transferring the block
                   new_cost = g + transfer_costs[to_stack_ind]
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The heuristic is the sum of the number of blocks in each stack that are not sorted
                       h = heuristic(new_state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state):
   # The heuristic is admissible and consistent, as it is the sum of the number of blocks in each stack that are not sorted
   # The heuristic is also non-decreasing along the path to the goal state
   return sum(len(stack) - 1 for stack in state if len(stack) > 1)


print(a_star())
