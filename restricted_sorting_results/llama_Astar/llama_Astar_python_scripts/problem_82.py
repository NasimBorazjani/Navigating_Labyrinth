
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = (['Red', 'Black', 'Yellow', 'Black', 'White', 'Blue', 'White'], [], ['White', 'Blue', 'Green', 'Yellow', 'Blue', 'Yellow', 'Pink'], ['Yellow', 'Red', 'Pink', 'Green', 'Black', 'Red', 'White'], [], ['Pink', 'Red', 'Green', 'Green', 'Green', 'Black', 'Blue'], ['Pink', 'Blue', 'Blue', 'Black', 'Red', 'Pink', 'Black'], ['Yellow', 'Red', 'Pink', 'White', 'White', 'Yellow', 'Green'], [], [], [], [])
   # Define the costs of moving one block to the top of each stack
   costs = {0: 7, 1: 13, 2: 10, 3: 12, 4: 4, 5: 13, 6: 2, 7: 11, 8: 11, 9: 10, 10: 8, 11: 9}
   # Define the number of stacks and the capacity of each stack
   num_stacks = 12
   capacity = 7


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the state is the goal state, return the actions taken
       if all(len(stack) == 0 or len(stack) == capacity for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from a non-empty stack to an empty stack or a stack with only blocks of the same shade
       for from_stack_ind, from_stack in enumerate(state):
           if from_stack:
               for to_stack_ind, to_stack in enumerate(state):
                   if not to_stack or to_stack[-1] == from_stack[-1]:
                       # Check if the new state is valid, ie the stacks do not exceed their capacity
                       if len(to_stack) < capacity:
                           # Generate the new state
                           new_state = [list(stack[:]) for stack in state]
                           new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                           new_state = tuple(tuple(stack) for stack in new_state)
                           # The cost so far is the number of actions taken, as the task is to minimize the cost of the actions
                           new_cost = g + costs[from_stack_ind]


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               h = heuristic(new_state, costs)
                               heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, costs):
   # The heuristic function can be a simulation of moving blocks greedily, using the next most expensive stack as the destination stack for each block
   # This heuristic is admissible because it is greedy, always opting for the action that minimizes the cost, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is moved to a more expensive stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum cost of moving a block is by using the most expensive stack that won't cause the stack to exceed its capacity
   h = 0
   # Sort the stacks by decreasing cost
   stacks = sorted(range(len(state)), key=lambda i: costs[i], reverse=True)
   # Iterate through the stacks
   for i in range(len(state)):
       stack = state[i]
       # Move the blocks in the stack to the next most expensive stack as long as the stack does not exceed its capacity
       while stack and len(state[stacks[0]]) < capacity:
           # Increment the estimated cost to the goal by 1 actions
           h += 1
           # Move the block to the most expensive stack
           state[stacks[0]].append(stack.pop())
   return h


print(a_star())
