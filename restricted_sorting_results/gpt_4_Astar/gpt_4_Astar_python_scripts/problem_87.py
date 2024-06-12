
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = [['Black', 'Blue', 'Pink', 'Green', 'Blue', 'Red', 'Red'],
                    ['Yellow', 'White', 'White', 'Black', 'Yellow', 'Green', 'Green'],
                    ['Yellow', 'Pink', 'White', 'Pink', 'Black', 'Red', 'Black'],
                    [],
                    ['Pink', 'Red', 'Blue', 'White', 'Blue', 'Blue', 'Red'],
                    ['Blue', 'Yellow', 'White', 'Pink', 'Pink', 'Green', 'Green'],
                    [],
                    [],
                    ['Yellow', 'Black', 'Yellow', 'White', 'Red', 'Black', 'Green'],
                    [],
                    [],
                    []]
   num_stacks = 12
   stack_capacity = 7
   # Define the cost of moving a block to each stack
   stack_costs = {0: 11, 1: 13, 2: 4, 3: 4, 4: 13, 5: 7, 6: 12, 7: 6, 8: 4, 9: 6, 10: 11, 11: 4}


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie if all stacks are either empty or contain blocks of a single shade
       if all(len(set(stack)) <= 1 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes moving a block from the top of any stack to the top of any other stack, provided the move is valid
       for from_stack_ind in range(num_stacks):
           # Can't move a block from an empty stack
           if state[from_stack_ind]:
               for to_stack_ind in range(num_stacks):
                   # Can't move a block to a stack that is already at capacity or to a stack that contains blocks of a different shade
                   if len(state[to_stack_ind]) < stack_capacity and (not state[to_stack_ind] or state[to_stack_ind][-1] == state[from_stack_ind][-1]):
                       # Generate the new state
                       new_state = [stack[:] for stack in state]
                       new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                       # The cost of the new state is the cost of moving a block to the to_stack
                       new_cost = g + stack_costs[to_stack_ind]


                       if tuple(tuple(stack) for stack in new_state) not in visited_costs or new_cost < visited_costs[tuple(tuple(stack) for stack in new_state)]:
                           visited_costs[tuple(tuple(stack) for stack in new_state)] = new_cost
                           # The heuristic is 0 as we don't have an admissible and consistent heuristic for this problem
                           heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None


print(a_star())
