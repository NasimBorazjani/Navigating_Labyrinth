
import heapq


def initialize():
   # Define the initial state of the stacks as a list of lists
   initial_state = [['Black', 'Green', 'Red', 'Yellow', 'Black'], [], ['Blue', 'Red', 'Black', 'Black', 'Yellow'], ['Green', 'Red', 'Yellow', 'Blue', 'Green'], [], [], ['Green', 'Blue', 'Red', 'Yellow', 'Blue'], []]
   num_stacks = 8
   stack_capacity = 5
   # Define the cost of moving one block to the top of each stack
   move_costs = {0: 4, 1: 4, 2: 1, 3: 9, 4: 7, 5: 8, 6: 9, 7: 7}
   # Create the set of the valid colors that could be in the stacks
   colors = set(['Black', 'Green', 'Red', 'Yellow', 'Blue'])


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_stacks, stack_capacity, move_costs, colors, visited_costs, queue
  
def a_star():
  
   initial_state, num_stacks, stack_capacity, move_costs, colors, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must have all stacks sorted with 4 blocks of a single shade
       if all(len(stack) == 4 and len(set(stack)) == 1 for stack in state if stack):
           return actions


       # Generate all possible actions from the current state, which includes transferring one block from the top of a stack to an empty stack or to a stack that has only blocks of that shade, without exceeding the stacks’ capacity
       for from_stack_ind, from_stack in enumerate(state):
           if from_stack:
               from_color = from_stack[-1]
               for to_stack_ind, to_stack in enumerate(state):
                   if len(to_stack) < stack_capacity and (not to_stack or to_stack[-1] == from_color):
                       # Generate the new state
                       new_state = [list(stack[:]) for stack in state]
                       new_state[from_stack_ind].pop()
                       new_state[to_stack_ind].append(from_color)
                       # The additional cost of this state is the cost of moving one block
                       new_cost = g + move_costs[from_stack_ind]
                      
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[tuple(tuple(stack) for stack in new_state)] = new_cost
                           # The heuristic is the sum of the costs of moving all blocks to their final positions
                           h = heuristic(new_state, colors, move_costs)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, colors, move_costs):
   # The heuristic is the sum of the costs of moving all blocks to their final positions
   # This heuristic is admissible because it is a lower bound on the cost to reach the goal state
   # The heuristic is consistent as the cost of moving a block is always at least 1
   # The heuristic is also safe, as it never overestimates the cost to reach the goal state

   h = 0
   for from_stack_ind, from_stack in enumerate(state):
       for block in from_stack:
           to_stack_ind = None
           # Find the stack to which the block can be transferred
           for i, stack in enumerate(state):
               if i != from_stack_ind and (not stack or stack[-1] == block):
                   to_stack_ind = i
                   break
           # Add the cost of moving the block to its final position
           h += move_costs[to_stack_ind]
   return h


print(a_star())
