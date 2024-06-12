
import heapq


def initialize():
   # Define the initial state of the stacks as a list of lists
   initial_state = [[], [], ['Green', 'Blue', 'Green', 'Yellow'], [], ['Red', 'Red', 'Yellow', 'Blue'], ['Green', 'Red', 'Blue', 'Yellow']]
   num_stacks = 6
   stack_capacity = 4
   # Create the set of the valid block shades
   shades = set(['Green', 'Blue', 'Yellow', 'Red'])
   # Define the cost of moving one block to the top of each stack
   cost_dict = {0: 2, 1: 4, 2: 6, 3: 6, 4: 6, 5: 7}


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_stacks, stack_capacity, shades, cost_dict, visited_costs, queue
  
def a_star():
  
   initial_state, num_stacks, stack_capacity, shades, cost_dict, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must not have any blocks left in the stacks
       if not any(state):
           return actions


       # Generate all possible actions from the current state, which includes transferring one block from one stack to another
       for from_stack in range(num_stacks):
           for to_stack in range(num_stacks):
               # Check if the transfer is valid, ie if the from_stack is not empty and the to_stack is not full and has the same shade as the top block of the from_stack
               if state[from_stack] and len(state[to_stack]) < stack_capacity and (not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]):
                   # Generate the new state
                   new_state = [stack[:] for stack in state]
                   new_state[to_stack].append(new_state[from_stack].pop())
                   new_state = [stack[:] for stack in new_state]
                   # The cost of the new state is the cost of moving the block plus the cost so far
                   new_cost = g + cost_dict[to_stack]
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[tuple(tuple(stack) for stack in new_state)] = new_cost
                       # The heuristic is the sum of the number of blocks in each stack times the cost of moving the top block of that stack to the top of any other stack
                       h = sum(len(stack) * cost_dict[i] for i, stack in enumerate(new_state))
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None


print(a_star())
