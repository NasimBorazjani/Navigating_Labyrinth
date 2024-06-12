
import heapq


def initialize():
   # Define the initial state of the stacks as a tuple of tuples
   initial_state = ((), ('Yellow', 'Green', 'Red', 'Red'), ('Blue', 'Green', 'Red', 'Green'), ('Yellow', 'Blue', 'Yellow', 'Blue'), (), ())
   num_stacks = 6
   stack_capacity = 4
   # Define the cost of moving a block to each stack
   stack_costs = {0: 3, 1: 6, 2: 5, 3: 6, 4: 1, 5: 1}


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_stacks, stack_capacity, stack_costs, visited_costs, queue
  
def a_star():
  
   initial_state, num_stacks, stack_capacity, stack_costs, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If all the stacks are empty or contain blocks of a single shade, return the actions taken
       if all(len(stack) == 0 or len(set(stack)) == 1 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes moving the top block from any stack to any other stack
       for from_stack_ind in range(num_stacks):
           # Check if the stack has any blocks to move
           if state[from_stack_ind]:
               for to_stack_ind in range(num_stacks):
                   # Check if the stack can accept more blocks and if the block can be moved to the stack
                   if (len(state[to_stack_ind]) < stack_capacity and
                       (not state[to_stack_ind] or state[to_stack_ind][-1] == state[from_stack_ind][-1])):
                       # Generate the new state
                       new_state = list(list(stack) for stack in state)
                       block = new_state[from_stack_ind].pop()
                       new_state[to_stack_ind].append(block)
                       new_state = tuple(tuple(stack) for stack in new_state)
                       # The cost of the new state is the cost of moving a block to the stack
                       new_cost = g + stack_costs[to_stack_ind]


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(new_state)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state):
   # The heuristic function can be the sum of the number of blocks in each stack that are not of the same shade as the top block
   # This heuristic is admissible because it presumes we can move the blocks to any stack, even if the stack is full or contains blocks of a different shade, thus reporting a lower cost estimate to reach the goal state
   # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of moving a block from one stack to another is always at least 1, which is exactly the decrease in the heuristic value, if the block is moved to a stack with blocks of the same shade, otherwise the heuristic value of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as all the blocks in each stack are of the same shade in the goal state
   h = 0
   for stack in state:
       if stack:
           h += len([block for block in stack if block != stack[-1]])
   return h


print(a_star())
