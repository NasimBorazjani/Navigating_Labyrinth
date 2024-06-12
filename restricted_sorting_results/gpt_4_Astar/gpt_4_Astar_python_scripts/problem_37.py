
import heapq


def a_star():
   # Define the initial state of the stacks as a tuple of tuples
   initial_state = ((), ('Blue', 'Black', 'Blue', 'Yellow', 'Red'), ('Red', 'Green', 'Black', 'Green', 'Black'), (), ('Red', 'Red', 'Green', 'Yellow', 'Yellow'), (), (), ('Blue', 'Yellow', 'Green', 'Black', 'Blue'))
   num_stacks = 8
   stack_capacity = 5
   # Define the cost of moving a block to each stack
   stack_costs = {0: 3, 1: 2, 2: 1, 3: 7, 4: 5, 5: 5, 6: 6, 7: 4}


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
                   if len(state[to_stack_ind]) < stack_capacity and (not state[to_stack_ind] or state[to_stack_ind][-1] == state[from_stack_ind][-1]):
                       # Generate the new state
                       new_state = list(list(stack) for stack in state)
                       block = new_state[from_stack_ind].pop()
                       new_state[to_stack_ind].append(block)
                       new_state = tuple(tuple(stack) for stack in new_state)
                       # The cost of the new state is the cost of moving a block to the to_stack
                       new_cost = g + stack_costs[to_stack_ind]


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is the sum of the costs of moving the top block of each stack to an empty stack or a stack with blocks of the same shade
                           h = heuristic(new_state, stack_costs)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, stack_costs):
   # The heuristic function can be the sum of the costs of moving the top block of each stack to an empty stack or a stack with blocks of the same shade
   # This heuristic is admissible because it presumes we can move the blocks directly to their goal position, thus reporting a lower cost estimate to reach the goal state
   # The heuristic is consistent because the cost of moving a block from one stack to another is always greater than or equal to the cost of moving the block to an empty stack or a stack with blocks of the same shade
   h = 0
   for from_stack_ind in range(len(state)):
       if state[from_stack_ind]:
           min_cost = float('inf')
           for to_stack_ind in range(len(state)):
               if len(state[to_stack_ind]) < 5 and (not state[to_stack_ind] or state[to_stack_ind][-1] == state[from_stack_ind][-1]):
                   min_cost = min(min_cost, stack_costs[to_stack_ind])
           h += min_cost
   return h


print(a_star())