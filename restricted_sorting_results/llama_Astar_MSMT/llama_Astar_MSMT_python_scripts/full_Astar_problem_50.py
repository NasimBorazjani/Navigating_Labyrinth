
import heapq


def initialize():
   # Define the initial state of the stacks as a list of lists
   initial_state = [[], [], ['Blue', 'Green', 'Black', 'Blue', 'Red'], ['Green', 'Red', 'Blue', 'Black', 'Blue'], [], ['Red', 'Green', 'Yellow', 'Yellow', 'Black'], ['Green', 'Black', 'Red', 'Yellow', 'Yellow'], []]
   num_stacks = 8
   stack_capacity = 5
   block_colors = ['Blue', 'Green', 'Black', 'Red', 'Yellow']
   # Define the cost of moving one block to the top of each stack
   move_costs = {0: 1, 1: 3, 2: 3, 3: 8, 4: 7, 5: 9, 6: 8, 7: 8}


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_stacks, stack_capacity, block_colors, move_costs, visited_costs, queue
  
def a_star():
  
   initial_state, num_stacks, stack_capacity, block_colors, move_costs, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the state is the goal state, return the actions taken
       if all(len(stack) == 4 and len(set(stack)) == 1 for stack in state):
           return actions


       # Generate all possible actions from the current state
       for from_stack_ind in range(num_stacks):
           for to_stack_ind in range(num_stacks):
               # Check if moving a block from the from_stack to the to_stack is valid
               if from_stack_ind != to_stack_ind and (len(state[to_stack_ind]) < stack_capacity or (len(state[to_stack_ind]) == stack_capacity and state[to_stack_ind][-1] == state[from_stack_ind][-1])):
                   new_state = [list(stack[:]) for stack in state]
                   new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                   # The new state must be mapped to a 2d tuple
                   new_state = [tuple(stack) for stack in new_state]
                   new_state = tuple(new_state)
                   # The cost of the new state is the cost to move the block plus the cost to reach the current state
                   new_cost = g + move_costs[to_stack_ind]
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The heuristic is the sum of the costs of moving the remaining blocks in each stack to their correct position
                       h = heuristic(new_state, block_colors)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, block_colors):
   # The heuristic is the sum of the costs of moving the remaining blocks in each stack to their correct position
   # The cost of moving a block from a stack to the correct position is the number of blocks in the stack times the cost of moving the block to the top of the stack
   # The cost of moving a block to the top of the stack is the cost of moving it to the top of the correct position stack
   h = 0
   for stack_ind, stack in enumerate(state):
       if stack:
           color = stack[-1]
           h += len(stack) * move_costs[stack_ind]
           for other_stack_ind, other_stack in enumerate(state):
               if other_stack and other_stack[-1] == color:
                   h -= len(other_stack) * move_costs[other_stack_ind]
   return h


print(a_star())
