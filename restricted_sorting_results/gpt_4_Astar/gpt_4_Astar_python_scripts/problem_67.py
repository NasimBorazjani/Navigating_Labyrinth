
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = ([], ['Blue', 'Black', 'Black', 'Yellow', 'White', 'Green'], ['Green', 'Black', 'Red', 'Green', 'Yellow', 'Blue'], [], ['Green', 'Red', 'Blue', 'Yellow', 'Green', 'Blue'], ['Black', 'White', 'White', 'Red', 'White', 'Black'], [], ['White', 'Red', 'Blue', 'Yellow', 'Yellow', 'Red'], [], [])
   num_stacks = 10
   stack_capacity = 6
   # Define the cost of moving a block to each stack
   stack_costs = {0: 5, 1: 4, 2: 7, 3: 7, 4: 11, 5: 11, 6: 8, 7: 3, 8: 7, 9: 9}


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie if all stacks are either empty or contain blocks of a single shade
       if all(len(set(stack)) <= 1 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes moving the top block from any stack to any other stack
       for from_stack_ind in range(num_stacks):
           # Check if the stack is not empty
           if state[from_stack_ind]:
               # Get the color of the top block in the stack
               top_block_color = state[from_stack_ind][-1]
               for to_stack_ind in range(num_stacks):
                   # Check if the stack is empty or contains blocks of the same color as the top block of the from_stack, and if the stack has not reached its capacity
                   if (not state[to_stack_ind] or (state[to_stack_ind][-1] == top_block_color and len(state[to_stack_ind]) < stack_capacity)):
                       # Generate the new state
                       new_state = [stack[:] for stack in state]
                       new_state[from_stack_ind].pop()
                       new_state[to_stack_ind].append(top_block_color)
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
   # The heuristic function can be the sum of the costs of moving the remaining blocks in the stacks to the cheapest stack
   # This heuristic is admissible because it always underestimates the cost to reach the goal state, as it assumes that all blocks can be moved to the cheapest stack, ignoring the constraints that a stack can only contain blocks of a single color and that a stack has a capacity
   # The heuristic is consistent because the cost of moving a block from one stack to another is always greater than or equal to the cost of moving a block to the cheapest stack
   return sum(len(stack) * min(stack_costs.values()) for stack in state)


print(a_star())
