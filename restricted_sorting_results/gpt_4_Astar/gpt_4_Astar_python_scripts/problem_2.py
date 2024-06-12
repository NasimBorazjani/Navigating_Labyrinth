
import heapq


def a_star():
   # Define the initial state of the stacks as a tuple of tuples
   initial_state = (('Red', 'Green', 'Red', 'Blue'), ('Red', 'Yellow', 'Yellow', 'Green'), (), ('Blue', 'Yellow', 'Green', 'Blue'), (), ())
   num_stacks = 6
   stack_capacity = 4
   # Define the cost of moving a block to each stack
   stack_costs = {0: 5, 1: 3, 2: 3, 3: 1, 4: 3, 5: 2}


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
                   # Check if the stack is not full and if the stack is either empty or contains blocks of the same shade as the block to be moved
                   if (len(state[to_stack_ind]) < stack_capacity and
                       (not state[to_stack_ind] or state[to_stack_ind][0] == state[from_stack_ind][0])):
                       # Generate the new state
                       new_state = list(list(stack) for stack in state)
                       block = new_state[from_stack_ind].pop(0)
                       new_state[to_stack_ind].insert(0, block)
                       new_state = tuple(tuple(stack) for stack in new_state)
                       # The cost of the new state is the cost of moving a block to the stack
                       new_cost = g + stack_costs[to_stack_ind]


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is the sum of the costs of moving the top block from each stack to a stack that is either empty or contains blocks of the same shade as the block to be moved
                           h = heuristic(new_state, stack_costs)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, stack_costs):
   # The heuristic function can be the sum of the costs of moving the top block from each stack to a stack that is either empty or contains blocks of the same shade as the block to be moved
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is moved to a stack with a higher cost, or equal or less by at most the cost of moving a block to the stack (equal to the cost of reaching the successor node, ie one action) as the maximum amount of blocks that can be sorted is by moving the block to a stack that is either empty or contains blocks of the same shade as the block to be moved, which is exactly the action taken in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to the cost of moving a block to the stack) + h(n’)
   h = 0
   for stack in state:
       if stack:
           # Get the cost of moving the block to the cheapest stack that is either empty or contains blocks of the same shade as the block to be moved
           h += min(stack_costs[i] for i in range(len(state)) if not state[i] or state[i][0] == stack[0])
   return h


print(a_star())
