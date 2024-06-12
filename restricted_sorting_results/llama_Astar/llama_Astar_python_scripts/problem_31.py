
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = ([], [], ['Yellow', 'Yellow', 'Green', 'Black', 'Red'], ['Black', 'Green', 'Black', 'Blue', 'Yellow'], ['Green', 'Blue', 'Yellow', 'Red', 'Blue'], [], [], ['Black', 'Red', 'Green', 'Red', 'Blue'])
   # Define the costs of moving one block to the top of each stack
   costs = {0: 7, 1: 2, 2: 1, 3: 1, 4: 9, 5: 4, 6: 2, 7: 7}
   # Define the capacities of the stacks
   capacities = [5, 5, 5, 5, 5, 5, 5, 5]
   # Define the goal state, where each stack has 4 blocks of a single shade
   goal_state = ([], [], ['Yellow', 'Yellow', 'Yellow', 'Yellow'], ['Black', 'Black', 'Black', 'Black'], ['Green', 'Green', 'Green', 'Green'], ['Blue', 'Blue', 'Blue', 'Blue'], ['Red', 'Red', 'Red', 'Red'], [])


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from a non-empty stack to an empty stack or a stack with only blocks of the same shade
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
   # The heuristic function can be a simulation of transferring blocks greedily, using the least costly stack as the destination stack for each block
   # This heuristic is admissible because it is greedy, always opting for the action that transfers the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is transferred to a more costly stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum cost of transferring a block is by using the least costly stack that won't cause the stack to exceed its capacity
   h = 0
   # Sort the stacks by the cost of transferring a block to the top of each stack
   stacks = sorted(range(len(state)), key=lambda i: costs[i])
   # Iterate through the stacks
   for i in stacks:
       # If the stack is not empty
       if state[i]:
           # Transfer the blocks to the least costly stack that won't exceed its capacity
           while len(state[i]) > capacities[i]:
               # Find the least costly stack that has the same shade as the top block of the current stack
               for j in stacks:
                   if state[j] and state[j][-1] == state[i][-1]:
                       # Transfer the top block of the current stack to the least costly stack
                       state[j].append(state[i].pop())
                       # Increment the estimated cost to the goal by 1 actions
                       h += 1
   return h


print(a_star())
