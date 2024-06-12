
import heapq


def initialize():
   # Define the initial state of the stacks as a list of lists
   initial_state = [['Blue', 'Yellow', 'Yellow', 'Green', 'Black'], [], [], [], ['Blue', 'Red', 'Black', 'Yellow', 'Green'], ['Black', 'Red', 'Green', 'Blue', 'Red'], ['Green', 'Yellow', 'Black', 'Red', 'Blue'], []]
   num_stacks = 8
   stack_capacity = 5
   # The cost of moving a block to the top of each stack
   move_costs = {0: 4, 1: 4, 2: 7, 3: 1, 4: 8, 5: 8, 6: 8, 7: 4}


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_stacks, stack_capacity, move_costs, visited_costs, queue
  
def a_star():
  
   initial_state, num_stacks, stack_capacity, move_costs, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the state is correctly sorted, return the actions taken
       if all(len(stack) == 1 or (len(stack) == stack_capacity and len(set(stack)) == 1) for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from the top of one stack to an empty stack or to a stack that has only blocks of that shade
       for from_stack_ind in range(num_stacks):
           for to_stack_ind in range(num_stacks):
               # Check if the transfer is valid, ie if the from_stack is not empty and the to_stack is not full and has the same color block on top or is empty
               if state[from_stack_ind] and (not state[to_stack_ind] or state[to_stack_ind][-1] == state[from_stack_ind][-1]) and len(state[to_stack_ind]) < stack_capacity:
                   new_state = [list(stack[:]) for stack in state]
                   # Perform the transfer
                   new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                   # The new state must be a 2d tuple
                   new_state = [tuple(stack) for stack in new_state]
                   new_state = tuple(new_state)
                   # The cost so far is the number of actions taken, as the task is to minimize the cost of sorting the blocks
                   new_cost = g + move_costs[from_stack_ind]
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The heuristic is the sum of the costs of moving the blocks in the current state to their correct stacks
                       h = heuristic(state, move_costs)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, move_costs):
   # The heuristic function can be the sum of the costs of moving the blocks in the current state to their correct stacks
   # This heuristic is admissible because it is a lower bound on the cost to reach the goal state
   # The heuristic is consistent because the cost of moving a block is always at least 1, and the cost of moving a block to the top of each stack is always at least 1
   h = sum(move_costs[from_stack_ind] for from_stack_ind in range(len(state)) if state[from_stack_ind])
   return h


print(a_star())
