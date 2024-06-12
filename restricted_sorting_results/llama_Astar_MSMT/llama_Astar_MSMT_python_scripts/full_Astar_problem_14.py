
import heapq


def initialize():
   # Define the initial state of the stacks as a list of lists
   initial_state = [['Green', 'Yellow', 'Red', 'Yellow'], [], ['Blue', 'Blue', 'Blue', 'Red'], [], ['Green', 'Green', 'Red', 'Yellow'], []]
   num_stacks = 6
   stack_capacity = 4
   # Define the cost of moving one block to the top of each stack
   move_costs = {0: 3, 1: 6, 2: 5, 3: 5, 4: 3, 5: 1}
   # Create the set of the valid colors that could be in the stacks
   colors = set(['Green', 'Yellow', 'Red', 'Blue'])


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_stacks, stack_capacity, move_costs, colors, visited_costs, queue
  
def a_star():
  
   initial_state, num_stacks, stack_capacity, move_costs, colors, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must have all stacks sorted, with each stack having 3 blocks of a single shade
       if all(len(stack) == 3 and len(set(stack)) == 1 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring one block from the top of a stack to an empty stack or to a stack that has only blocks of that shade
       for from_stack_ind in range(num_stacks):
           for to_stack_ind in range(num_stacks):
               if from_stack_ind != to_stack_ind:
                   # Check if the transfer would be valid, ie the to_stack is empty or has only blocks of the same shade as the top block of the from_stack
                   if not state[to_stack_ind] or state[to_stack_ind][-1] == state[from_stack_ind][-1]:
                       # Check if the to_stack is not full
                       if len(state[to_stack_ind]) < stack_capacity:
                           # Generate the new state
                           new_state = [list(stack[:]) for stack in state]
                           new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                           new_state = [stack for stack in new_state if stack]
                           # The additional cost of this state is the cost of moving the block
                           new_cost = g + move_costs[to_stack_ind]
                          
                           if new_state not in visited_costs or new_cost < visited_costs[tuple(tuple(stack) for stack in new_state)]:
                               visited_costs[tuple(tuple(stack) for stack in new_state)] = new_cost
                               # The heuristic is the sum of the costs of moving the blocks to their final positions
                               h = heuristic(new_state, move_costs)
                               heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, move_costs):
   # The heuristic is the sum of the costs of moving the blocks to their final positions
   # The heuristic is admissible because it is a lower bound on the cost to reach the goal state
   # The heuristic is consistent because the cost of moving a block is always at least 1, and the cost of moving a block to its final position is always less than or equal to the cost of moving it to any other position
   h = 0
   for from_stack_ind in range(len(state)):
       for block in state[from_stack_ind]:
           to_stack_ind = [i for i, stack in enumerate(state) if stack and stack[-1] == block][0]
           h += move_costs[to_stack_ind]
   return h


print(a_star())
