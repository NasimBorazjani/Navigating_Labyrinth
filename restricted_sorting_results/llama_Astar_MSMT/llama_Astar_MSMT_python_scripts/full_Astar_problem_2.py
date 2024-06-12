
import heapq


def initialize():
   # Define the initial state of the stacks as a list of lists
   initial_state = [['Red', 'Green', 'Red', 'Blue'], ['Red', 'Yellow', 'Yellow', 'Green'], [], ['Blue', 'Yellow', 'Green', 'Blue'], [], []]
   num_stacks = 6
   stack_capacity = 4
   # The cost of moving one block to the top of each stack
   move_costs = {0: 5, 1: 3, 2: 3, 3: 1, 4: 3, 5: 2}


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_stacks, stack_capacity, move_costs, visited_costs, queue
  
def a_star():
  
   initial_state, num_stacks, stack_capacity, move_costs, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the state is the goal state, return the actions taken
       if all(len(stack) == 1 or len(stack) == 0 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from one stack to another
       for from_stack in range(num_stacks):
           for to_stack in range(num_stacks):
               # Check if the transfer is valid, ie if the from_stack is not empty and the to_stack is either empty or has only blocks of the same shade as the top block of the from_stack
               if state[from_stack] and (not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]):
                   # Generate the new state
                   new_state = [stack[:] for stack in state]
                   new_state[to_stack].append(new_state[from_stack].pop())
                   new_state = [stack for stack in new_state if stack]
                   # The cost so far is the number of actions taken, as the task is to minimize the cost of the actions
                   new_cost = g + move_costs[from_stack]
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[tuple(tuple(stack) for stack in new_state)] = new_cost
                       h = heuristic(new_state, move_costs)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None




def heuristic(state, move_costs):
   # The heuristic function can be a simulation of moving blocks greedily, using the next most expensive stack as the destination stack for each block
   # This heuristic is admissible because it is greedy, always opting for the action that moves the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is moved to a less expensive stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum cost of moving a block is by moving it to the least expensive stack, which is exactly the stack used to move the block in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the stacks by decreasing cost
   stacks = sorted(range(len(state)), key=lambda i: move_costs[i], reverse=True)
   # Iterate through the stacks
   for i in range(len(state)):
       # Move the blocks from the current stack to the next most expensive stack
       while state[i]:
           h += move_costs[stacks[i]]
           state[stacks[i]].append(state[i].pop())
   return h


print(a_star())
