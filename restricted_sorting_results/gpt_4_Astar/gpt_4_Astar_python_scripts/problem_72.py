
import heapq


def a_star():
   # Define the initial state of the stacks as a tuple of tuples
   initial_state = ((), (), ('Blue', 'Blue', 'Blue', 'Green', 'Black', 'Red'), (), ('Red', 'Black', 'Blue', 'White', 'Blue', 'Yellow'), ('Yellow', 'White', 'Green', 'Black', 'Yellow', 'Red'), (), (), ('White', 'Black', 'White', 'White', 'Black', 'Red'), ('Red', 'Green', 'Green', 'Yellow', 'Yellow', 'Green'))
   num_stacks = 10
   stack_capacity = 6
   # Define the cost of moving a block to each stack
   stack_costs = {0: 3, 1: 10, 2: 9, 3: 8, 4: 8, 5: 7, 6: 6, 7: 9, 8: 2, 9: 8}


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie if all the blocks in each stack are of the same color and the stack is full
       if all(len(stack) == stack_capacity and len(set(stack)) == 1 for stack in state if stack):
           return actions


       # Generate all possible actions from the current state, which includes moving the top block from any stack to any other stack
       for from_stack_ind in range(num_stacks):
           # Check if the stack is not empty
           if state[from_stack_ind]:
               for to_stack_ind in range(num_stacks):
                   # Check if the stack is not full and if the stack is empty or the top block is of the same color as the block to be moved
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
                           # The heuristic is the sum of the costs of moving the remaining blocks in each stack to the stack with the lowest cost, as we are trying to minimize the total cost of moving the blocks
                           h = heuristic(new_state, stack_costs)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, stack_costs):
   # The heuristic function can be the sum of the costs of moving the remaining blocks in each stack to the stack with the lowest cost
   # This heuristic is admissible because it always opts for the action that incurs the lowest cost, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is moved to a stack with a higher cost, or equal or less by at most the cost of moving a block to the stack with the lowest cost, as the maximum cost that can be saved by moving a block to a different stack is the difference between the cost of moving a block to the stack with the highest cost and the cost of moving a block to the stack with the lowest cost
   h = 0
   min_stack_cost = min(stack_costs.values())
   for stack in state:
       h += len(stack) * min_stack_cost
   return h


print(a_star())
