
import heapq


def initialize():
   # Define the initial state of the stacks as a list of lists
   initial_state = [[], [], ['Green', 'Blue', 'Blue', 'Blue'], ['Yellow', 'Red', 'Yellow', 'Red'], ['Green', 'Red', 'Green', 'Yellow'], []]
   num_stacks = 6
   stack_capacity = 4
   # The cost of moving one block to the top of each stack
   move_costs = {0: 1, 1: 7, 2: 2, 3: 4, 4: 6, 5: 5}


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_stacks, stack_capacity, move_costs, visited_costs, queue
  
def a_star():
  
   initial_state, num_stacks, stack_capacity, move_costs, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the state is the goal state, return the actions taken
       if all(len(stack) == 0 or len(set(stack)) == 1 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from one stack to another
       for from_stack in range(num_stacks):
           for to_stack in range(num_stacks):
               # Check if the transfer is valid, ie if the from_stack is not empty and the to_stack is either empty or has only blocks of the same shade
               if state[from_stack] and (not state[to_stack] or set(state[from_stack]) == set(state[to_stack])):
                   # Perform the transfer
                   new_state = [stack[:] for stack in state]
                   new_state[to_stack].append(new_state[from_stack].pop())
                   # The cost of the new state is the cost of the transfer
                   new_cost = g + move_costs[to_stack]
                  
                   if new_state not in visited_costs or new_cost < visited_costs[tuple(tuple(stack) for stack in new_state)]:
                       visited_costs[tuple(tuple(stack) for stack in new_state)] = new_cost
                       # The heuristic is the sum of the costs of moving all blocks to their correct stacks
                       h = heuristic(new_state, move_costs)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None




def heuristic(state, move_costs):
   # The heuristic is the sum of the costs of moving all blocks to their correct stacks
   h = 0
   for from_stack in range(len(state)):
       for block in state[from_stack]:
           # The correct stack for the block is the one with only blocks of the same shade
           to_stack = next((i for i, stack in enumerate(state) if stack and set(stack) == set([block])), None)
           if to_stack is not None:
               h += move_costs[to_stack]
   return h


print(a_star())
