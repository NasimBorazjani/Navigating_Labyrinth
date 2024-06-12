
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = (['Yellow', 'Blue', 'Blue', 'Green'], [], ['Yellow', 'Green', 'Red', 'Red'], ['Green', 'Red', 'Yellow', 'Blue'], [], [])
   # Define the cost of moving one block to the top of each stack
   stack_costs = {0: 7, 1: 3, 2: 5, 3: 5, 4: 1, 5: 3}
   # Define the maximum capacity of each stack
   stack_capacity = 4
   # Define the goal state, where each stack has 3 blocks of a single shade
   goal_state = (['Blue', 'Blue', 'Blue', 'Blue'], ['Green', 'Green', 'Green', 'Green'], ['Red', 'Red', 'Red', 'Red'], ['Yellow', 'Yellow', 'Yellow', 'Yellow'], [], [])


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which involves transferring a block from one stack to another
       for from_stack in range(len(state)):
           for to_stack in range(len(state)):
               # Check if the transfer is valid, ie if the from_stack is not empty and the to_stack is not full and has the same shade as the top block of the from_stack
               if state[from_stack] and len(state[to_stack]) < stack_capacity and (not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]):
                   # Generate the new state
                   new_state = [list(stack[:]) for stack in state]
                   new_state[to_stack].append(new_state[from_stack].pop())
                   new_state = tuple(tuple(stack) for stack in new_state)
                   # The cost so far is the number of actions taken, as the task is to minimize the cost of the actions required to sort the blocks
                   new_cost = g + stack_costs[to_stack]


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(state, goal_state, stack_costs)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None




def heuristic(state, goal_state, stack_costs):
   # The heuristic function can be a simulation of sorting the blocks greedily, using the next smallest shade block repeatedly as long as the stack does not exceed its capacity
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is removed from a stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of blocks that can be added to the stack is by using the smallest shade block that won't cause an overflow, which is exactly the block used to fill the stack in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the shades by increasing frequency
   shades = sorted(set(block for stack in state for block in stack), key=lambda shade: -state.count(shade))
   # Iterate through the stacks
   for i in range(len(state)):
       stack_shade = state[i][-1] if state[i] else None
       # Sort the blocks in the stack by shade
       state[i] = sorted(state[i], key=lambda shade: shades.index(shade))
       # Fill the stack with the next smallest shade block repeatedly as long as the stack does not exceed its capacity
       while len(state[i]) < stack_capacity and shades.index(stack_shade) < len(shades) - 1:
           stack_shade = shades[shades.index(stack_shade) + 1]
           state[i].append(stack_shade)
           # Increment the estimated cost to the goal by 1 actions
           h += 1
   return h


print(a_star())
