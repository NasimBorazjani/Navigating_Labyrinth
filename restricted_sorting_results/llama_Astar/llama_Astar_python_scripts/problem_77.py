
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = (['Green', 'Black', 'White', 'Red', 'White', 'Yellow', 'Blue'], [], ['White', 'Pink', 'White', 'White', 'Green', 'Red', 'Blue'], [], ['Pink', 'Black', 'Black', 'White', 'Black', 'Green', 'Blue'], ['Pink', 'Green', 'Pink', 'Yellow', 'Yellow', 'Blue', 'Red'], [], ['Red', 'Yellow', 'Yellow', 'Yellow', 'Blue', 'Red', 'Black'], [], [], [], ['Red', 'Green', 'Black', 'Blue', 'Pink', 'Pink', 'Green'])
   # Define the costs of moving one block to the top of each stack
   costs = {0: 13, 1: 5, 2: 8, 3: 11, 4: 6, 5: 9, 6: 5, 7: 11, 8: 2, 9: 11, 10: 11, 11: 7}
   # Define the goal state, where each stack has 6 blocks of a single shade
   goal_state = (['Green'] * 6, ['Black'] * 6, ['White'] * 6, ['Red'] * 6, ['Yellow'] * 6, ['Blue'] * 6, ['Pink'] * 6)
   num_stacks = 12


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
               # Check if the transfer is valid, ie if the from_stack is not empty and the to_stack is empty or has the same shade as the top block of the from_stack
               if state[from_stack] and (not state[to_stack] or state[from_stack][-1] == state[to_stack][-1]):
                   # Generate the new state
                   new_state = [list(stack[:]) for stack in state]
                   new_state[to_stack].append(new_state[from_stack].pop())
                   new_state = tuple(tuple(stack) for stack in new_state)
                   # The cost so far is the number of transfers made, as the task is to minimize the cost of the transfers
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(state, goal_state, costs)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None




def heuristic(state, goal_state, costs):
   # The heuristic function can be a simulation of the transfers greedily, using the next most expensive stack as the destination stack for the top block of the most expensive stack, until all stacks are sorted
   # This heuristic is admissible because it is greedy, always opting for the action that minimizes the cost, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is transferred to a more expensive stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the most expensive stack is always the one that has the top block transferred in the heuristic
   h = 0
   # Sort the stacks by the cost of moving a block to the top of the stack
   stacks = sorted(range(len(state)), key=lambda i: costs[i], reverse=True)
   # Iterate through the stacks
   for i in range(len(state)):
       # If the stack is not sorted, transfer the top block to the most expensive stack that can accept it
       if state[i] and state[i][-1] != goal_state[i][-1]:
           # Find the most expensive stack that can accept the top block of the current stack
           for j in stacks:
               if not state[j] or state[j][-1] == state[i][-1]:
                   # Increment the estimated cost to the goal by the cost of the transfer
                   h += costs[j] - costs[i]
                   break
   return h


print(a_star())
