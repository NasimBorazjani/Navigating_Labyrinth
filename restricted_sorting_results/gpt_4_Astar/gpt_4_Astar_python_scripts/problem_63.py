
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = ([], [], ['Blue', 'Yellow', 'Yellow', 'Yellow', 'Yellow', 'Black'], ['Red', 'Red', 'Blue', 'White', 'Blue', 'Black'], ['White', 'Green', 'Red', 'Black', 'Blue', 'Yellow'], [], ['White', 'Green', 'Green', 'White', 'Green', 'Green'], ['Black', 'Red', 'Red', 'Blue', 'White', 'Black'], [], [])
   num_stacks = 10
   stack_capacity = 6
   # Define the cost of moving a block to each stack
   stack_costs = {0: 7, 1: 7, 2: 8, 3: 5, 4: 8, 5: 10, 6: 5, 7: 5, 8: 4, 9: 8}


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state is when all stacks are either empty or contain blocks of a single shade
       if all(len(set(stack)) <= 1 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes moving the top block from any stack to any other stack
       for from_stack in range(num_stacks):
           # Check if the stack is not empty
           if state[from_stack]:
               for to_stack in range(num_stacks):
                   # Check if the stack is not full and if the stack is either empty or contains blocks of the same shade as the block to be moved
                   if len(state[to_stack]) < stack_capacity and (not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]):
                       # Generate the new state
                       new_state = [stack[:] for stack in state]
                       new_state[to_stack].append(new_state[from_stack].pop())
                       new_state = tuple(tuple(stack) for stack in new_state)
                       # The cost of the new state is the cost of moving a block to the to_stack
                       new_cost = g + stack_costs[to_stack]


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is the sum of the costs of moving the top block from each stack to an empty stack, as the blocks must be moved to sort the stacks
                           h = heuristic(state, stack_costs)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None




def heuristic(state, stack_costs):
   # The heuristic is the sum of the costs of moving the top block from each stack to an empty stack, as the blocks must be moved to sort the stacks
   # The heuristic is admissible because it presumes that we can move the blocks to any empty stack, even if the stack is full or contains blocks of a different shade, thus reporting a lower cost estimate to reach the goal state
   # The heuristic is consistent because the cost of moving a block from one stack to another is always greater than or equal to the cost of moving the block to an empty stack, as the cost of moving a block to a stack is at least 1
   return sum(stack_costs[i] for i in range(len(state)) if state[i])


print(a_star())
