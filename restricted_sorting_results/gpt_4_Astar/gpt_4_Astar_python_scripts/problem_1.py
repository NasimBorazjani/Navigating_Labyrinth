
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = ([], [], [], ['Blue', 'Yellow', 'Blue', 'Blue'], ['Red', 'Green', 'Yellow', 'Green'], ['Red', 'Red', 'Yellow', 'Green'])
   num_stacks = 6
   stack_capacity = 4
   # Define the cost of moving a block to each stack
   stack_costs = {0: 5, 1: 5, 2: 3, 3: 1, 4: 5, 5: 1}


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when all the blocks are sorted by shade, ie each stack is either empty or contains blocks of a single shade
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
                       new_state = [stack[:] for stack in state]
                       new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                       new_state = tuple(tuple(stack) for stack in new_state)
                       # The cost of the new state is the cost of moving a block to the to_stack
                       new_cost = g + stack_costs[to_stack_ind]


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is the sum of the costs of moving the top block of each stack to a stack that is either empty or contains blocks of the same shade
                           h = heuristic(new_state, stack_costs)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, stack_costs):
   # The heuristic is the sum of the costs of moving the top block of each stack to a stack that is either empty or contains blocks of the same shade
   # The heuristic is admissible because it presumes that we can move the top block of each stack to any other stack, even if the stack is full or contains blocks of a different shade, thus reporting a lower cost estimate to reach the goal state
   # The heuristic is consistent because the cost of moving a block from one stack to another is always greater than or equal to the cost of moving the block to the same stack in the heuristic
   h = 0
   for from_stack_ind in range(len(state)):
       if state[from_stack_ind]:
           # Find the stack with the lowest cost that is either empty or contains blocks of the same shade
           to_stack_costs = [stack_costs[to_stack_ind] for to_stack_ind in range(len(state)) if not state[to_stack_ind] or state[to_stack_ind][-1] == state[from_stack_ind][-1]]
           if to_stack_costs:
               h += min(to_stack_costs)
   return h


print(a_star())
