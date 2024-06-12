
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = ([], ['Yellow', 'Blue', 'Blue', 'Yellow', 'Green'], ['Black', 'Red', 'Black', 'Green', 'Red'], ['Yellow', 'Yellow', 'Red', 'Black', 'Blue'], [], ['Blue', 'Red', 'Green', 'Green', 'Black'], [], [])
   # Define the costs of moving one block to the top of each stack
   costs = {0: 6, 1: 3, 2: 5, 3: 2, 4: 8, 5: 3, 6: 8, 7: 5}
   # Define the capacities of the stacks
   capacities = [5, 5, 5, 5, 5, 5, 5, 5]
   # Define the goal state, where each stack has 4 blocks of a single shade
   goal_state = (['Blue', 'Blue', 'Blue', 'Blue'], ['Green', 'Green', 'Green', 'Green'], ['Red', 'Red', 'Red', 'Red'], ['Yellow', 'Yellow', 'Yellow', 'Yellow'], ['Black', 'Black', 'Black', 'Black'])


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from a non-empty stack to an empty stack or a stack with only blocks of the same shade
       for from_stack_ind, from_stack in enumerate(state):
           if from_stack:
               for to_stack_ind, to_stack in enumerate(state):
                   if not to_stack or to_stack[-1] == from_stack[-1]:
                       # Check if the transfer would not exceed the capacity of the receiving stack
                       if len(to_stack) < capacities[to_stack_ind]:
                           # Generate the new state
                           new_state = [list(stack[:]) for stack in state]
                           new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                           new_state = tuple(tuple(stack) for stack in new_state)
                           # The cost so far is the number of actions taken, as the task is to minimize the cost of transferring blocks
                           new_cost = g + costs[from_stack_ind]


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               h = heuristic(state, goal_state, capacities)
                               heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, goal_state, capacities):
   # The heuristic function can be a simulation of transferring blocks greedily, using the least costly stack as the destination stack for each block
   # This heuristic is admissible because it is greedy, always opting for the action that transfers the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is transferred to a more costly stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum cost of transferring a block is by using the least costly stack that won't cause an overflow, which is exactly the stack used to transfer the block in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the stacks by the cost of transferring a block to the top of each stack
   stacks = sorted(range(len(state)), key=lambda i: costs[i])
   # Iterate through the stacks
   for i in range(len(state)):
       # For each stack, transfer the blocks to the least costly stack that won't cause an overflow
       while state[i]:
           for j in stacks:
               if len(state[j]) < capacities[j] and (not state[j] or state[j][-1] == state[i][-1]):
                   # Increment the estimated cost to the goal by 1 actions
                   h += 1
                   break
   return h


print(a_star())
