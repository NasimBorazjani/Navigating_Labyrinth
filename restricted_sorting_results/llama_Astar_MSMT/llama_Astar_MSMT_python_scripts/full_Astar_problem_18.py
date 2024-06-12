
import heapq


def initialize():
   # Define the initial state of the stacks as a list of lists
   initial_state = [[], [], ['Blue', 'Green', 'Yellow', 'Green'], ['Red', 'Yellow', 'Yellow', 'Green'], [], ['Red', 'Blue', 'Red', 'Blue']]
   num_stacks = 6
   stack_capacity = 4
   # The cost of moving one block to the top of each stack
   cost_dict = {0: 7, 1: 6, 2: 2, 3: 7, 4: 7, 5: 4}


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_stacks, stack_capacity, cost_dict, visited_costs, queue
  
def a_star():
  
   initial_state, num_stacks, stack_capacity, cost_dict, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If all stacks are sorted, return the actions taken
       if all(len(stack) == 1 or len(stack) == stack_capacity and len(set(stack)) == 1 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring one block from a stack to another
       for from_stack_ind in range(num_stacks):
           for to_stack_ind in range(num_stacks):
               # Check if the transfer is valid, ie if the from_stack is not empty and the to_stack is either empty or has only blocks of the same shade
               if state[from_stack_ind] and (not state[to_stack_ind] or state[to_stack_ind][-1] == state[from_stack_ind][-1]) and len(state[to_stack_ind]) < stack_capacity:
                   # Generate the new state
                   new_state = [stack[:] for stack in state]
                   new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                   new_state = [stack for stack in new_state if stack]
                   # The cost so far is the number of transfers made, as our objective is to minimize the number of transfers required to sort the blocks
                   new_cost = g + cost_dict[to_stack_ind]
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[tuple(tuple(stack) for stack in new_state)] = new_cost
                       # The heuristic is the sum of the costs of moving all the blocks to their correct stacks
                       h = heuristic(new_state, cost_dict)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, cost_dict):
   # The heuristic is the sum of the costs of moving all the blocks to their correct stacks
   return sum(cost_dict[to_stack_ind] for from_stack_ind, to_stack_ind in enumerate(sorted([(stack[0], i) for i, stack in enumerate(state) if stack], key=lambda x: x[0])))


print(a_star())
