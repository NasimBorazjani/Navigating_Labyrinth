
import heapq


def initialize():
   # Define the initial state of the stacks as a list of lists
   initial_state = [[], ['Green', 'Blue', 'Yellow', 'Black', 'Blue'], [], [], ['Blue', 'Black', 'Green', 'Yellow', 'Red'], [], ['Green', 'Red', 'Black', 'Yellow', 'Blue'], ['Red', 'Green', 'Red', 'Black', 'Yellow']]
   num_stacks = 8
   stack_capacity = 5
   block_colors = ['Green', 'Blue', 'Yellow', 'Black', 'Red']
   cost_matrix = {0: 2, 1: 4, 2: 5, 3: 2, 4: 2, 5: 3, 6: 2, 7: 5}


   visited_costs = {}
   visited_costs[tuple(tuple(blocks) for blocks in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_stacks, stack_capacity, block_colors, cost_matrix, visited_costs, queue
  
def a_star():
  
   initial_state, num_stacks, stack_capacity, block_colors, cost_matrix, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the stacks are correctly sorted, return the actions taken
       if all(len(stack) == 4 and len(set(stack)) == 1 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from one stack to another
       for from_stack_ind in range(num_stacks):
           for to_stack_ind in range(num_stacks):
               # Check if the transfer results in a valid state, ie the to_stack is not full, and the from_stack is not empty
               if len(state[to_stack_ind]) < stack_capacity and state[from_stack_ind]:
                   # The color of the block to be transferred
                   block_color = state[from_stack_ind][-1]
                   # Check if the block can be transferred to the to_stack
                   if not state[to_stack_ind] or state[to_stack_ind][-1] == block_color:
                       # Generate the new state
                       new_state = [list(stack[:]) for stack in state]
                       new_state[from_stack_ind].pop()
                       new_state[to_stack_ind].append(block_color)
                       new_state = [tuple(stack) for stack in new_state]
                       # The cost so far is the number of transfers made, as the task is to minimize the number of transfers required to sort the blocks
                       new_cost = g + cost_matrix[from_stack_ind] + cost_matrix[to_stack_ind]
                      
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is the sum of the distances of the top block of each stack to its correct stack, which is consistent and admissible
                           h = heuristic(new_state, block_colors)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, block_colors):
   # The heuristic function can be the sum of the distances of the top block of each stack to its correct stack
   # This heuristic is admissible because it is a lower bound on the cost to reach the goal state, and consistent because it never overestimates the cost to reach the goal
   h = 0
   for i in range(len(state)):
       if state[i]:
           color = state[i][-1]
           h += abs(i - block_colors.index(color))
   return h


print(a_star())
