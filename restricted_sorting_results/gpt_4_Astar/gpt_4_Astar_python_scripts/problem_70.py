
import heapq


def a_star():
   # Define the initial state of the stacks as a 2d tuple
   initial_state = (('Red', 'Green', 'Blue', 'Yellow', 'Yellow', 'Blue'),
                    (),
                    (),
                    (),
                    ('White', 'Black', 'White', 'Red', 'White', 'Blue'),
                    ('Black', 'Green', 'Red', 'Black', 'Green', 'Yellow'),
                    (),
                    ('Red', 'White', 'Yellow', 'Black', 'Green', 'White'),
                    (),
                    ('Blue', 'Blue', 'Black', 'Green', 'Red', 'Yellow'))
   num_stacks = 10
   stack_capacity = 6
   # Define the cost of moving a block to each stack
   stack_costs = {0: 11, 1: 5, 2: 9, 3: 5, 4: 2, 5: 2, 6: 6, 7: 6, 8: 6, 9: 2}


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
           # Check if the from_stack is not empty
           if state[from_stack_ind]:
               for to_stack_ind in range(num_stacks):
                   # Check if the to_stack is not full and if it is either empty or the top block is of the same shade as the block to be moved
                   if (len(state[to_stack_ind]) < stack_capacity and
                       (not state[to_stack_ind] or state[to_stack_ind][-1] == state[from_stack_ind][-1])):
                       # Generate the new state
                       new_state = [list(stack[:]) for stack in state]
                       new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                       new_state = tuple(tuple(stack) for stack in new_state)
                       # The cost of the new state is the cost of moving a block to the to_stack
                       new_cost = g + stack_costs[to_stack_ind]


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is the sum of the costs of moving the remaining blocks in the stacks to the cheapest stack
                           h = heuristic(new_state, stack_costs)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, stack_costs):
   # The heuristic function can be a simulation of moving all the remaining blocks to the cheapest stack
   # This heuristic is admissible because it is greedy, always opting for the action that costs the least, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is moved to a more expensive stack, or equal or less by at most the cost of moving a block to the cheapest stack (equal to the cost of reaching the successor node, ie one action) as the maximum cost of moving a block is by moving it to the cheapest stack, which is exactly the stack used to move the blocks in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to the cost of moving a block to the cheapest stack) + h(n’)
   h = 0
   # Get the cost of moving a block to the cheapest stack
   min_cost = min(stack_costs.values())
   # Add the cost of moving each remaining block to the cheapest stack to the estimate
   for stack in state:
       h += len(stack) * min_cost
   return h


print(a_star())
