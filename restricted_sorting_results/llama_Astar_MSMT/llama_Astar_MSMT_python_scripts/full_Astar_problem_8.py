
import heapq


def initialize():
   # Define the initial state of the stacks as a list of lists
   initial_state = [['Blue', 'Green', 'Green', 'Red'], ['Yellow', 'Yellow', 'Green', 'Yellow'], [], [], [], ['Red', 'Blue', 'Red', 'Blue']]
   num_stacks = 6
   stack_capacity = 4
   # Define the cost of moving one block to the top of each stack
   move_costs = {0: 3, 1: 6, 2: 1, 3: 7, 4: 2, 5: 3}


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_stacks, stack_capacity, move_costs, visited_costs, queue
  
def a_star():
  
   initial_state, num_stacks, stack_capacity, move_costs, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the state is the goal state, return the actions taken
       if all(len(stack) == 1 or len(stack) == 0 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring one block from a stack to another
       for from_stack_ind in range(num_stacks):
           for to_stack_ind in range(num_stacks):
               # Check if the transfer is valid, ie if the from_stack is not empty and the to_stack is either empty or has only blocks of the same shade
               if state[from_stack_ind] and (not state[to_stack_ind] or state[to_stack_ind][-1] == state[from_stack_ind][-1]):
                   # Generate the new state
                   new_state = [stack[:] for stack in state]
                   new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                   new_state = [stack[:] for stack in new_state]
                   # The cost so far is the number of transfers made, as our objective is to minimize the number of transfers required to sort the blocks
                   new_cost = g + 1
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[tuple(tuple(stack) for stack in new_state)] = new_cost
                       h = heuristic(new_state, move_costs)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, move_costs):
   # The heuristic function can be a simulation of moving blocks greedily, using the next most expensive stack as the destination stack for each block
   # This heuristic is admissible because it is greedy, always opting for the action that moves the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is moved to a less expensive stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of blocks that can be moved to a more expensive stack is by moving the blocks to the most expensive stack, which is exactly the stack used to move the blocks in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the stacks by decreasing cost of moving a block to the top
   stacks = sorted(range(len(state)), key=lambda i: move_costs[i], reverse=True)
   # Iterate through the stacks
   for i in range(len(state)):
       # Move the blocks from the current stack to the next most expensive stack
       while state[i]:
           # Find the next most expensive stack with a different shade of block or an empty stack
           for j in stacks:
               if j != i and (not state[j] or state[j][-1] != state[i][-1]):
                   # Move the block to the next most expensive stack
                   state[j].append(state[i].pop())
                   # Increment the estimated cost to the goal by 1 actions
                   h += 1
                   break
   return h


print(a_star())
