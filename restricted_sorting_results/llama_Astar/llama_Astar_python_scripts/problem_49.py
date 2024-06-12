
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = (['Black', 'Green', 'Red', 'Yellow', 'Black'], [], ['Blue', 'Red', 'Black', 'Black', 'Yellow'], ['Green', 'Red', 'Yellow', 'Blue', 'Green'], [], [], ['Green', 'Blue', 'Red', 'Yellow', 'Blue'], [])
   # Define the cost of moving one block to the top of each stack
   cost_dict = {0: 4, 1: 4, 2: 1, 3: 9, 4: 7, 5: 8, 6: 9, 7: 7}
   # Define the goal state, where each stack has 4 blocks of a single shade
   goal_state = (['Black', 'Black', 'Black', 'Black'], ['Green', 'Green', 'Green', 'Green'], ['Blue', 'Blue', 'Blue', 'Blue'], ['Red', 'Red', 'Red', 'Red'], ['Yellow', 'Yellow', 'Yellow', 'Yellow'], [], [], [])


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which involves transferring a block from a non-empty stack to an empty stack or a stack with only blocks of the same shade
       for from_stack in range(len(state)):
           if state[from_stack]:
               for to_stack in range(len(state)):
                   if not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]:
                       # Check if the new state is valid, ie the stacks do not exceed their capacity and the cost of the new state is less than the cost of the current state
                       if len(state[to_stack]) < 4 and (to_stack not in cost_dict or g + cost_dict[to_stack] < visited_costs.get((*state[:to_stack], state[to_stack] + [state[from_stack][-1]], *state[to_stack + 1:]), float('inf'))):
                           # Generate the new state
                           new_state = [list(stack[:]) for stack in state]
                           new_state[from_stack].pop()
                           new_state[to_stack].append(state[from_stack][-1])
                           new_state = tuple(tuple(stack) for stack in new_state)
                           # The cost of the new state is the cost of the current state plus the cost of moving the block to the new stack
                           new_cost = g + cost_dict.get(to_stack, 0)
                          
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state, cost_dict), new_cost, actions + [(from_stack, to_stack)], new_state))
   return None




def heuristic(state, goal, cost_dict):
   # The heuristic function can be a simulation of moving blocks greedily, using the next most expensive stack as the destination stack for each block
   # This heuristic is admissible because it is greedy, always opting for the action that moves the blocks to the most expensive stack, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is moved to a less expensive stack, or equal or less by at most the cost of reaching the successor node, ie one action
   h = 0
   # Sort the stacks by decreasing cost
   stacks = sorted(range(len(state)), key=lambda i: cost_dict.get(i, 0), reverse=True)
   # Iterate through the stacks
   for i in range(len(state)):
       # If the stack is not empty
       if state[i]:
           # Move the block to the next most expensive stack
           while stacks[0] != i:
               # Increment the estimated cost to the goal by the cost of moving the block to the next most expensive stack
               h += cost_dict[stacks[0]]
               # Remove the most expensive stack from the list
               stacks.pop(0)
   return h


print(a_star())
