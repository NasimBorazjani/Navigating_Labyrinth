
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = ([], ['Yellow', 'Green', 'Red', 'Red'], ['Blue', 'Green', 'Red', 'Green'], ['Yellow', 'Blue', 'Yellow', 'Blue'], [], [])
   # Define the cost of moving one block to the top of each stack
   stack_costs = {0: 3, 1: 6, 2: 5, 3: 6, 4: 1, 5: 1}
   # Define the goal state, where each stack has 3 blocks of a single shade
   goal_state = (['Red', 'Red', 'Red'], ['Green', 'Green', 'Green'], ['Blue', 'Blue', 'Blue'], ['Yellow', 'Yellow', 'Yellow'], [], [])
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


       # Generate all possible actions from the current state, which involves transferring a block from one stack to another
       for from_stack in range(num_stacks):
           for to_stack in range(num_stacks):
               # Check if the transfer is valid, ie if the from_stack is not empty and the to_stack is either empty or has blocks of the same shade as the top block of the from_stack
               if state[from_stack] and (not state[to_stack] or state[from_stack][-1] == state[to_stack][-1]):
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
   # The heuristic function can be a simulation of moving blocks greedily, using the next most expensive stack as the destination stack for each block
   # This heuristic is admissible because it is greedy, always opting for the action that moves the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is moved to a less expensive stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum cost of moving a block is by moving it to the most expensive stack, which is exactly the stack used to move the block in the heuristic
   h = 0
   # Sort the stacks by decreasing cost
   stacks = sorted(range(len(state)), key=lambda i: stack_costs[i], reverse=True)
   # Iterate through the stacks
   for i in range(len(state)):
       # For each stack, move the blocks to the next most expensive stack
       while state[i]:
           # Find the next most expensive stack that has the same shade of block as the top of the current stack
           for j in stacks:
               if not state[j] or state[j][-1] == state[i][-1]:
                   # Move the block to the next most expensive stack
                   state[j].append(state[i].pop())
                   # Increment the estimated cost to the goal by the cost of moving the block
                   h += stack_costs[i]
                   break
   return h


print(a_star())
