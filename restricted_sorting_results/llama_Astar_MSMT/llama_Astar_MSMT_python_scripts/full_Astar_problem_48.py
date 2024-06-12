
import heapq


def initialize():
   # Define the initial state of the stacks as a list of lists
   initial_state = [[], ['Green', 'Blue', 'Yellow', 'Black', 'Blue'], [], [], ['Blue', 'Black', 'Green', 'Yellow', 'Red'], [], ['Green', 'Red', 'Black', 'Yellow', 'Blue'], ['Red', 'Green', 'Red', 'Black', 'Yellow']]
   # Define the capacities of the stacks
   capacities = [5, 5, 5, 5, 5, 5, 5, 5]
   # Define the cost of moving one block to the top of each stack
   cost_dict = {0: 2, 1: 4, 2: 5, 3: 2, 4: 2, 5: 3, 6: 2, 7: 5}


   visited_costs = {}
   visited_costs[tuple(tuple(row) for row in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, capacities, cost_dict, visited_costs, queue
  
def a_star():
  
   initial_state, capacities, cost_dict, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must be that all stacks have 4 blocks of a single shade
       if all(len(stack) == 4 and len(set(stack)) == 1 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from one stack to another
       for from_stack_index, from_stack in enumerate(state):
           if from_stack:
               for to_stack_index, to_stack in enumerate(state):
                   if len(to_stack) < capacities[to_stack_index] and (not to_stack or to_stack[-1] == from_stack[-1]):
                       # Generate the new state
                       new_state = [list(stack[:]) for stack in state]
                       new_state[from_stack_index].pop()
                       new_state[to_stack_index].append(from_stack[-1])
                       new_state = [tuple(stack) for stack in new_state]
                       # The cost of the new state is the cost of moving the block plus the cost so far
                       new_cost = g + cost_dict[to_stack_index]
                      
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(new_state, capacities)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_index, to_stack_index)], new_state))
   return None




def heuristic(state, capacities):
   # The heuristic function can be a simulation of moving blocks greedily, using the next block of the most filled stack as long as it can be placed in the current stack
   # This heuristic is admissible because it is greedy, always opting for the action that moves the most blocks, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is removed from a stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of blocks that can be added to a stack is by using the next block of the most filled stack, which is exactly the block used to fill the stack in the heuristic. Thus h(n) can never be greater than c(n, n’) + h(n’)
   h = 0
   # Sort the stacks by their size
   stacks = sorted(state, key=len, reverse=True)
   # Iterate through the stacks
   for i in range(len(stacks)):
       # If the stack is not full, fill it with the next block from the most filled stack
       if len(stacks[i]) < capacities[i] and i < len(stacks) - 1:
           next_block = stacks[i + 1].pop(0)
           stacks[i].append(next_block)
           # Increment the estimated cost to the goal by 1 actions
           h += 1
   return h


print(a_star())
