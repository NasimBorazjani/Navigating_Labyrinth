
import heapq


def initialize():
   # Define the initial state of the stacks as a tuple of tuples
   initial_state = ((), (), (), ('Blue', 'Yellow', 'Blue', 'Blue'), ('Red', 'Green', 'Yellow', 'Green'), ('Red', 'Red', 'Yellow', 'Green'))
   num_stacks = 6
   stack_capacity = 4
   # Define the cost of moving a block to each stack
   stack_costs = {0: 5, 1: 5, 2: 3, 3: 1, 4: 5, 5: 1}


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_stacks, stack_capacity, stack_costs, visited_costs, queue
  
def a_star():
  
   initial_state, num_stacks, stack_capacity, stack_costs, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If all stacks are either empty or contain blocks of a single shade, return the actions taken
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
                       new_state = list(list(stack) for stack in state)
                       new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                       new_state = tuple(tuple(stack) for stack in new_state)
                       # The cost of moving a block to a stack is the cost of the stack
                       new_cost = g + stack_costs[to_stack_ind]


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is the sum of the costs of moving a block to each stack, weighted by the number of blocks that need to be moved to each stack
                           h = heuristic(new_state, stack_costs)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, stack_costs):
   # The heuristic function can be the sum of the costs of moving a block to each stack, weighted by the number of blocks that need to be moved to each stack
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is moved to a stack with a higher cost, or equal or less by at most the cost of moving a block to the stack (equal to the cost of reaching the successor node, ie one action) as the maximum number of blocks that can be moved to a stack is the capacity of the stack, which is exactly the number of blocks moved to the stack in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to the cost of moving a block to the stack) + h(n’)
   h = 0
   # Count the number of blocks of each shade
   block_counts = {}
   for stack in state:
       for block in stack:
           if block not in block_counts:
               block_counts[block] = 0
           block_counts[block] += 1
   # For each shade, find the stack with the minimum cost that has blocks of that shade or is empty, and add the cost of moving a block to that stack, weighted by the number of blocks of that shade, to the heuristic
   for block, count in block_counts.items():
       min_cost_stack = min([i for i in range(len(state)) if not state[i] or state[i][-1] == block], key=lambda x: stack_costs[x])
       h += stack_costs[min_cost_stack] * count
   return h


print(a_star())
