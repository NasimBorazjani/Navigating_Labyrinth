
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = (['White', 'Green', 'Red', 'Blue', 'Red', 'Yellow'],
                   ['Black', 'Black', 'White', 'Blue', 'Green', 'Green'],
                   ['White', 'Blue', 'White', 'Yellow', 'Black', 'Green'],
                   [],
                   [],
                   [],
                   [],
                   [],
                   ['Green', 'Yellow', 'Red', 'White', 'Blue', 'Black'],
                   ['Yellow', 'Red', 'Blue', 'Red', 'Black', 'Yellow'],
                   [])
   # Define the cost of moving one block to the top of each stack
   cost_dict = {0: 8, 1: 8, 2: 10, 3: 6, 4: 8, 5: 4, 6: 3, 7: 7, 8: 11, 9: 9}
   # Define the number of stacks and the capacity of each stack
   num_stacks = 10
   capacity = 6


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the state is the goal state, return the actions taken
       if all(len(stack) == 0 or len(stack) == capacity for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from a non-empty stack to an empty stack or a stack with only blocks of the same shade
       for from_stack_ind, from_stack in enumerate(state):
           if from_stack:
               for to_stack_ind, to_stack in enumerate(state):
                   if not to_stack or to_stack[-1] == from_stack[-1]:
                       # Check if the new state is valid, ie the stacks do not exceed their capacity
                       if len(to_stack) < capacity:
                           # Generate the new state
                           new_state = [stack[:] for stack in state]
                           new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                           new_state = tuple(new_state)
                           # The cost so far is the number of actions taken, as the task is to minimize the cost of transferring blocks
                           new_cost = g + cost_dict[from_stack_ind]


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               h = heuristic(new_state, cost_dict)
                               heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, cost_dict):
   # The heuristic function can be a simulation of moving blocks greedily, using the next most expensive stack as the destination stack for each block
   # This heuristic is admissible because it is greedy, always opting for the action that minimizes the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is moved to a more expensive stack, or equal or less by at most the cost of reaching the successor node, ie one action
   h = 0
   # Sort the stacks by the cost of moving a block to the top of each stack
   stacks = sorted(range(len(state)), key=lambda i: cost_dict[i])
   # Iterate through the stacks
   for i in range(len(state)):
       # For each stack, move the blocks to the next most expensive stack
       for j in range(i + 1, len(state)):
           # Calculate the number of blocks that can be moved from the current stack to the next stack
           num_blocks = min(len(state[i]), capacity - len(state[j]))
           # Increment the estimated cost to the goal by the cost of moving the blocks
           h += num_blocks * cost_dict[stacks[j]]
   return h


print(a_star())
