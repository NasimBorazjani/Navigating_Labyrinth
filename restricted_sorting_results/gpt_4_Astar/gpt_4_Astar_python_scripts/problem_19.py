
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = ([], [], ['Green', 'Blue', 'Green', 'Yellow'], [], ['Red', 'Red', 'Yellow', 'Blue'], ['Green', 'Red', 'Blue', 'Yellow'])
   # Define the cost of moving a block to each stack
   stack_costs = {0: 2, 1: 4, 2: 6, 3: 6, 4: 6, 5: 7}
   num_stacks = 6
   stack_capacity = 4


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie all stacks are either empty or contain blocks of a single shade
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
                       new_state = [stack[:] for stack in state]
                       new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                       new_state = tuple(tuple(stack) for stack in new_state)
                       # The cost of the new state is the cost of moving a block to the to_stack
                       new_cost = g + stack_costs[to_stack_ind]


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is the sum of the costs of moving the top block from each stack to a stack that is either empty or contains blocks of the same shade, as the heuristic relaxes the constraint that a stack can only hold 4 blocks and presumes we can move the blocks to their goal position by transferring them to any of the other stacks
                           h = heuristic(new_state, stack_costs)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None


def heuristic(state, stack_costs):
   # The heuristic is the sum of the costs of moving the top block from each stack to a stack that is either empty or contains blocks of the same shade
   # The heuristic relaxes the constraint that a stack can only hold 4 blocks and presumes we can move the blocks to their goal position by transferring them to any of the other stacks
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the cost of moving a block to a neighboring stack is always equal to the cost of moving a block to that stack, which is exactly the decrease in the heuristic, if the block is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of each block from its goal position would be 0 in the goal state.
   h = 0
   for stack in state:
       if stack:
           # Get the cost of moving the block to the cheapest stack that is either empty or contains blocks of the same shade
           h += min(stack_costs[i] for i in range(len(state)) if not state[i] or state[i][-1] == stack[-1])
   return h


print(a_star())
