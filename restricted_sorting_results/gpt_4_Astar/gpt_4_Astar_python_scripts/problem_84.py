
import heapq


def a_star():
   # Define the initial state of the stacks as a tuple of tuples
   initial_state = ((), (), (), (), ('Pink', 'Red', 'Green', 'Pink', 'White', 'Blue', 'Yellow'), (), ('Yellow', 'White', 'Yellow', 'Blue', 'Yellow', 'Black', 'White'), ('Black', 'Green', 'Pink', 'Pink', 'Green', 'Yellow', 'Green'), ('White', 'Blue', 'Red', 'Red', 'Red', 'Yellow', 'Black'), ('Black', 'Blue', 'Blue', 'Pink', 'Red', 'White', 'Green'), (), ('Blue', 'Black', 'Black', 'White', 'Red', 'Green', 'Pink'))
   num_stacks = 12
   stack_capacity = 7
   # Define the cost of moving a block to each stack
   stack_costs = {0: 12, 1: 3, 2: 11, 3: 5, 4: 11, 5: 13, 6: 2, 7: 2, 8: 12, 9: 4, 10: 2, 11: 10}


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
               from_stack_top_color = state[from_stack_ind][-1]
               for to_stack_ind in range(num_stacks):
                   # Check if the stack is not full and if the stack is either empty or the top block is the same color as the block to be moved
                   if len(state[to_stack_ind]) < stack_capacity and (not state[to_stack_ind] or state[to_stack_ind][-1] == from_stack_top_color):
                       # Generate the new state
                       new_state = list(list(stack) for stack in state)
                       new_state[from_stack_ind].pop()
                       new_state[to_stack_ind].append(from_stack_top_color)
                       new_state = tuple(tuple(stack) for stack in new_state)
                       # The cost of the new state is the cost of moving a block to the to_stack
                       new_cost = g + stack_costs[to_stack_ind]


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is 0 as we don't have any information about the goal state, other than the constraints on the blocks in each stack
                           heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None


print(a_star())
