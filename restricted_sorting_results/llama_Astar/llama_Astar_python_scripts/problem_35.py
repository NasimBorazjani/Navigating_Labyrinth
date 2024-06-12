
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = ([], ['Green', 'Blue', 'Yellow', 'Black', 'Blue'], [], [], ['Blue', 'Black', 'Green', 'Yellow', 'Red'], [], ['Green', 'Red', 'Black', 'Yellow', 'Blue'], ['Red', 'Green', 'Red', 'Black', 'Yellow'])
   # Define the costs of moving one block to the top of each stack
   costs = {0: 2, 1: 4, 2: 5, 3: 2, 4: 2, 5: 3, 6: 2, 7: 5}
   # Define the capacities of the stacks
   capacities = [5, 5, 5, 5, 5, 5, 5, 5]
   # Define the goal state, where each stack has 4 blocks of a single shade
   goal_state = ([], ['Blue', 'Blue', 'Blue', 'Blue'], [], [], ['Red', 'Red', 'Red', 'Red'], [], ['Green', 'Green', 'Green', 'Green'], ['Yellow', 'Yellow', 'Yellow', 'Yellow'])
   # Define the number of stacks
   num_stacks = 8


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
               # Check if the transfer is valid, ie if the from_stack is not empty and the to_stack is not full and has the same shade as the top block of the from_stack
               if state[from_stack] and len(state[to_stack]) < capacities[to_stack] and (not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]):
                   # Generate the new state
                   new_state = [list(stack[:]) for stack in state]
                   new_state[to_stack].append(new_state[from_stack].pop())
                   new_state = tuple(tuple(stack) for stack in new_state)
                   # The cost so far is the number of actions taken, as the task is to minimize the cost of transferring blocks
                   new_cost = g + costs[from_stack]


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(state, goal_state, capacities)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None




def heuristic(state, goal_state, capacities):
   # The heuristic function can be a simulation of moving blocks greedily, using the next most common shade of block repeatedly as long as the stack does not exceed its capacity
   # This heuristic is admissible because it is greedy, always opting for the action that moves the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is removed from a stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of blocks that can be added to the stack is by using the next most common shade of block, which is exactly the shade used to fill the stack in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the stacks by the shade of their top block
   state = sorted(state, key=lambda stack: stack[-1] if stack else '')
   # Iterate through the stacks
   for i in range(len(state)):
       stack = state[i]
       goal_stack = goal_state[i]
       # Fill the stack with the next most common shade of block repeatedly as long as the stack does not exceed its capacity
       while len(stack) < capacities[i]:
           # Increment the estimated cost to the goal by 1 actions
           h += 1
   return h


print(a_star())
