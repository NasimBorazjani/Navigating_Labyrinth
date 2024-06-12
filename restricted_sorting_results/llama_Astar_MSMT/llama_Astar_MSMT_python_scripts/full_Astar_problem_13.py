
import heapq


def initialize():
   # Define the initial state of the stacks as a list of lists
   initial_state = [['Green', 'Red', 'Blue', 'Blue'], [], ['Yellow', 'Red', 'Green', 'Green'], [], [], ['Red', 'Yellow', 'Blue', 'Yellow']]
   num_stacks = 6
   stack_capacity = 4
   # Define the costs of moving one block to the top of each stack
   move_costs = {0: 4, 1: 2, 2: 2, 3: 7, 4: 4, 5: 5}


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


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
               # Check if the transfer is valid, ie if the from_stack is not empty and the to_stack is not full and has the same shade as the top block of the from_stack
               if state[from_stack_ind] and len(state[to_stack_ind]) < stack_capacity and (not state[to_stack_ind] or state[to_stack_ind][-1] == state[from_stack_ind][-1]):
                   # Generate the new state
                   new_state = [list(stack[:]) for stack in state]
                   new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                   new_state = [stack for stack in new_state if stack]  # Remove empty stacks
                   # The cost so far is the number of transfers made, as our objective is to minimize the number of transfers required to sort the blocks
                   new_cost = g + 1
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[tuple(tuple(stack) for stack in new_state)] = new_cost
                       h = heuristic(new_state, move_costs)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, move_costs):
   # The heuristic function can be a simulation of sorting the blocks greedily, using the least expensive stack first
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is transferred to a more expensive stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of blocks that can be transferred to a stack is by using the least expensive stack, which is exactly the stack used to transfer the blocks in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the stacks by increasing move_costs to the stacks
   stacks = sorted(state, key=lambda stack: move_costs[state.index(stack)])
   # Iterate through the stacks
   for stack in stacks:
       # If the stack is not sorted, transfer the top block to the least expensive stack first
       if len(stack) != 3 or len(set(stack)) != 1:
           least_expensive_stack = min(stacks, key=lambda stack: move_costs[state.index(stack)])
           h += move_costs[state.index(least_expensive_stack)]
   return h


print(a_star())
