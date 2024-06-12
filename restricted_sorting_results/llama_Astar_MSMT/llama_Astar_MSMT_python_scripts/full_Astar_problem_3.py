
import heapq


def initialize():
   # Define the initial state of the stacks as a list of lists
   initial_state = [[], ['Yellow', 'Green', 'Red', 'Red'], ['Blue', 'Green', 'Red', 'Green'], ['Yellow', 'Blue', 'Yellow', 'Blue'], [], []]
   num_stacks = 6
   stack_capacity = 4
   # Define the costs of moving one block to the top of each stack
   move_costs = {0: 3, 1: 6, 2: 5, 3: 6, 4: 1, 5: 1}
   # Create the set of the valid block shades
   shades = set(['Yellow', 'Green', 'Red', 'Blue'])


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_stacks, stack_capacity, move_costs, shades, visited_costs, queue
  
def a_star():
  
   initial_state, num_stacks, stack_capacity, move_costs, shades, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must have all stacks sorted, with each stack having 3 blocks of a single shade
       if all(len(stack) == 3 and len(set(stack)) == 1 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring one block from the top of a stack to an empty stack or to a stack that has only blocks of that shade
       for from_stack_ind, from_stack in enumerate(state):
           if from_stack:
               for to_stack_ind, to_stack in enumerate(state):
                   if len(to_stack) < stack_capacity and (not to_stack or to_stack[-1] == from_stack[-1]):
                       # Generate the new state
                       new_state = [list(stack[:]) for stack in state]
                       new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                       new_state = [tuple(stack) for stack in new_state]
                       # The additional cost of this state is the cost of moving the block
                       new_cost = g + move_costs[to_stack_ind]
                      
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # Relaxing the constraints on the stacks to calculate the heuristic
                           h = heuristic(new_state, shades)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, shades):
   # Relax the stacks constraints to compute an admissible and consistent heuristic
   # This heuristic considers the sum of the costs of moving the blocks to the goal state, where each stack is sorted with 3 blocks of a single shade
   # The heuristic assumes that the blocks can be moved to the goal state with the minimum cost, even if the stacks are not sorted yet, thus reporting a lower cost estimate to reach the goal state, making it admissible
   # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of moving a block is always at least 1
   # Also the cost of the goal state is 0, as the stacks are sorted with 3 blocks of a single shade


   h = 0
   for stack in state:
       if len(stack) != 3 or len(set(stack)) != 1:
           # Calculate the cost of moving the blocks to the goal state
           for block in stack:
               h += move_costs[shades.index(block)]
   return h


print(a_star())
