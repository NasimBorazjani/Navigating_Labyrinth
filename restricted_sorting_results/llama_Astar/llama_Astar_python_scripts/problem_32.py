
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = (['Black', 'Yellow', 'Blue', 'Yellow', 'Red'], [], [], [], [], ['Blue', 'Green', 'Blue', 'Green', 'Blue'], ['Yellow', 'Black', 'Green', 'Yellow', 'Black'], ['Red', 'Red', 'Red', 'Green', 'Black'])
   # Define the costs of moving a block to the top of each stack
   costs = {0: 5, 1: 8, 2: 1, 3: 6, 4: 8, 5: 2, 6: 1, 7: 8}
   # Define the capacities of the stacks
   capacities = [5, 5, 5, 5, 5, 5, 5, 5]
   # Define the goal state, where each stack has 4 blocks of a single shade
   goal_state = (['Black'], ['Yellow'], ['Blue'], ['Yellow'], ['Red'], ['Green'], ['Blue'], ['Yellow'])


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which involves transferring a block from a non-empty stack to an empty stack or a stack with only blocks of the same shade
       for from_stack in range(len(state)):
           if state[from_stack]:
               for to_stack in range(len(state)):
                   # Check if the transfer is valid, ie if the to_stack is empty or has only blocks of the same shade as the top block of the from_stack
                   if not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]:
                       # Check if the to_stack is not full
                       if len(state[to_stack]) < capacities[to_stack]:
                           # Generate the new state
                           new_state = [list(stack[:]) for stack in state]
                           new_state[to_stack].append(new_state[from_stack].pop())
                           new_state = tuple(tuple(stack) for stack in new_state)
                           # The cost so far is the number of actions taken, as the task is to minimize the cost of transferring blocks
                           new_cost = g + costs[to_stack]


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               h = heuristic(state, goal_state, capacities)
                               heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None




def heuristic(state, goal_state, capacities):
   # The heuristic function can be a simulation of moving blocks greedily, using the next smallest shade block repeatedly as long as the stack does not exceed its capacity
   # This heuristic is admissible because it is greedy, always opting for the action that moves the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is removed from a stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of blocks that can be added to the stack is by using the smallest shade block that won't cause an overflow, which is exactly the block used to fill the stack in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Iterate through the stacks
   for i in range(len(state)):
       # Sort the blocks in the stack by shade
       stack = sorted(state[i], key=lambda x: (x != 'Black', x != 'Yellow', x != 'Blue', x != 'Green', x != 'Red'))
       # Fill the stack with the next smallest shade block repeatedly as long as the stack does not exceed its capacity
       for shade in ['Black', 'Yellow', 'Blue', 'Green', 'Red']:
           while len(stack) < capacities[i] and stack and stack[-1] == shade:
               stack.pop()
               # Increment the estimated cost to the goal by 1 actions
               h += 1
   return h


print(a_star())
