
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = (['Pink', 'Red', 'Black', 'Green', 'Yellow', 'Yellow', 'Pink'], [], [], ['Pink', 'White', 'Yellow', 'Blue', 'Green', 'Blue', 'Black'], ['Black', 'Blue', 'Red', 'Pink', 'Yellow', 'Yellow', 'Blue'], [], ['White', 'Black', 'Yellow', 'Green', 'Red', 'Green', 'Green'], [], [], ['Pink', 'Red', 'Black', 'White', 'White', 'Red', 'White'], ['Blue', 'Green', 'Pink', 'Blue', 'White', 'Red', 'Black'], [])
   # Define the cost of moving one block to the top of each stack
   cost_dict = {0: 8, 1: 5, 2: 4, 3: 12, 4: 9, 5: 9, 6: 3, 7: 2, 8: 11, 9: 9, 10: 3, 11: 2}
   # Define the maximum capacity of each stack
   capacity = 7
   # Define the goal state, where each stack has 6 blocks of a single shade
   goal_state = ([], ['Pink'] * 6, ['Red'] * 6, ['Black'] * 6, ['Green'] * 6, ['Yellow'] * 6, ['White'] * 6, ['Blue'] * 6)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which involves transferring a block from a non-empty stack to an empty stack or a stack with the same shade
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
   # The heuristic function can be a simulation of moving blocks greedily, using the next most expensive stack as the destination for each block
   # This heuristic is admissible because it is greedy, always opting for the action that minimizes the cost, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is moved to a more expensive stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum cost of moving a block is by using the most expensive stack that won't cause an overflow, which is exactly the stack used to move the block in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the stacks by decreasing cost
   stacks = sorted(range(len(state)), key=lambda i: cost_dict[i], reverse=True)
   # Iterate through the stacks
   for i in range(len(state)):
       # For each stack, move the blocks to the next most expensive stack
       while state[i]:
           for j in stacks:
               # Check if the transfer is valid
               if not state[j] or state[j][-1] == state[i][-1]:
                   # Increment the estimated cost to the goal by 1 actions
                   h += 1
                   break
   return h


print(a_star())
