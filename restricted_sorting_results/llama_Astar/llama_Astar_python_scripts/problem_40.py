
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = ([], [], ['Green', 'Yellow', 'Black', 'Red', 'Black'], ['Black', 'Red', 'Yellow', 'Blue', 'Yellow'], ['Green', 'Blue', 'Blue', 'Red', 'Black'], [], [], ['Red', 'Green', 'Blue', 'Green', 'Yellow'])
   # Define the costs of moving a block to the top of each stack
   costs = {0: 5, 1: 5, 2: 1, 3: 7, 4: 7, 5: 9, 6: 1, 7: 6}
   # Define the maximum capacity of each stack
   capacity = 5
   # Define the goal state, where each stack has 4 blocks of a single shade
   goal_state = ([], [], ['Black', 'Black', 'Black', 'Black'], ['Red', 'Red', 'Red', 'Red'], ['Green', 'Green', 'Green', 'Green'], ['Blue', 'Blue', 'Blue', 'Blue'], ['Yellow', 'Yellow', 'Yellow', 'Yellow'], [])


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
                   # Check if the transfer is valid, ie if the to_stack is empty or has only blocks of the same shade as the top block of the from_stack
                   if not to_stack or to_stack[-1] == from_stack[-1]:
                       # Check if the to_stack is not full
                       if len(to_stack) < capacity:
                           # Generate the new state
                           new_state = [list(stack[:]) for stack in state]
                           new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                           new_state = tuple(tuple(stack) for stack in new_state)
                           # The cost so far is the number of actions taken, as the task is to minimize the cost of transferring blocks
                           new_cost = g + costs[to_stack_ind]


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               h = heuristic(state, goal_state, costs)
                               heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, goal_state, costs):
   # The heuristic function can be a simulation of moving blocks greedily, using the next most expensive stack as the destination stack for each block
   # This heuristic is admissible because it is greedy, always opting for the action that moves the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is moved to a less expensive stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum cost of moving a block is by moving it to the least expensive stack, which is exactly the stack used to move the block in the heuristic
   h = 0
   # Sort the stacks by decreasing cost
   stacks = sorted(range(len(state)), key=lambda i: costs[i], reverse=True)
   # Iterate through the stacks
   for i in range(len(state)):
       # For each stack, move the blocks to the next most expensive stack
       while state[i]:
           # Find the next most expensive stack that is not full
           for j in stacks:
               if len(state[j]) < capacity:
                   # Move the block to the next most expensive stack
                   state[j].append(state[i].pop())
                   # Increment the estimated cost to the goal by 1 actions
                   h += 1
                   break
   return h


print(a_star())
