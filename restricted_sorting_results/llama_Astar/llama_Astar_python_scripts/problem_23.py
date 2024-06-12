
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = (['Green', 'Green', 'Blue', 'Red'],
                   ['Blue', 'Red', 'Yellow', 'Blue'],
                   [],
                   ['Green', 'Yellow', 'Red', 'Yellow'],
                   [],
                   [])
   # Define the cost of moving one block to the top of each stack
   stack_costs = {0: 2, 1: 7, 2: 4, 3: 7, 4: 6, 5: 3}
   # Define the goal state, where each stack has 3 blocks of a single shade
   goal_state = (['Green', 'Green', 'Green'],
                 ['Blue', 'Blue', 'Blue'],
                 ['Red', 'Red', 'Red'],
                 ['Yellow', 'Yellow', 'Yellow'])
   # Define the number of stacks
   num_stacks = 6


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from a non-empty stack to an empty stack or a stack with the same shade
       for from_stack in range(num_stacks):
           for to_stack in range(num_stacks):
               # Check if the transfer is valid
               if state[from_stack] and (not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]):
                   # Generate the new state
                   new_state = [list(stack[:]) for stack in state]
                   new_state[to_stack].append(new_state[from_stack].pop())
                   new_state = tuple(tuple(stack) for stack in new_state)
                   # The cost so far is the number of actions taken, as the task is to minimize the cost of transferring blocks
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(state, goal_state, stack_costs)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None




def heuristic(state, goal_state, stack_costs):
   # The heuristic function can be a simulation of transferring blocks greedily, using the least expensive stack as the target for each block
   # This heuristic is admissible because it is greedy, always opting for the action that transfers the blocks to the least expensive stack, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is transferred to a more expensive stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum cost of transferring a block is by using the least expensive stack that won't cause an overflow, which is exactly the stack used to transfer the block in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the stacks by increasing cost
   stacks = sorted(range(len(state)), key=stack_costs.get)
   # Iterate through the stacks
   for i in range(len(state)):
       # For each stack, greedily transfer the blocks to the least expensive stack
       while state[i]:
           # Find the least expensive stack that can accept the block
           for j in stacks:
               if not state[j] or state[j][-1] == state[i][-1]:
                   # Transfer the block to the least expensive stack
                   state[j].append(state[i].pop())
                   # Increment the estimated cost to the goal by the cost of the transfer
                   h += stack_costs[i]
                   break
   return h


print(a_star())
