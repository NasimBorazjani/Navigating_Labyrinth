
import heapq


def a_star():
   # Define the initial state of the stacks as a tuple of tuples
   initial_state = ((), ('Yellow', 'Blue', 'Blue', 'Yellow', 'Green'), ('Black', 'Red', 'Black', 'Green', 'Red'), ('Yellow', 'Yellow', 'Red', 'Black', 'Blue'), (), ('Blue', 'Red', 'Green', 'Green', 'Black'), (), ())
   num_stacks = 8
   stack_capacity = 5
   # Define the cost of moving a block to each stack
   stack_costs = {0: 6, 1: 3, 2: 5, 3: 2, 4: 8, 5: 3, 6: 8, 7: 5}


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state is when all stacks are either empty or contain blocks of a single shade
       if all(len(set(stack)) <= 1 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes moving the top block from any stack to any other stack
       for from_stack_ind in range(num_stacks):
           # Check if the stack is not empty
           if state[from_stack_ind]:
               for to_stack_ind in range(num_stacks):
                   # Check if the stack is not full and if the stack is either empty or contains blocks of the same shade as the block to be moved
                   if len(state[to_stack_ind]) < stack_capacity and (not state[to_stack_ind] or state[to_stack_ind][-1] == state[from_stack_ind][-1]):
                       # Generate the new state
                       new_state = list(list(stack) for stack in state)
                       block = new_state[from_stack_ind].pop()
                       new_state[to_stack_ind].append(block)
                       new_state = tuple(tuple(stack) for stack in new_state)
                       # The cost of the new state is the cost of moving a block to the to_stack
                       new_cost = g + stack_costs[to_stack_ind]


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(new_state)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the number of blocks in each stack that are not of the same shade as the top block
   # The heuristic relaxes the constraints that a block can only be moved to an empty stack or a stack with blocks of the same shade, and that a stack can only hold a certain number of blocks, and presumes we can move the blocks to any stack
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the cost of moving a block from one stack to another is always at least 1, which is exactly the decrease in the heuristic, if the block is moved to a stack with blocks of the same shade, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as all blocks in each stack are of the same shade in the goal state
   h = 0
   for stack in state:
       if stack:
           h += len([block for block in stack if block != stack[-1]])
   return h


print(a_star())
