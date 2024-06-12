
import heapq


def a_star():
   # Define the initial state of the stacks as a tuple of tuples
   initial_state = (('Red', 'Black', 'Yellow', 'Black', 'White', 'Blue', 'White'),
                    (),
                    ('White', 'Blue', 'Green', 'Yellow', 'Blue', 'Yellow', 'Pink'),
                    ('Yellow', 'Red', 'Pink', 'Green', 'Black', 'Red', 'White'),
                    (),
                    ('Pink', 'Red', 'Green', 'Green', 'Green', 'Black', 'Blue'),
                    ('Pink', 'Blue', 'Blue', 'Black', 'Red', 'Pink', 'Black'),
                    ('Yellow', 'Red', 'Pink', 'White', 'White', 'Yellow', 'Green'),
                    (),
                    (),
                    (),
                    ())
   num_stacks = 12
   stack_capacity = 7
   # Define the cost of moving a block to each stack
   stack_costs = {0: 7, 1: 13, 2: 10, 3: 12, 4: 4, 5: 13, 6: 2, 7: 11, 8: 11, 9: 10, 10: 8, 11: 9}


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
                   # Check if the stack is not full and if the stack is either empty or contains blocks of the same shade as the block to be moved
                   if (len(state[to_stack_ind]) < stack_capacity and
                       (not state[to_stack_ind] or state[to_stack_ind][-1] == state[from_stack_ind][-1])):
                       # Generate the new state
                       new_state = list(list(stack) for stack in state)
                       block = new_state[from_stack_ind].pop()
                       new_state[to_stack_ind].append(block)
                       new_state = tuple(tuple(stack) for stack in new_state)
                       # The cost of moving a block to a stack is given in the problem statement
                       new_cost = g + stack_costs[to_stack_ind]


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is 0 as we do not have any information on the goal state, other than that the blocks in each stack must be of the same shade
                           heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None


print(a_star())
