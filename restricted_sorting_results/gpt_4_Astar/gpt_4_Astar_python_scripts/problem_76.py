
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = (['Black', 'Blue', 'Green', 'Green', 'Pink', 'Black', 'Red'], [], ['Green', 'White', 'Yellow', 'Red', 'White', 'Blue', 'Pink'], [], [], ['Black', 'Green', 'Black', 'Yellow', 'Black', 'Blue', 'Black'], ['Green', 'Blue', 'Yellow', 'Yellow', 'Red', 'Yellow', 'Pink'], ['Red', 'White', 'Blue', 'Pink', 'Red', 'Blue', 'White'], [], [], ['Red', 'White', 'Pink', 'Green', 'Yellow', 'White', 'Pink'], [])
   num_stacks = 12
   stack_capacity = 7
   # Define the cost of moving a block to each stack
   stack_costs = {0: 7, 1: 9, 2: 13, 3: 3, 4: 4, 5: 4, 6: 6, 7: 11, 8: 12, 9: 3, 10: 13, 11: 5}


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


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
                   # Check if the stack is not full and if the stack is either empty or contains blocks of the same shade as the block to be moved
                   if len(state[to_stack_ind]) < stack_capacity and (not state[to_stack_ind] or state[to_stack_ind][-1] == state[from_stack_ind][-1]):
                       # Generate the new state
                       new_state = list(list(stack) for stack in state)
                       new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                       new_state = tuple(tuple(stack) for stack in new_state)
                       # The cost of moving a block is the cost of moving a block to the destination stack
                       new_cost = g + stack_costs[to_stack_ind]


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is 0 as we do not have any information on the goal state, thus we cannot estimate the cost to reach the goal state
                           heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None


print(a_star())
