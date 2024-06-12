
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = [['Green', 'Black', 'White', 'Red', 'White', 'Yellow', 'Blue'],
                    [],
                    ['White', 'Pink', 'White', 'White', 'Green', 'Red', 'Blue'],
                    [],
                    ['Pink', 'Black', 'Black', 'White', 'Black', 'Green', 'Blue'],
                    ['Pink', 'Green', 'Pink', 'Yellow', 'Yellow', 'Blue', 'Red'],
                    [],
                    ['Red', 'Yellow', 'Yellow', 'Yellow', 'Blue', 'Red', 'Black'],
                    [],
                    [],
                    [],
                    ['Red', 'Green', 'Black', 'Blue', 'Pink', 'Pink', 'Green']]
   num_stacks = 12
   stack_capacity = 7
   # Define the cost of moving a block to each stack
   stack_costs = {0: 13, 1: 5, 2: 8, 3: 11, 4: 6, 5: 9, 6: 5, 7: 11, 8: 2, 9: 11, 10: 11, 11: 7}


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie if all the stacks are either empty or contain blocks of a single shade
       if all(len(set(stack)) <= 1 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes moving the top block from each stack to any other stack
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
                       # The cost of the new state is the cost of moving a block to the destination stack
                       new_cost = g + stack_costs[to_stack_ind]


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is the sum of the costs of moving the top block from each stack to an empty stack or a stack with blocks of the same color
                           h = heuristic(new_state, stack_costs)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, stack_costs):
   # The heuristic is the sum of the costs of moving the top block from each stack to an empty stack or a stack with blocks of the same color
   # The heuristic is admissible because it assumes that we can move the top block from each stack to any other stack, even if the stack is full or contains blocks of a different color, thus reporting a lower cost estimate to reach the goal state
   # The heuristic is consistent because the cost of moving a block from one stack to another is always greater than or equal to the cost of moving the block to an empty stack or a stack with blocks of the same color
   h = 0
   for from_stack_ind in range(len(state)):
       if state[from_stack_ind]:
           block_color = state[from_stack_ind][-1]
           # Get the costs of moving the block to each stack
           to_stack_costs = [stack_costs[to_stack_ind] for to_stack_ind in range(len(state)) if len(state[to_stack_ind]) < 7 and (not state[to_stack_ind] or state[to_stack_ind][-1] == block_color)]
           # Add the minimum cost to the heuristic
           if to_stack_costs:
               h += min(to_stack_costs)
   return h


print(a_star())
