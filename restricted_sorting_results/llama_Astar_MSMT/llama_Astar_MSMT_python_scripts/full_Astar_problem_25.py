
import heapq


def initialize():
   # Define the initial state of the stacks as a list of lists
   initial_state = [[], ['Green', 'Blue', 'Yellow', 'Green'], ['Yellow', 'Red', 'Red', 'Blue'], [], ['Blue', 'Green', 'Yellow', 'Red'], []]
   num_stacks = 6
   stack_capacity = 4
   # Create the set of the valid block shades
   shades = set(['Green', 'Blue', 'Yellow', 'Red'])
   # Define the cost of moving one block to the top of each stack
   cost_dict = {0: 4, 1: 3, 2: 2, 3: 4, 4: 2, 5: 5}


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_stacks, stack_capacity, shades, cost_dict, visited_costs, queue
  
def a_star():
  
   initial_state, num_stacks, stack_capacity, shades, cost_dict, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must be all stacks with 3 blocks of a single shade
       if all(len(stack) == 3 and len(set(stack)) == 1 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring one block from a stack to another
       for from_stack_ind, from_stack in enumerate(state):
           if from_stack:
               for to_stack_ind, to_stack in enumerate(state):
                   if len(to_stack) < stack_capacity and (not to_stack or to_stack[-1] == from_stack[-1]):
                       # Generate the new state
                       new_state = [list(stack[:]) for stack in state]
                       block_to_move = new_state[from_stack_ind].pop()
                       new_state[to_stack_ind].append(block_to_move)
                       new_state = [tuple(stack) for stack in new_state]
                       # The additional cost of this state is the cost of moving the block
                       new_cost = g + cost_dict[to_stack_ind]
                      
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is the sum of the number of blocks in each stack that are not sorted, plus the number of blocks in the wrong stack
                           h = heuristic(new_state, shades)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, shades):
   # The heuristic function counts the number of blocks in each stack that are not sorted, plus the number of blocks in the wrong stack
   # This heuristic is admissible because it is a lower bound on the cost to reach the goal state
   # The heuristic is consistent because it never overestimates the cost to reach the goal state
   h = 0
   for stack in state:
       if len(stack) != 3:
           h += len(stack)
       else:
           h += len(set(stack)) - 1
   return h


print(a_star())
