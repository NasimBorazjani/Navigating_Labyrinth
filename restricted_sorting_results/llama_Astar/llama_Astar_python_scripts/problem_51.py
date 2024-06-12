
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = ([], [], [], ['Green', 'Blue', 'Blue', 'Green', 'Black'], ['Red', 'Green', 'Blue', 'Blue', 'Red'], ['Black', 'Black', 'Yellow', 'Red', 'Yellow'], [], ['Yellow', 'Black', 'Green', 'Red', 'Yellow'])
   # Define the costs of moving one block to the top of each stack
   costs = {0: 7, 1: 8, 2: 2, 3: 8, 4: 9, 5: 6, 6: 8, 7: 1}
   # Define the goal state, where each stack has 4 blocks of a single shade
   goal_state = (['Green', 'Green', 'Green', 'Green'], ['Blue', 'Blue', 'Blue', 'Blue'], ['Red', 'Red', 'Red', 'Red'], ['Black', 'Black', 'Black', 'Black'], ['Yellow', 'Yellow', 'Yellow', 'Yellow'])
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


       # Generate all possible actions from the current state, which includes transferring a block from a non-empty stack to an empty stack or a stack with only blocks of the same shade
       for from_stack in range(num_stacks):
           if state[from_stack]:
               for to_stack in range(num_stacks):
                   # Check if transferring a block from the current stack to the other stack is valid
                   if not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]:
                       # Generate the new state
                       new_state = [list(stack[:]) for stack in state]
                       new_state[to_stack].append(new_state[from_stack].pop())
                       new_state = tuple(tuple(stack) for stack in new_state)
                       # The cost so far is the number of actions taken, as the task is to minimize the cost of transferring blocks
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(state, goal_state, costs)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None




def heuristic(state, goal_state, costs):
   # The heuristic function can be a simulation of moving blocks greedily, using the least expensive stack as the target for each block
   # This heuristic is admissible because it is greedy, always opting for the action that moves the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is moved to a more expensive stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum cost of moving a block is by using the least expensive stack that won't cause an overflow, which is exactly the stack used to move the block in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the stacks by the cost of moving a block to the top of each stack
   stacks = sorted(range(len(state)), key=lambda i: costs[i])
   # Iterate through the stacks
   for i in range(len(state)):
       # For each stack, calculate the cost of moving all its blocks to the least expensive stack
       for block in state[i]:
           h += costs[stacks[0]]
   return h


print(a_star())
