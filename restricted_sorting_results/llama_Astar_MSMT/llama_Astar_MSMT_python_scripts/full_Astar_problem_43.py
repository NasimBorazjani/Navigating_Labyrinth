
import heapq


def initialize():
   # Define the initial state of the stacks as a list of lists
   initial_state = [['Green', 'Green', 'Red', 'Blue', 'Red'], ['Black', 'Red', 'Black', 'Red', 'Green'], ['Yellow', 'Green', 'Black', 'Black', 'Blue'], [], ['Blue', 'Yellow', 'Blue', 'Yellow', 'Yellow'], [], [], []]
   # Define the costs of moving a block from one stack to another
   move_costs = {0: 5, 1: 2, 2: 8, 3: 7, 4: 5, 5: 6, 6: 1, 7: 1}
   # Define the capacities of the stacks
   capacities = [5, 5, 5, 5, 5, 5, 5, 5]
   # Define the colors of the blocks
   colors = ['Green', 'Red', 'Blue', 'Black', 'Yellow']
   # Define the number of stacks
   num_stacks = 8
   # Define the maximum number of blocks that can be in a stack
   max_blocks = 4


   visited_costs = {}
   visited_costs[tuple(tuple(row) for row in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, move_costs, capacities, colors, num_stacks, max_blocks, visited_costs, queue
  
def a_star():
  
   initial_state, move_costs, capacities, colors, num_stacks, max_blocks, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state is when all stacks have 4 blocks of a single shade
       if all(len(stack) == max_blocks and len(set(stack)) == 1 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from one stack to another
       for from_stack in range(num_stacks):
           for to_stack in range(num_stacks):
               # Check if the transfer is valid, ie if the from_stack is not empty and the to_stack is not full and has the same shade as the top block of the from_stack
               if state[from_stack] and len(state[to_stack]) < capacities[to_stack] and (not state[to_stack] or state[from_stack][-1] == state[to_stack][-1]):
                   # Generate the new state
                   new_state = [list(stack[:]) for stack in state]
                   new_state[to_stack].append(new_state[from_stack].pop())
                   # The cost of the new state is the cost of transferring the block plus the cost so far
                   new_cost = g + move_costs[from_stack] + (0 if not state[to_stack] else move_costs[to_stack])
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[tuple(tuple(row) for row in new_state)] = new_cost
                       h = heuristic(new_state, colors, capacities, max_blocks)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None




def heuristic(state, colors, capacities, max_blocks):
   # The heuristic function can be a simulation of moving blocks greedily, using the next most abundant color as the block to move, provided the stack to move to is not full and has the same color
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is moved to a stack that is not full but has a different color, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of blocks that can be in a stack is by moving the block to the stack with the same color, which is exactly the block used to fill the stack in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the colors by their frequency in the stacks
   colors = sorted(colors, key=lambda color: sum(stack.count(color) for stack in state))
   # Iterate through the stacks
   for i in range(len(state)):
       # Fill the stack with the next most abundant color as long as the stack is not full and has the same color
       while len(state[i]) < capacities[i] and state[i] and state[i][-1] == colors[-1]:
           # Increment the estimated cost to the goal by 1 actions
           h += 1
           # Move the block from the stack to the top of the next most abundant color stack
           for j in range(len(state)):
               if state[j] and state[j][-1] == colors[-1]:
                   state[j].pop()
                   state[i].append(colors[-1])
   return h


print(a_star())
