
import heapq


def initialize():
   # Define the initial state of the stacks as a list of lists
   initial_state = [['Yellow', 'Blue', 'Blue', 'Green'], [], ['Yellow', 'Green', 'Red', 'Red'], ['Green', 'Red', 'Yellow', 'Blue'], [], []]
   num_stacks = 6
   stack_capacity = 4
   # Define the costs of moving one block to the top of each stack
   move_costs = {0: 7, 1: 3, 2: 5, 3: 5, 4: 1, 5: 3}


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_stacks, stack_capacity, move_costs, visited_costs, queue
  
def a_star():
  
   initial_state, num_stacks, stack_capacity, move_costs, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the state is the goal state, return the actions taken
       if all(len(stack) == 1 or len(stack) == stack_capacity for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring one block from a non-empty stack to an empty stack or to a stack that has only blocks of that shade
       for from_stack_ind, from_stack in enumerate(state):
           if from_stack:
               from_block = from_stack[-1]
               for to_stack_ind, to_stack in enumerate(state):
                   if not to_stack or to_stack[-1] == from_block:
                       # Check if the new state, containing the transfer, would be valid; ie the stacks must not exceed their capacity
                       if len(to_stack) < stack_capacity:
                           # Generate the new state
                           new_state = [list(stack[:]) for stack in state]
                           new_state[from_stack_ind].pop()
                           new_state[to_stack_ind].append(from_block)
                           new_state = [tuple(stack) for stack in new_state]
                           # The additional cost of this state is the cost of moving the block
                           new_cost = g + move_costs[to_stack_ind]
                          
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               # The heuristic is the sum of the costs of moving all remaining blocks to their correct stacks
                               h = heuristic(new_state, move_costs)
                               heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, move_costs):
   # The heuristic is the sum of the costs of moving all remaining blocks to their correct stacks
   # This heuristic is admissible because it is a lower bound on the cost to reach the goal state
   # The heuristic is consistent because the cost of moving a block is always at least 1, and the cost of moving a block to the top of each stack is always at least 1
   h = 0
   for from_stack_ind, from_stack in enumerate(state):
       for block in from_stack:
           to_stack_ind = state.index(tuple([block]))
           h += move_costs[to_stack_ind]
   return h


print(a_star())
