
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = ([], ['Black', 'Green', 'White', 'Pink', 'Yellow', 'Blue', 'Red'], [], ['Green', 'Red', 'Red', 'Red', 'White', 'Black', 'Black'], [], ['Blue', 'Blue', 'Pink', 'Yellow', 'Pink', 'Green', 'Red'], ['Blue', 'Black', 'White', 'Green', 'White', 'Yellow', 'Yellow'], ['White', 'Blue', 'Pink', 'Green', 'Yellow', 'Green', 'Pink'], [], ['Yellow', 'Black', 'White', 'Red', 'Blue', 'Black', 'Pink'], [], [])
   # Define the cost of moving one block to the top of each stack
   cost_dict = {0: 10, 1: 8, 2: 12, 3: 3, 4: 5, 5: 11, 6: 5, 7: 12, 8: 3, 9: 3, 10: 11, 11: 6}
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
                   if to_stack_ind != from_stack_ind and (not to_stack or to_stack[-1] == from_stack[-1]) and len(to_stack) < capacity:
                       # Generate the new state
                       new_state = [stack[:] for stack in state]
                       new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                       new_state = tuple(tuple(stack) for stack in new_state)
                       # The cost so far is the number of actions taken, as the task is to minimize the cost of transferring blocks
                       new_cost = g + cost_dict[from_stack_ind]


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(new_state, cost_dict)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, cost_dict):
   # The heuristic function can be a simulation of moving blocks greedily, using the next most expensive stack as the destination stack for each block
   # This heuristic is admissible because it is greedy, always opting for the action that minimizes the cost, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is moved to a more expensive stack, or equal or less by at most the cost of reaching the successor node, ie one action
   h = 0
   # Sort the stacks by the cost of moving a block to the top of each stack
   stacks = sorted(range(len(state)), key=lambda i: cost_dict[i])
   # Iterate through the stacks
   for i in range(len(state)):
       # If the stack is not empty
       if state[i]:
           # Find the most expensive stack that can accept the block
           for j in stacks:
               if j != i and (not state[j] or state[j][-1] == state[i][-1]) and len(state[j]) < capacity:
                   # Increment the estimated cost to the goal by the cost of moving the block to the next most expensive stack
                   h += cost_dict[j]
                   break
   return h


print(a_star())
