
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = [['Pink', 'Red', 'Black', 'Green', 'Yellow', 'Yellow', 'Pink'],
                    [],
                    [],
                    ['Pink', 'White', 'Yellow', 'Blue', 'Green', 'Blue', 'Black'],
                    ['Black', 'Blue', 'Red', 'Pink', 'Yellow', 'Yellow', 'Blue'],
                    [],
                    ['White', 'Black', 'Yellow', 'Green', 'Red', 'Green', 'Green'],
                    [],
                    [],
                    ['Pink', 'Red', 'Black', 'White', 'White', 'Red', 'White'],
                    ['Blue', 'Green', 'Pink', 'Blue', 'White', 'Red', 'Black'],
                    []]
   num_stacks = 12
   stack_capacity = 7
   # Define the cost of moving a block to each stack
   stack_costs = {0: 8, 1: 5, 2: 4, 3: 12, 4: 9, 5: 9, 6: 3, 7: 2, 8: 11, 9: 9, 10: 3, 11: 2}


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
               # Get the color of the top block in the stack
               block_color = state[from_stack_ind][-1]
               for to_stack_ind in range(num_stacks):
                   # Check if the stack is not full and if the stack is either empty or contains blocks of the same color as the block to be moved
                   if len(state[to_stack_ind]) < stack_capacity and (not state[to_stack_ind] or state[to_stack_ind][-1] == block_color):
                       # Generate the new state
                       new_state = [stack[:] for stack in state]
                       new_state[from_stack_ind].pop()
                       new_state[to_stack_ind].append(block_color)
                       # The cost of the new state is the cost of moving a block to the stack
                       new_cost = g + stack_costs[to_stack_ind]


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is 0 as we do not have any information on the goal state, thus we cannot estimate the cost to reach the goal state
                           heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None


print(a_star())
