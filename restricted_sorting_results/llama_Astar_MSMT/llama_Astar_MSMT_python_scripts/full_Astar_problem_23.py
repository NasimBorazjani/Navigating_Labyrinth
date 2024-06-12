
import heapq


def initialize():
   # Define the initial state of the stacks as a list of lists
   initial_state = [['Green', 'Green', 'Blue', 'Red'], ['Blue', 'Red', 'Yellow', 'Blue'], [], ['Green', 'Yellow', 'Red', 'Yellow'], [], []]
   num_stacks = 6
   stack_capacity = 4
   # The cost of moving one block to the top of each stack
   move_costs = {0: 2, 1: 7, 2: 4, 3: 7, 4: 6, 5: 3}
   # The colors of the blocks
   colors = ['Green', 'Blue', 'Red', 'Yellow']


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_stacks, stack_capacity, move_costs, colors, visited_costs, queue
  
def a_star():
  
   initial_state, num_stacks, stack_capacity, move_costs, colors, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the state is the goal state, return the actions taken
       if all(len(stack) == 1 or len(stack) == stack_capacity and len(set(stack)) == 1 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring one block from a stack to another
       for from_stack in range(num_stacks):
           for to_stack in range(num_stacks):
               # Check if the transfer is valid, ie if the to_stack is empty or has only blocks of the same color as the top block of the from_stack
               if len(state[to_stack]) < stack_capacity and (len(state[from_stack]) == 0 or state[to_stack][-1] == state[from_stack][-1]):
                   # Generate the new state
                   new_state = [list(stack[:]) for stack in state]
                   new_state[to_stack].append(new_state[from_stack].pop())
                   new_state = [stack for stack in new_state if stack]
                   new_cost = g + move_costs[from_stack]
                  
                   if new_state not in visited_costs or new_cost < visited_costs[tuple(tuple(stack) for stack in new_state)]:
                       visited_costs[tuple(tuple(stack) for stack in new_state)] = new_cost
                       h = heuristic(new_state, colors)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None




def heuristic(state, colors):
   # The heuristic function can be a simulation of moving blocks greedily, using the next most common color in the remaining stacks as the color of the blocks to be moved
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is moved to a stack with a different color, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of blocks that can be moved to a stack in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Count the remaining blocks of each color
   color_counts = {color: sum(stack.count(color) for stack in state) for color in colors}
   # Sort the colors by the count of their remaining blocks
   sorted_colors = sorted(colors, key=lambda color: color_counts[color])
   # Iterate through the stacks
   for stack in state:
       # If the stack is not empty
       if stack:
           # Find the most common color in the remaining stacks
           most_common_color = sorted_colors.pop(0)
           # The number of blocks in the stack that are not of the most common color
           num_blocks_to_move = len([block for block in stack if block != most_common_color])
           # Increment the estimated cost to the goal by the number of blocks to move
           h += num_blocks_to_move
   return h


print(a_star())
