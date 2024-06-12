
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = ([], [], ['Green', 'Red', 'White', 'Green', 'Black', 'White'], [], ['Red', 'Red', 'Yellow', 'White', 'Blue', 'Black'], ['Blue', 'Yellow', 'Red', 'Blue', 'Blue', 'Green'], [], [], ['Black', 'White', 'Black', 'White', 'Yellow', 'Blue'], ['Yellow', 'Black', 'Green', 'Red', 'Green', 'Yellow'])
   # Define the cost of moving one block to the top of each stack
   cost_dict = {0: 7, 1: 11, 2: 8, 3: 10, 4: 5, 5: 6, 6: 10, 7: 10, 8: 4, 9: 11}
   # Define the goal state, where each stack has 5 blocks of a single shade
   goal_state = (['Green', 'Green', 'Green', 'Green', 'Green'], ['Red', 'Red', 'Red', 'Red', 'Red'], ['White', 'White', 'White', 'White', 'White'], ['Black', 'Black', 'Black', 'Black', 'Black'], ['Blue', 'Blue', 'Blue', 'Blue', 'Blue'], ['Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow'])
   # Define the number of stacks
   num_stacks = 10


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from a stack to another stack
       for from_stack in range(num_stacks):
           for to_stack in range(num_stacks):
               # Check if the transfer is valid, ie if the from_stack is not empty and the to_stack is empty or has blocks of the same shade as the top block of the from_stack
               if state[from_stack] and (not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]):
                   # Generate the new state
                   new_state = [list(stack[:]) for stack in state]
                   new_state[to_stack].append(new_state[from_stack].pop())
                   new_state = tuple(tuple(stack) for stack in new_state)
                   # The cost so far is the number of transfers made, as the task is to minimize the cost of transfers
                   new_cost = g + cost_dict[from_stack]


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(state, goal_state, cost_dict)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None




def heuristic(state, goal_state, cost_dict):
   # The heuristic function can be a simulation of moving blocks greedily, using the next most expensive stack as the destination stack for each block
   # This heuristic is admissible because it is greedy, always opting for the action that minimizes the cost, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is moved to a more expensive stack, or equal or less by at most the cost of reaching the successor node, ie one action
   h = 0
   # Sort the stacks by decreasing cost
   stacks = sorted(range(len(state)), key=lambda i: cost_dict[i], reverse=True)
   # Iterate through the stacks
   for i in range(len(state)):
       # If the stack is not empty
       if state[i]:
           # Find the next most expensive stack with the same shade of block
           for j in stacks:
               if state[j] and state[j][-1] == state[i][-1]:
                   # Increment the estimated cost to the goal by the cost of moving the block to the next most expensive stack
                   h += cost_dict[j]
                   break
   return h


print(a_star())
