
import heapq


def initialize():
   # Define the initial state of the stacks as a list of lists
   initial_state = [['Green', 'Yellow', 'Yellow', 'Green'], ['Red', 'Red', 'Blue', 'Yellow'], [], [], ['Blue', 'Red', 'Blue', 'Green'], []]
   # Define the cost of moving one block to the top of each stack
   cost_dict = {0: 2, 1: 2, 2: 3, 3: 7, 4: 1, 5: 7}
   # Define the maximum capacity of each stack
   capacity = 4


   visited_costs = {}
   visited_costs[tuple(tuple(row) for row in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, cost_dict, capacity, visited_costs, queue
  
def a_star():
  
   initial_state, cost_dict, capacity, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the state is the goal state, return the actions taken
       if all(len(stack) == 1 or len(stack) == 0 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from one stack to another
       for from_stack_ind, from_stack in enumerate(state):
           if from_stack:
               from_stack_top = from_stack[-1]
               for to_stack_ind, to_stack in enumerate(state):
                   if not to_stack or to_stack[-1] == from_stack_top:
                       # Check if the new state, after the transfer, would be valid; ie the stacks must not exceed their capacity
                       if len(to_stack) < capacity:
                           new_state = [list(stack[:]) for stack in state]
                           new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                           new_state = [tuple(stack) for stack in new_state]
                           # The additional cost of this state is the cost of the transfer
                           new_cost = g + cost_dict[to_stack_ind]
                          
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               # The heuristic is the sum of the number of blocks in each stack that are not sorted
                               h = heuristic(new_state)
                               heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state):
   # The heuristic is the sum of the number of blocks in each stack that are not sorted
   return sum(len(stack) for stack in state if len(stack) != 1 and len(stack) != 0)


print(a_star())
