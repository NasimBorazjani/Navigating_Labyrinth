
import heapq


def initialize():
   # Define the initial state of the stacks as a list of lists
   initial_state = [[], ['Green', 'Red', 'Yellow', 'Blue'], [], ['Red', 'Blue', 'Yellow', 'Green'], ['Red', 'Yellow', 'Blue', 'Green'], []]
   num_stacks = 6
   stack_capacity = 4
   # Define the costs of moving one block to the top of each stack
   move_costs = {0: 4, 1: 2, 2: 5, 3: 2, 4: 4, 5: 1}


   visited_costs = {}
   visited_costs[tuple(tuple(row) for row in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_stacks, stack_capacity, move_costs, visited_costs, queue
  
def a_star():
  
   initial_state, num_stacks, stack_capacity, move_costs, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must have all stacks sorted, with each stack having 3 blocks of a single shade
       if all(len(stack) == 3 and len(set(stack)) == 1 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring one block from a stack to another
       for from_stack_ind in range(num_stacks):
           for to_stack_ind in range(num_stacks):
               # Check if the transfer is valid, ie if the to_stack is not full, and if the from_stack is not empty
               if len(state[to_stack_ind]) < stack_capacity and len(state[from_stack_ind]) > 0:
                   # Generate the new state
                   new_state = [list(stack[:]) for stack in state]
                   # Remove the top block from the from_stack and add it to the to_stack
                   new_state[from_stack_ind].pop()
                   new_state[to_stack_ind].append(state[from_stack_ind][-1])
                   new_state = [tuple(stack) for stack in new_state]
                   # The cost so far is the number of transfers made, as our objective is to minimize the number of transfers required to sort the blocks
                   new_cost = g + 1
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(new_state, stack_capacity)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, stack_capacity):
   # The heuristic function can be a simulation of sorting the blocks greedily, always transferring the block that would result in the most sorted stacks
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is transferred to a stack that is not sorted, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of blocks that can be sorted in the heuristic is by transferring the block that would result in the most sorted stacks
   h = 0
   # Iterate through the stacks
   for i in range(len(state)):
       # Sort the blocks in the stack by shade
       state[i].sort()
       # Calculate the number of blocks that would need to be transferred to sort the stack
       h += abs(len(state[i]) - stack_capacity)
   return h


print(a_star())
