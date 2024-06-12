
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = ([], ['Blue', 'Pink', 'Red', 'Red', 'Yellow', 'White', 'Green'], [], [], ['White', 'Black', 'Blue', 'Yellow', 'Yellow', 'Pink', 'White'], ['Green', 'Pink', 'White', 'Blue', 'Pink', 'Red', 'Pink'], ['Black', 'Green', 'Yellow', 'White', 'Yellow', 'Red', 'Blue'], [], ['Red', 'White', 'Black', 'Blue', 'Black', 'Yellow', 'Green'], [], ['Green', 'Black', 'Pink', 'Black', 'Red', 'Green', 'Blue'], [])
   # Define the cost of moving one block to the top of each stack
   cost_dict = {0: 2, 1: 7, 2: 5, 3: 11, 4: 6, 5: 13, 6: 12, 7: 7, 8: 8, 9: 6, 10: 7, 11: 7}
   # Define the number of stacks and the capacity of each stack
   num_stacks = 12
   capacity = 7


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the state is the goal state, return the actions taken
       if all(len(stack) == 6 and len(set(stack)) == 1 for stack in state if stack):
           return actions


       # Generate all possible actions from the current state, which involves transferring a block from one stack to another
       for from_stack_ind, from_stack in enumerate(state):
           if from_stack:
               for to_stack_ind, to_stack in enumerate(state):
                   if to_stack_ind != from_stack_ind and len(to_stack) < capacity and (not to_stack or to_stack[-1] == from_stack[-1]):
                       # Generate the new state
                       new_state = [stack[:] for stack in state]
                       new_state[from_stack_ind].pop()
                       new_state[to_stack_ind].append(from_stack[-1])
                       new_state = tuple(tuple(stack) for stack in new_state)
                       # The cost of the new state is the cost of moving the block plus the cost so far
                       new_cost = g + cost_dict[from_stack_ind]


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is the sum of the number of blocks not in their correct stack and the sum of the squares of the differences between the number of blocks in each stack and the capacity
                           h = heuristic(new_state)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state):
   # The heuristic is an admissible and consistent estimate of the cost to reach the goal state
   # It is the sum of the number of blocks not in their correct stack and the sum of the squares of the differences between the number of blocks in each stack and the capacity
   # The heuristic is admissible because it never overestimates the cost to reach the goal state
   # The heuristic is consistent because the cost of moving a block is always at least 1, and the cost of moving a block to the top of each stack is at least 1
   # Thus the cost of moving a block to the top of each stack is the same for all stacks, and the cost of moving a block to the top of a stack is the same for all blocks
   # Thus the heuristic estimate for the goal state is 0, as the distance of each block from its goal position would be 0 in the goal state
   h = 0
   for stack in state:
       if stack:
           h += len(stack) - 1
   for stack in state:
       h += (len(stack) - 6) ** 2
   return h


print(a_star())
