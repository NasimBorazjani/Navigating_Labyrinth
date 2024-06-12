
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = ([], ['White', 'Black', 'Yellow', 'Black', 'Green', 'Blue', 'Pink'], ['Black', 'Red', 'Yellow', 'White', 'Yellow', 'Black', 'Green'], ['Yellow', 'White', 'Green', 'White', 'White', 'Black', 'Blue'], ['Blue', 'Pink', 'Red', 'Pink', 'Green', 'Yellow', 'Black'], ['White', 'Red', 'Pink', 'Blue', 'Blue', 'Pink', 'Green'], [], [], [], ['Red', 'Pink', 'Red', 'Blue', 'Red', 'Green', 'Yellow'], [], [])
   # Define the cost of moving one block to the top of each stack
   cost_dict = {0: 5, 1: 3, 2: 3, 3: 4, 4: 2, 5: 2, 6: 12, 7: 9, 8: 5, 9: 11, 10: 11, 11: 10}
   # Define the capacity of the stacks
   capacity = 7
   # Define the goal state, where each stack has 6 blocks of a single shade
   goal_state = ([], ['White', 'White', 'White', 'White', 'White', 'White', 'White'], ['Black', 'Black', 'Black', 'Black', 'Black', 'Black', 'Black'], ['Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow'], ['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'], ['Pink', 'Pink', 'Pink', 'Pink', 'Pink', 'Pink', 'Pink'], ['Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red'], ['Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green'], [], [], [])


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from a non-empty stack to an empty stack or a stack with the same shade
       for from_stack_ind, from_stack in enumerate(state):
           if from_stack:
               for to_stack_ind, to_stack in enumerate(state):
                   if not to_stack or to_stack[-1] == from_stack[-1]:
                       # Check if the new state would be valid, ie the stacks do not exceed their capacity
                       if len(to_stack) < capacity:
                           # Generate the new state
                           new_state = [list(stack[:]) for stack in state]
                           new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                           new_state = tuple(tuple(stack) for stack in new_state)
                           # The cost so far is the number of actions taken, as the task is to minimize the cost of the actions
                           new_cost = g + cost_dict[to_stack_ind]


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               h = heuristic(state, goal_state, cost_dict)
                               heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, goal_state, cost_dict):
   # The heuristic function can be a simulation of moving blocks greedily, using the next most expensive stack as the destination stack for each block
   # This heuristic is admissible because it is greedy, always opting for the action that minimizes the cost, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is moved to a more expensive stack, or equal or less by at most the cost of reaching the successor node, ie one action
   h = 0
   # Sort the stacks by the cost of moving a block to the top of each stack
   stacks = sorted(range(len(state)), key=lambda x: cost_dict[x])
   # Iterate through the stacks
   for i in range(len(state)):
       # For each stack, move the blocks to the next most expensive stack
       for block in state[stacks[i]]:
           # Find the next most expensive stack with the same shade as the block
           for j in range(i + 1, len(stacks)):
               if state[stacks[j]] and state[stacks[j]][-1] == block:
                   # Increment the estimated cost to the goal by the cost of moving the block
                   h += cost_dict[stacks[j]]
                   break
   return h


print(a_star())
