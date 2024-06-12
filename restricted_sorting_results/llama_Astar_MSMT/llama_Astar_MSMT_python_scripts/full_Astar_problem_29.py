
import heapq


def initialize():
   # Define the initial state of the stacks as a list of lists
   initial_state = [['Yellow', 'Green', 'Green', 'Blue'], [], [], ['Red', 'Green', 'Blue', 'Yellow'], [], ['Yellow', 'Blue', 'Red', 'Red']]
   # Define the costs of moving a block to the top of each stack
   stack_costs = {0: 1, 1: 5, 2: 6, 3: 7, 4: 7, 5: 5}
   # Define the capacities of the stacks
   stack_capacities = [4, 4, 4, 4, 4, 4]
   # Define the colors that need to be sorted
   colors = ['Red', 'Green', 'Blue', 'Yellow']


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, stack_costs, stack_capacities, colors, visited_costs, queue
  
def a_star():
  
   initial_state, stack_costs, stack_capacities, colors, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If all stacks are correctly sorted, return the actions taken
       if all(len(stack) == 3 and len(set(stack)) == 1 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from one stack to another
       for from_stack_ind, from_stack in enumerate(state):
           if from_stack:
               for to_stack_ind, to_stack in enumerate(state):
                   # Check if transferring a block from the current stack to the other stack is valid, ie if the other stack is not full and has the same color as the top block of the current stack
                   if len(to_stack) < stack_capacities[to_stack_ind] and (not to_stack or to_stack[-1] == from_stack[-1]):
                       # Generate the new state
                       new_state = [list(stack[:]) for stack in state]
                       # Remove the block from the current stack and add it to the other stack
                       new_state[from_stack_ind].pop()
                       new_state[to_stack_ind].append(from_stack[-1])
                       new_state = [tuple(stack) for stack in new_state]
                       # The cost so far is the number of actions taken, as the task is to minimize the cost of sorting the blocks
                       new_cost = g + stack_costs[from_stack_ind]
                      
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(new_state, colors)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, colors):
   # The heuristic function can be a simulation of sorting the blocks greedily, always transferring the block to the stack with the same color as the top block, if possible
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is transferred to a stack with a different color, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of blocks that can be transferred to the stack in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Iterate through the colors
   for color in colors:
       # Count the number of blocks of the current color in each stack
       color_counts = [sum(block == color for block in stack) for stack in state]
       # Sort the counts and the stacks together
       sorted_color_counts, sorted_stacks = zip(*sorted(zip(color_counts, state)))
       # Calculate the number of blocks that need to be moved to sort the stacks
       h += sum(max(0, count - 3) for count in sorted_color_counts)
   return h


print(a_star())
