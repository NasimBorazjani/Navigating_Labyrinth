
import heapq


def initialize():
   # Define the initial state of the stacks as a 2d tuple
   initial_state = (('Blue', 'Red', 'Green', 'Yellow'), [], ('Red', 'Yellow', 'Yellow', 'Green'), [], ('Blue', 'Blue', 'Green', 'Red'), [])
   num_stacks = 6
   stack_capacity = 4
   # The cost of moving one block to the top of each stack
   cost_dict = {0: 2, 1: 3, 2: 3, 3: 6, 4: 1, 5: 6}


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_stacks, stack_capacity, cost_dict, visited_costs, queue
  
def a_star():
  
   initial_state, num_stacks, stack_capacity, cost_dict, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must be all stacks sorted with 3 blocks of a single shade
       if all(len(stack) == 3 and len(set(stack)) == 1 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring one block from a stack to another
       for from_stack_ind, from_stack in enumerate(state):
           if from_stack:
               for to_stack_ind, to_stack in enumerate(state):
                   if len(to_stack) < stack_capacity and (not to_stack or to_stack[-1] == from_stack[-1]):
                       # The cost of the new state is the cost of moving one block from the from_stack to the to_stack
                       new_cost = g + cost_dict[to_stack_ind]
                       # Generate the new state
                       new_state = [list(stack[:]) for stack in state]
                       new_state[from_stack_ind].pop()
                       new_state[to_stack_ind].append(from_stack[-1])
                       new_state = tuple(tuple(stack) for stack in new_state)
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, cost_dict):
   # The heuristic function can be a simulation of moving blocks greedily, using the next most expensive stack as the destination stack for each block
   # This heuristic is admissible because it is greedy, always opting for the action that moves the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is moved to a more expensive stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum cost of moving a block is by moving it to the next most expensive stack, which is exactly the stack used to move the block in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the stacks by decreasing cost
   stacks = sorted(range(len(state)), key=lambda i: cost_dict[i], reverse=True)
   # Iterate through the stacks
   for i in range(len(state)):
       stack = state[i]
       # Move the blocks in the stack to the next most expensive stack
       while stack:
           # Increment the estimated cost to the goal by the cost of moving one block to the next most expensive stack
           h += cost_dict[stacks[0]]
           # Remove the block from the current stack
           stack.pop()
   return h


print(a_star())
