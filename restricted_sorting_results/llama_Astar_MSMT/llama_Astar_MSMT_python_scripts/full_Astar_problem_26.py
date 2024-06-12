
import heapq


def initialize():
   # Define the initial state of the stacks as a 2d tuple
   initial_state = (('Blue', 'Yellow', 'Red', 'Yellow'),
                   ('Green', 'Red', 'Green', 'Red'),
                   ('Blue', 'Green', 'Blue', 'Yellow'),
                   (), (), ())
   # Define the cost of moving one block to the top of each stack
   stack_costs = {0: 4, 1: 4, 2: 7, 3: 7, 4: 5, 5: 6}
   # Create the set of the valid block shades
   shades = set(['Blue', 'Yellow', 'Red', 'Green'])


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, stack_costs, shades, visited_costs, queue
  
def a_star():
  
   initial_state, stack_costs, shades, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must have all the blocks correctly sorted
       if all(len(stack) == 3 and len(set(stack)) == 1 for stack in state):
           return actions


       # If the state is not the goal state, generate all possible actions from the current state, which includes moving one block from a non-empty stack to an empty stack or to a stack that has only blocks of that shade
       for from_stack_ind, from_stack in enumerate(state):
           if from_stack:
               for to_stack_ind, to_stack in enumerate(state):
                   if not to_stack or to_stack[-1] == from_stack[-1]:
                       # Generate the new state
                       new_state = [list(stack[:]) for stack in state]
                       block = new_state[from_stack_ind].pop()
                       new_state[to_stack_ind].append(block)
                       new_state = tuple(tuple(stack) for stack in new_state)
                       # The additional cost of this state is the cost of moving the block
                       new_cost = g + stack_costs[from_stack_ind]
                      
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is the sum of the costs of moving the blocks to their correct stacks
                           h = heuristic(new_state, stack_costs)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, stack_costs):
   # The heuristic is the sum of the costs of moving the blocks to their correct stacks
   h = 0
   for from_stack_ind, from_stack in enumerate(state):
       if from_stack:
           to_stack_ind = from_stack[-1]
           h += stack_costs[from_stack_ind]
   return h


print(a_star())
