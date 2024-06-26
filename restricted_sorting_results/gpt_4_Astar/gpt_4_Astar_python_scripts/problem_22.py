
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = ([], ['Blue', 'Yellow', 'Blue', 'Yellow'], [], [], ['Red', 'Blue', 'Yellow', 'Green'], ['Green', 'Green', 'Red', 'Red'])
   # Define the cost of moving a block to each stack
   stack_costs = {0: 1, 1: 4, 2: 2, 3: 7, 4: 6, 5: 6}
   num_stacks = 6
   stack_capacity = 4


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If all the stacks are either empty or contain blocks of a single shade, return the actions taken
       if all(len(set(stack)) <= 1 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes moving the top block from any stack to any other stack
       for from_stack_ind in range(num_stacks):
           # Check if the stack is not empty
           if state[from_stack_ind]:
               for to_stack_ind in range(num_stacks):
                   # Check if the stack is not full and if the stack is either empty or the top block is of the same shade as the block to be moved
                   if (len(state[to_stack_ind]) < stack_capacity and
                       (not state[to_stack_ind] or state[to_stack_ind][-1] == state[from_stack_ind][-1])):
                       # Generate the new state
                       new_state = [list(stack[:]) for stack in state]
                       block = new_state[from_stack_ind].pop()
                       new_state[to_stack_ind].append(block)
                       new_state = tuple(tuple(stack) for stack in new_state)
                       # The cost of the new state is the cost of moving a block to the to_stack
                       new_cost = g + stack_costs[to_stack_ind]


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is the sum of the costs of moving the remaining blocks to the stacks with the lowest cost
                           h = heuristic(new_state, stack_costs)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, stack_costs):
   # The heuristic function can be the sum of the costs of moving the remaining blocks to the stacks with the lowest cost
   # This heuristic is admissible because it always reports a lower estimate on the cost to reach the goal state, as it presumes we can move the blocks to the stacks with the lowest cost, even if the stack is full or contains blocks of a different shade
   # The heuristic is consistent because the cost of moving a block to a stack is always greater than or equal to the cost of moving a block to the stack with the lowest cost, which is the decrease in the heuristic value, if the block is moved to a stack with the lowest cost, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as there are no blocks left to move in the goal state
   h = 0
   for stack in state:
       h += len(stack) * min(stack_costs.values())
   return h


print(a_star())
