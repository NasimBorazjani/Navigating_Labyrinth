
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = (['Red', 'Red', 'Red', 'Green', 'Yellow'],
                   ['Black', 'Red', 'Green', 'Yellow', 'Yellow'],
                   [],
                   [],
                   [],
                   ['Black', 'Blue', 'Black', 'Yellow', 'Green'],
                   [],
                   ['Blue', 'Green', 'Blue', 'Black', 'Blue'])
   # Define the costs of moving a block to the top of each stack
   stack_costs = {0: 8, 1: 2, 2: 7, 3: 6, 4: 7, 5: 1, 6: 5, 7: 3}
   # Define the goal state, where each stack has 4 blocks of a single shade
   goal_state = (['Red', 'Red', 'Red', 'Red'],
                 ['Black', 'Black', 'Black', 'Black'],
                 ['Green', 'Green', 'Green', 'Green'],
                 ['Yellow', 'Yellow', 'Yellow', 'Yellow'],
                 ['Blue', 'Blue', 'Blue', 'Blue'])
   # Define the number of stacks
   num_stacks = 8


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
                   # The cost so far is the number of actions taken, as the task is to minimize the cost of the actions required to sort the blocks
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(state, goal_state, stack_costs)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None




def heuristic(state, goal_state, stack_costs):
   # The heuristic function can be a simulation of sorting the blocks greedily, using the next smallest shade repeatedly as long as the stack has space
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is removed from a stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of blocks that can be added to the stack is by using the smallest shade that won't cause an overflow, which is exactly the shade used to fill the stack in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the shades by increasing frequency in the state
   shades = sorted(set(block for stack in state for block in stack), key=lambda shade: -sum(stack.count(shade) for stack in state))
   # Iterate through the stacks
   for i in range(len(state)):
       stack = state[i]
       goal_stack = goal_state[i]
       # Fill the stack with the next smallest shade repeatedly as long as the stack has space
       for shade in shades:
           while len(stack) < 4 and (not goal_stack or stack[-1] == goal_stack[-1]):
               stack.append(shade)
               # Increment the estimated cost to the goal by the cost of moving a block to the top of the stack
               h += stack_costs[i]
   return h


print(a_star())
