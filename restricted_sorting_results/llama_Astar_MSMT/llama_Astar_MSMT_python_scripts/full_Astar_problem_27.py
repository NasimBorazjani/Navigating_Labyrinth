
import heapq


def initialize():
   # Define the initial state of the stacks as a list of lists
   initial_state = [['Red', 'Blue', 'Green', 'Yellow'], ['Blue', 'Blue', 'Green', 'Red'], [], [], [], ['Green', 'Red', 'Yellow', 'Yellow']]
   num_stacks = 6
   stack_capacity = 4
   # Define the costs of moving one block to the top of each stack
   move_costs = {0: 3, 1: 6, 2: 2, 3: 4, 4: 6, 5: 5}


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_stacks, stack_capacity, move_costs, visited_costs, queue
  
def a_star():
  
   initial_state, num_stacks, stack_capacity, move_costs, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If all stacks are sorted, return the actions taken
       if all(len(stack) == 1 or (len(stack) <= stack_capacity and len(set(stack)) == 1) for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring one block from a non-empty stack to an empty stack or a stack with only blocks of that shade
       for from_stack_ind, from_stack in enumerate(state):
           if from_stack:
               for to_stack_ind, to_stack in enumerate(state):
                   if not to_stack or to_stack[-1] == from_stack[-1]:
                       # Check if the new state, containing the transfer, would be valid; ie the stacks must not exceed their capacities and the transfer must not exceed the cost limit
                       if len(to_stack) < stack_capacity and g + move_costs[to_stack_ind] <= visited_costs[tuple(tuple(stack) for stack in state)]:
                           # Generate the new state
                           new_state = [list(stack[:]) for stack in state]
                           new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                           new_state = [stack for stack in new_state if stack]
                           new_state = [[]] * (num_stacks - len(new_state)) + new_state
                           # The additional cost of this state is the cost of moving the block
                           new_cost = g + move_costs[to_stack_ind]
                          
                           if tuple(tuple(new_stack) for new_stack in new_state) not in visited_costs or new_cost < visited_costs[tuple(tuple(new_stack) for new_stack in new_state)]:
                               visited_costs[tuple(tuple(new_stack) for new_stack in new_state)] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state, move_costs), new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, move_costs):
   # The heuristic function can be a simulation of moving blocks greedily, using the next most cost-effective stack as the destination stack for each block
   # This heuristic is admissible because it is greedy, always opting for the action that moves the blocks the most cost-effectively, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is moved to a more expensive stack, or equal or less by at most the cost of reaching the successor node, ie one action
   h = 0
   # Sort the stacks by the cost of moving a block to the top of each stack
   stacks = sorted(state, key=lambda stack: move_costs[state.index(stack)])
   # Iterate through the stacks
   for i in range(len(stacks)):
       # If the stack is not empty
       if stacks[i]:
           # Move the block to the top of the next most cost-effective stack
           while stacks[i]:
               # Find the next most cost-effective stack
               for j in range(i + 1, len(stacks)):
                   if stacks[j] and stacks[j][-1] == stacks[i][-1]:
                       stacks[j].append(stacks[i].pop())
                       # Increment the estimated cost to the goal by 1 action
                       h += 1
                       break
   return h


print(a_star())
