
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = [['Yellow', 'Yellow', 'Pink', 'Black', 'Green', 'Green', 'Yellow'],
                   ['Pink', 'Yellow', 'White', 'Red', 'Black', 'Blue', 'Blue'],
                   [],
                   [],
                   ['Pink', 'Green', 'Pink', 'Pink', 'Blue', 'Red', 'Red'],
                   ['Black', 'Black', 'Black', 'Blue', 'Yellow', 'Red', 'White'],
                   [],
                   [],
                   [],
                   [],
                   [],
                   ['Green', 'Blue', 'Red', 'Red', 'Green', 'White', 'Black'],
                   ['White', 'White', 'Green', 'Yellow', 'Blue', 'White', 'Pink']]
   # Define the costs of moving one block to the top of each stack
   costs = {0: 12, 1: 11, 2: 5, 3: 11, 4: 10, 5: 9, 6: 5, 7: 5, 8: 3, 9: 10, 10: 5, 11: 5}
   num_stacks = 12


   visited_costs = {}
   visited_costs[tuple(initial_state)] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the state is the goal state, return the actions taken
       if all(len(stack) == 0 or len(set(stack)) == 1 for stack in state):
           return actions


       # Generate all possible actions from the current state
       for from_stack_ind in range(num_stacks):
           for to_stack_ind in range(num_stacks):
               # Check if the action is valid, ie if the from_stack is not empty and the to_stack is empty or has the same color as the top block of the from_stack
               if state[from_stack_ind] and (not state[to_stack_ind] or state[to_stack_ind][-1] == state[from_stack_ind][-1]):
                   # Generate the new state
                   new_state = [stack[:] for stack in state]
                   new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                   new_state = [stack for stack in new_state if stack]
                   # The cost so far is the number of actions taken
                   new_cost = g + 1


                   if tuple(new_state) not in visited_costs or new_cost < visited_costs[tuple(new_state)]:
                       visited_costs[tuple(new_state)] = new_cost
                       h = heuristic(state, costs)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, costs):
   # The heuristic function can be a simulation of moving blocks greedily, using the next most expensive stack as the destination stack for each block
   # This heuristic is admissible because it is greedy, always opting for the action that moves the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is moved to a less expensive stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum cost of moving a block to a more expensive stack is by using the most expensive stack that won't cause an overflow, which is exactly the stack used to move the block in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the stacks by decreasing cost
   stacks = sorted(range(len(state)), key=lambda i: costs[i], reverse=True)
   # Iterate through the stacks
   for i in range(len(state)):
       # If the stack is not empty
       if state[i]:
           # Move the block to the next most expensive stack
           while state[i]:
               h += costs[stacks[0]]
               stacks = stacks[1:]
   return h


print(a_star())
