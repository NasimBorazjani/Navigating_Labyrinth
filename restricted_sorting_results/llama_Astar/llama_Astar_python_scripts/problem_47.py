
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = ([], [], ['Red', 'Yellow', 'Black', 'Yellow', 'Green'], ['Red', 'Red', 'Blue', 'Red', 'Black'], [], ['Black', 'Blue', 'Yellow', 'Blue', 'Black'], [], ['Green', 'Green', 'Yellow', 'Blue', 'Green'])
   # Define the costs of moving one block to the top of each stack
   costs = {0: 4, 1: 6, 2: 8, 3: 2, 4: 4, 5: 7, 6: 7, 7: 5}
   # Define the capacities of the stacks
   capacities = [5, 5, 5, 5, 5, 5, 5, 5]
   # Define the goal state, where each stack has 4 blocks of a single shade
   goal_state = ([], [], ['Red'], ['Red'], ['Blue'], ['Black'], ['Yellow'], ['Green'])


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which involves transferring a block from a non-empty stack to an empty stack or a stack with only blocks of the same shade
       for from_stack_ind, from_stack in enumerate(state):
           if from_stack:
               for to_stack_ind, to_stack in enumerate(state):
                   if not to_stack or to_stack[-1] == from_stack[-1]:
                       # Check if the stack to which the block is transferred has not exceeded its capacity
                       if len(to_stack) < capacities[to_stack_ind]:
                           # Generate the new state
                           new_state = [list(stack[:]) for stack in state]
                           new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                           new_state = tuple(tuple(stack) for stack in new_state)
                           # The cost so far is the number of actions taken, as the task is to minimize the cost of transferring blocks
                           new_cost = g + costs[from_stack_ind]


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               h = heuristic(state, goal_state, costs)
                               heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, goal_state, costs):
   # The heuristic function can be a simulation of moving blocks greedily, using the next most expensive stack as the destination stack for each block
   # This heuristic is admissible because it is greedy, always opting for the action that moves the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is moved to a less expensive stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum cost of moving a block is by using the most expensive stack that won't cause an overflow, which is exactly the stack used to move the block in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the stacks by decreasing costs
   stacks = sorted(range(len(state)), key=lambda i: costs[i], reverse=True)
   # Iterate through the stacks
   for i in range(len(state)):
       # For each stack, move the blocks to the next most expensive stack as long as it is possible
       while state[i] and state[stacks[0]] != state[i]:
           # Increment the estimated cost to the goal by 1 actions
           h += 1
   return h


print(a_star())
