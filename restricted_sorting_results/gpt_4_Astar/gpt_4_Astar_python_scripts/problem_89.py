
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = ([], ['Blue', 'Yellow', 'Pink', 'Green', 'Pink', 'Red', 'Red'], [], ['Pink', 'White', 'Pink', 'Black', 'White', 'Black', 'Pink'], ['Yellow', 'Green', 'White', 'Red', 'Yellow', 'Yellow', 'Red'], ['Green', 'Pink', 'White', 'Blue', 'Red', 'White', 'Red'], [], [], ['Blue', 'Blue', 'Yellow', 'Blue', 'Black', 'Blue', 'Green'], ['Yellow', 'Black', 'Black', 'White', 'Green', 'Green', 'Black'], [], [])
   num_stacks = 12
   stack_capacity = 7
   # Define the cost of moving a block to each stack
   stack_costs = {0: 10, 1: 8, 2: 6, 3: 4, 4: 11, 5: 5, 6: 11, 7: 5, 8: 7, 9: 7, 10: 10, 11: 10}


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie if all the stacks are either empty or contain blocks of a single shade
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
                       new_state = [stack[:] for stack in state]
                       new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                       # The cost of the new state is the cost of moving a block to the to_stack
                       new_cost = g + stack_costs[to_stack_ind]


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is 0 as we don't have any information on the goal state, thus we can't estimate the cost to reach the goal state
                           heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None


print(a_star())
