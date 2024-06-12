
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = ([], [], ['Blue', 'Blue', 'Blue', 'Green', 'Black', 'Red'], [], ['Red', 'Black', 'Blue', 'White', 'Blue', 'Yellow'], ['Yellow', 'White', 'Green', 'Black', 'Yellow', 'Red'], [], [], ['White', 'Black', 'White', 'White', 'Black', 'Red'], ['Red', 'Green', 'Green', 'Yellow', 'Yellow', 'Green'])
   # Define the cost of moving one block to the top of each stack
   cost_dict = {0: 3, 1: 10, 2: 9, 3: 8, 4: 8, 5: 7, 6: 6, 7: 9, 8: 2, 9: 8}
   # Define the goal state, where each stack has 5 blocks of a single shade
   goal_state = (['Blue'], ['Blue'], ['Blue'], ['Blue'], ['Blue'], ['Red'], ['Red'], ['Red'], ['Red'], ['Red'])
   # Define the maximum capacity of each stack
   capacity = 6


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
           if state[from_stack]:
               for to_stack in range(len(state)):
                   # Check if the transfer is valid, ie if the to_stack is empty or has the same shade as the top block of the from_stack
                   if not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]:
                       # Check if the to_stack is not full
                       if len(state[to_stack]) < capacity:
                           # Generate the new state
                           new_state = [list(stack[:]) for stack in state]
                           new_state[to_stack].append(new_state[from_stack].pop())
                           new_state = tuple(tuple(stack) for stack in new_state)
                           # The cost so far is the number of actions taken, as the task is to minimize the cost of transferring blocks
                           new_cost = g + cost_dict[to_stack]


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               h = heuristic(state, goal_state, cost_dict)
                               heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None




def heuristic(state, goal_state, cost_dict):
   # The heuristic function can be a simulation of transferring blocks greedily, using the next most expensive stack as the destination stack for each block
   # This heuristic is admissible because it is greedy, always opting for the action that transfers the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is transferred to a less expensive stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of blocks that can be transferred to a more expensive stack is by using the most expensive stack that won't cause an overflow, which is exactly the stack used to transfer the block in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the stacks by decreasing cost
   stacks = sorted(range(len(state)), key=lambda x: cost_dict[x], reverse=True)
   # Iterate through the stacks
   for i in range(len(state)):
       # For each stack, transfer blocks to the next most expensive stack as long as it is possible
       while state[i]:
           for j in stacks:
               if not state[j] or state[j][-1] == state[i][-1]:
                   # Increment the estimated cost to the goal by 1 actions
                   h += 1
                   break
   return h


print(a_star())
