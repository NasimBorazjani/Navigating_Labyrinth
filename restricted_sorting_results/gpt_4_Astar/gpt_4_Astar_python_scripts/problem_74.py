
import heapq


def a_star():
   # Define the initial state of the stacks as a tuple of tuples
   initial_state = (('Black', 'Blue', 'Red', 'White', 'Red', 'Green'),
                    ('Red', 'Black', 'Red', 'Green', 'Blue', 'Black'),
                    ('Black', 'Yellow', 'Yellow', 'White', 'White', 'Yellow'),
                    (),
                    (),
                    ('White', 'Green', 'Green', 'Red', 'Green', 'Yellow'),
                    (),
                    ('Blue', 'Blue', 'Blue', 'Black', 'White', 'Yellow'),
                    (),
                    ())
   num_stacks = 10
   stack_capacity = 6
   # Define the cost of moving a block to each stack
   stack_costs = {0: 3, 1: 8, 2: 5, 3: 10, 4: 8, 5: 2, 6: 3, 7: 4, 8: 11, 9: 3}


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
               for to_stack_ind in range(num_stacks):
                   # Check if the stack is not full and if the stack is either empty or contains blocks of the same shade as the block to be moved
                   if (len(state[to_stack_ind]) < stack_capacity and
                       (not state[to_stack_ind] or state[to_stack_ind][0] == state[from_stack_ind][0])):
                       # Generate the new state
                       new_state = list(list(stack) for stack in state)
                       block = new_state[from_stack_ind].pop(0)
                       new_state[to_stack_ind].insert(0, block)
                       new_state = tuple(tuple(stack) for stack in new_state)
                       # The cost of the new state is the cost of moving a block to the to_stack
                       new_cost = g + stack_costs[to_stack_ind]


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is 0 as we do not have any information on the goal state, thus we cannot estimate the cost to reach the goal state
                           heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None


print(a_star())
