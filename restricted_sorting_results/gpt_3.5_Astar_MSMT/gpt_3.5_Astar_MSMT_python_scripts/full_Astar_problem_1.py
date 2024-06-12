
import heapq


def initialize():
   # Define the initial state of the stacks, with the leftmost item being the shade of the topmost block in each stack
   initial_state = [[], [], [], ['Blue', 'Yellow', 'Blue', 'Blue'], ['Red', 'Green', 'Yellow', 'Green'], ['Red', 'Red', 'Yellow', 'Green']]
   num_stacks = 6
   stack_capacity = 4
   # Define the cost of moving one block to the top of each stack
   move_costs = {0: 5, 1: 5, 2: 3, 3: 1, 4: 5, 5: 1}


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_stacks, stack_capacity, move_costs, visited_costs, queue
  
def a_star():
  
   initial_state, num_stacks, stack_capacity, move_costs, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Unpack the state to check if all stacks are sorted
       sorted_state = all(all(stack[i] == stack[0] for i in range(len(stack))) for stack in state if stack)
       if sorted_state:
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from one stack to another
       for from_stack in range(num_stacks):
           for to_stack in range(num_stacks):
               # Check if the transfer is valid, ie if the from_stack is not empty, the to_stack is either empty or has blocks of the same shade, and the transfer does not exceed the stack capacity
               if state[from_stack] and (not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]) and len(state[to_stack]) < stack_capacity:
                   # Generate the new state after the transfer
                   new_state = [list(stack[:]) for stack in state]
                   new_state[from_stack].pop()
                   new_state[to_stack].append(state[from_stack][-1])
                   new_state = tuple(tuple(stack) for stack in new_state)
                   # The cost of the new state is the cost of moving the block from one stack to another
                   new_cost = g + move_costs[from_stack]
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None


print(a_star())
