
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = (['White', 'White', 'Yellow', 'White', 'White', 'Black'], [], ['Red', 'Red', 'Green', 'Green', 'Green', 'Red'], ['Black', 'Yellow', 'Black', 'Yellow', 'Blue', 'Green'], ['Yellow', 'Blue', 'Black', 'Green', 'Blue', 'Red'], [], ['Red', 'Black', 'Blue', 'Yellow', 'Blue', 'White'], [], [], [])
   # Define the cost of moving one block to the top of each stack
   cost_dict = {0: 6, 1: 7, 2: 11, 3: 10, 4: 7, 5: 2, 6: 3, 7: 3, 8: 11, 9: 8}
   # Define the goal state, where each stack has 5 blocks of a single shade
   goal_state = (['White', 'White', 'White', 'White', 'White', 'White'], ['Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow'], ['Red', 'Red', 'Red', 'Red', 'Red', 'Red'], ['Green', 'Green', 'Green', 'Green', 'Green', 'Green'], ['Black', 'Black', 'Black', 'Black', 'Black', 'Black'], ['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'])
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


       # Generate all possible actions from the current state, which includes transferring a block from a non-empty stack to an empty stack or a stack with the same shade
       for from_stack in range(num_stacks):
           for to_stack in range(num_stacks):
               # Check if the transfer is valid
               if state[from_stack] and (not state[to_stack] or state[from_stack][-1] == state[to_stack][-1]):
                   # Generate the new state
                   new_state = [list(stack[:]) for stack in state]
                   new_state[to_stack].append(new_state[from_stack].pop())
                   new_state = tuple(tuple(stack) for stack in new_state)
                   # The cost so far is the number of transfers made
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(state, goal_state, cost_dict)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None




def heuristic(state, goal_state, cost_dict):
   # The heuristic function can be a simulation of the transfers greedily, using the next most expensive stack as the destination stack for the next transfer, until all stacks are sorted
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the stacks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a transfer is made to a less expensive stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum cost of a transfer is by using the most expensive stack that won't cause an overflow, which is exactly the stack used to transfer the block in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the stacks by the cost of transferring a block to the top of each stack
   stacks_sorted = sorted(range(len(state)), key=lambda i: cost_dict[i])
   # Iterate through the stacks
   for i in stacks_sorted:
       # If the stack is not sorted, transfer the top block to the most expensive stack that won't cause an overflow
       if state[i] and state[i][-1] != goal_state[i][-1]:
           for j in stacks_sorted:
               if not state[j] or state[j][-1] == state[i][-1]:
                   # Increment the estimated cost to the goal by 1 actions
                   h += 1
                   break
   return h


print(a_star())
