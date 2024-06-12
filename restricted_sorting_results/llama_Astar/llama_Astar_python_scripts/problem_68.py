
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = (['Black', 'Black', 'White', 'Blue', 'Yellow', 'White'],
                   ['Black', 'Blue', 'Red', 'Blue', 'Red', 'Green'],
                   [],
                   ['Black', 'White', 'Red', 'Green', 'White', 'Blue'],
                   ['Yellow', 'Blue', 'Red', 'Green', 'Green', 'Yellow'],
                   [],
                   ['Green', 'Black', 'Red', 'White', 'Yellow', 'Yellow'],
                   [],
                   [],
                   [])
   # Define the cost of moving one block to the top of each stack
   cost_dict = {0: 9, 1: 11, 2: 2, 3: 10, 4: 8, 5: 6, 6: 4, 7: 4, 8: 7, 9: 3}
   # Define the number of stacks and the capacity of each stack
   num_stacks = 10
   capacity = 6


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the state is the goal state, return the actions taken
       if all(len(stack) == 5 and len(set(stack)) == 1 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from a stack to another stack
       for from_stack_ind, from_stack in enumerate(state):
           if from_stack:
               for to_stack_ind, to_stack in enumerate(state):
                   if to_stack_ind != from_stack_ind and len(to_stack) < capacity and (not to_stack or to_stack[-1] == from_stack[-1]):
                       # Generate the new state
                       new_state = [stack[:] for stack in state]
                       new_state[from_stack_ind].pop()
                       new_state[to_stack_ind].append(from_stack[-1])
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
   # This heuristic is admissible because it is greedy, always opting for the action that minimizes the cost, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is transferred to a more expensive stack, or equal or less by at most the cost of reaching the successor node, ie one action
   h = 0
   # Sort the stacks by the cost of moving a block to the top of each stack
   stacks = sorted(range(len(state)), key=lambda i: cost_dict[i])
   # Iterate through the stacks
   for i in range(len(state)):
       # If the stack is not empty
       if state[i]:
           # Find the most expensive stack that can accept the block
           for j in stacks:
               if len(state[j]) < capacity and (not state[j] or state[j][-1] == state[i][-1]):
                   # Increment the estimated cost to the goal by the cost of moving the block to the top of the stack
                   h += cost_dict[j]
                   break
   return h


print(a_star())
