
import heapq


def initialize():
   # Define the initial state of the stacks as a list of lists
   initial_state = [[], [], [], ['Red', 'Green', 'Green', 'Red'], ['Yellow', 'Blue', 'Yellow', 'Blue'], ['Yellow', 'Green', 'Red', 'Blue']]
   num_stacks = 6
   stack_capacity = 4
   # Define the cost of moving one block to the top of each stack
   cost_dict = {0: 4, 1: 5, 2: 5, 3: 2, 4: 5, 5: 2}


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_stacks, stack_capacity, cost_dict, visited_costs, queue
  
def a_star():
  
   initial_state, num_stacks, stack_capacity, cost_dict, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must have all stacks sorted, with each stack having 3 blocks of a single shade
       if all(len(stack) == 3 and len(set(stack)) == 1 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring one block from a stack to another
       for from_stack_ind in range(num_stacks):
           for to_stack_ind in range(num_stacks):
               # Check if the transfer is valid, ie if the from_stack is not empty and the to_stack is not full, and the shade of the top block in the from_stack is the same as the shade of the top block in the to_stack, or the to_stack is empty
               if state[from_stack_ind] and len(state[to_stack_ind]) < stack_capacity and (state[from_stack_ind][-1] == state[to_stack_ind][-1] or not state[to_stack_ind]):
                   # Perform the transfer
                   new_state = [stack[:] for stack in state]
                   new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                   # The cost of the new state is the cost of the transfer
                   new_cost = g + cost_dict[to_stack_ind]
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[tuple(tuple(stack) for stack in new_state)] = new_cost
                       # The heuristic is the sum of the number of blocks not sorted in each stack
                       h = heuristic(new_state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state):
   # The heuristic is the sum of the number of blocks not sorted in each stack
   return sum(len(stack) for stack in state if len(stack) != 3 or len(set(stack)) != 1)


print(a_star())
