
import heapq


def initialize():
   # Define the initial state of the stacks as a list of lists
   initial_state = [[], ['Blue', 'Yellow', 'Blue', 'Yellow'], [], [], ['Red', 'Blue', 'Yellow', 'Green'], ['Green', 'Green', 'Red', 'Red']]
   num_stacks = 6
   stack_capacity = 4
   # Define the cost of moving one block to the top of each stack
   move_costs = {0: 1, 1: 4, 2: 2, 3: 7, 4: 6, 5: 6}


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_stacks, stack_capacity, move_costs, visited_costs, queue
  
def a_star():
  
   initial_state, num_stacks, stack_capacity, move_costs, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the state is the goal state, return the actions taken
       if all(len(stack) == 3 and len(set(stack)) == 1 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring one block from a stack to another
       for from_stack in range(num_stacks):
           for to_stack in range(num_stacks):
               # Check if the transfer is valid, ie if the from_stack is not empty and the to_stack is either empty or has only blocks of the same shade as the top block of the from_stack
               if state[from_stack] and (not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]):
                   # Generate the new state
                   new_state = [list(stack[:]) for stack in state]
                   new_state[to_stack].append(new_state[from_stack].pop())
                   new_state = [stack for stack in new_state if stack]
                   # The cost so far is the number of actions taken, as the task is to minimize the cost of transferring blocks
                   new_cost = g + move_costs[from_stack]
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[tuple(tuple(stack) for stack in new_state)] = new_cost
                       h = heuristic(new_state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None




def heuristic(state):
   # The heuristic is the sum of the costs of moving the remaining blocks to their final positions, assuming that the blocks are moved to the stacks with the lowest cost first
   # This heuristic is admissible because it is a lower bound on the cost to reach the goal state
   # The heuristic is consistent because the cost of moving a block to a stack is always at least 1, and the cost of moving a block to a stack with a higher cost is higher or equal to the cost of moving it to a stack with a lower cost
   h = 0
   for stack in state:
       for block in stack:
           # Find the index of the stack that will have the same shade of block at the top after this transfer
           to_stack = state.index([block] + [b for b in stack if b != block])
           h += move_costs[to_stack]
   return h


print(a_star())
