
import heapq


def a_star():
   # Define the initial state of the stacks as a tuple of tuples
   initial_state = (('Yellow', 'Yellow', 'Pink', 'Black', 'Green', 'Green', 'Yellow'),
                    ('Pink', 'Yellow', 'White', 'Red', 'Black', 'Blue', 'Blue'),
                    (),
                    (),
                    ('Pink', 'Green', 'Pink', 'Pink', 'Blue', 'Red', 'Red'),
                    ('Black', 'Black', 'Black', 'Blue', 'Yellow', 'Red', 'White'),
                    (),
                    (),
                    (),
                    (),
                    ('Green', 'Blue', 'Red', 'Red', 'Green', 'White', 'Black'),
                    ('White', 'White', 'Green', 'Yellow', 'Blue', 'White', 'Pink'))
   num_stacks = 12
   stack_capacity = 7
   # Define the cost of moving a block to each stack
   stack_costs = {0: 12, 1: 11, 2: 5, 3: 11, 4: 10, 5: 9, 6: 5, 7: 5, 8: 3, 9: 10, 10: 5, 11: 5}


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
           # Check if the stack is not empty
           if state[from_stack_ind]:
               for to_stack_ind in range(num_stacks):
                   # Check if the stack is not full and if the stack is either empty or the top block is of the same shade as the block to be moved
                   if (len(state[to_stack_ind]) < stack_capacity and
                       (not state[to_stack_ind] or state[to_stack_ind][-1] == state[from_stack_ind][-1])):
                       # Generate the new state
                       new_state = list(list(stack) for stack in state)
                       block = new_state[from_stack_ind].pop()
                       new_state[to_stack_ind].append(block)
                       new_state = tuple(tuple(stack) for stack in new_state)
                       # The cost of the new state is the cost of moving a block to the to_stack
                       new_cost = g + stack_costs[to_stack_ind]


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is 0 as we don't have any information about the goal state that can be used to estimate the remaining cost to reach the goal state
                           heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None


print(a_star())
