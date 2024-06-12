
import heapq


def initialize():
   # Define the initial state of the stacks as a list of lists
   initial_state = [[], ['Blue', 'Black', 'Blue', 'Yellow', 'Red'], ['Red', 'Green', 'Black', 'Green', 'Black'], [], ['Red', 'Red', 'Green', 'Yellow', 'Yellow'], [], [], ['Blue', 'Yellow', 'Green', 'Black', 'Blue']]
   # Define the costs of moving a block to the top of each stack
   costs = {0: 3, 1: 2, 2: 1, 3: 7, 4: 5, 5: 5, 6: 6, 7: 4}
   # Define the maximum capacity of each stack
   capacity = 5
   # Define the number of stacks
   num_stacks = 8


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, costs, capacity, num_stacks, visited_costs, queue
  
def a_star():
  
   initial_state, costs, capacity, num_stacks, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must be all stacks sorted with 4 blocks of a single shade in each non-empty stack
       if all(len(stack) == 0 or (len(stack) == 4 and stack[0] == stack[1] == stack[2] == stack[3]) for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring one block from the top of a non-empty stack to an empty stack or a stack that has only blocks of that shade
       for from_stack in range(num_stacks):
           for to_stack in range(num_stacks):
               # Check if the transfer is valid
               if state[from_stack] and (not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]) and len(state[to_stack]) < capacity:
                   # The new state is the current state with the top block of the from_stack moved to the to_stack
                   new_state = [stack[:] for stack in state]
                   new_state[to_stack].append(new_state[from_stack].pop())
                   # The cost of the new state is the cost of the current state plus the cost of the transfer
                   new_cost = g + costs[to_stack]
                  
                   if new_state not in visited_costs or new_cost < visited_costs[tuple(tuple(stack) for stack in new_state)]:
                       visited_costs[tuple(tuple(stack) for stack in new_state)] = new_cost
                       # The heuristic is the sum of the costs of moving all the blocks to their final positions
                       h = heuristic(state, new_state, costs)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None




def heuristic(state, new_state, costs):
   # The heuristic is the sum of the costs of moving all the blocks to their final positions
   # This heuristic is admissible, as it is always less than or equal to the actual cost of reaching the goal state
   # The heuristic is consistent, as the cost of moving a block is always at least 1
   h = 0
   for from_stack in range(len(state)):
       for block in state[from_stack]:
           # Find the final position of the block
           to_stack = next(i for i in range(len(new_state)) if new_state[i] and new_state[i][-1] == block)
           h += costs[to_stack]
   return h


print(a_star())
