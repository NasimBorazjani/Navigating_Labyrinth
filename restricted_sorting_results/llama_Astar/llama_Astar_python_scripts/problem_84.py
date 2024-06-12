
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = ([], [], [], [], ['Pink', 'Red', 'Green', 'Pink', 'White', 'Blue', 'Yellow'], [], ['Yellow', 'White', 'Yellow', 'Blue', 'Yellow', 'Black', 'White'], ['Black', 'Green', 'Pink', 'Pink', 'Green', 'Yellow', 'Green'], ['White', 'Blue', 'Red', 'Red', 'Red', 'Yellow', 'Black'], ['Black', 'Blue', 'Blue', 'Pink', 'Red', 'White', 'Green'], [], ['Blue', 'Black', 'Black', 'White', 'Red', 'Green', 'Pink'])
   # Define the cost of moving one block to the top of each stack
   cost_dict = {0: 12, 1: 3, 2: 11, 3: 5, 4: 11, 5: 13, 6: 2, 7: 2, 8: 12, 9: 4, 10: 2, 11: 10}
   # Define the capacity of the stacks
   capacity = 7
   # Define the goal state, where each stack has 6 blocks of a single shade
   goal_state = ([], [], [], [], ['Pink', 'Pink', 'Pink', 'Pink', 'Pink', 'Pink'], [], ['Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow'], ['White', 'White', 'White', 'White', 'White', 'White'], ['Black', 'Black', 'Black', 'Black', 'Black', 'Black'], ['Red', 'Red', 'Red', 'Red', 'Red', 'Red'], ['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'], [], ['Green', 'Green', 'Green', 'Green', 'Green', 'Green'])


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
   # The heuristic function can be a simulation of moving blocks greedily, using the next most expensive stack as the destination stack for each block
   # This heuristic is admissible because it is greedy, always opting for the action that moves the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is moved to a less expensive stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum cost of moving a block to a more expensive stack is by using the most expensive stack that won't cause an overflow, which is exactly the stack used to move the block in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
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
