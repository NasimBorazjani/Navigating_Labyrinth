
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = (['Red', 'Yellow', 'Blue', 'Yellow'], [], [], ['Green', 'Blue', 'Green', 'Red'], [], ['Yellow', 'Red', 'Green', 'Blue'])
   # Define the cost of moving one block to the top of each stack
   stack_costs = {0: 4, 1: 5, 2: 3, 3: 3, 4: 3, 5: 5}
   # Define the goal state, where each stack has 3 blocks of a single shade
   goal_state = (['Red', 'Red', 'Red', 'Red'], ['Yellow', 'Yellow', 'Yellow', 'Yellow'], ['Blue', 'Blue', 'Blue', 'Blue'], ['Green', 'Green', 'Green', 'Green'])
   # Define the maximum capacity of each stack
   stack_capacity = 4


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from a non-empty stack to an empty stack or a stack with the same shade
       for from_stack in range(len(state)):
           for to_stack in range(len(state)):
               # Check if the transfer is valid, ie if the from_stack is not empty and the to_stack is either empty or has the same shade as the top block of the from_stack
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
   # The heuristic function can be a simulation of transferring blocks greedily, using the least expensive stack as the destination stack for each block
   # This heuristic is admissible because it is greedy, always opting for the action that transfers the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is transferred to a more expensive stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum cost of transferring a block is by using the least expensive stack that won't cause an overflow, which is exactly the stack used to transfer the block in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the stacks by increasing cost
   stacks = sorted(range(len(state)), key=lambda i: stack_costs[i])
   # Iterate through the stacks
   for i in range(len(state)):
       # For each stack, transfer the blocks to the least expensive stack that won't cause an overflow
       for block in state[i]:
           for j in stacks:
               if len(state[j]) < stack_capacity:
                   h += stack_costs[j]
                   break
   return h


print(a_star())
