
import heapq

def initialize():
   # Define the initial state of the stacks as a list of lists
   initial_state = [['Green', 'Green', 'Black', 'Blue', 'Black'], [], [], [], ['Yellow', 'Red', 'Black', 'Red', 'Blue'], ['Yellow', 'Blue', 'Red', 'Black', 'Blue'], ['Red', 'Green', 'Green', 'Yellow', 'Yellow'], []]
   num_stacks = 8
   stack_capacity = 5
   # The cost of moving one block to the top of each stack
   move_costs = {0: 8, 1: 8, 2: 1, 3: 2, 4: 9, 5: 4, 6: 7, 7: 8}
   # The color of the block at the top of each stack
   stack_tops = ['Green', 'Green', 'Black', 'Blue', 'Black', 'Yellow', 'Red', 'Black', 'Red', 'Blue', 'Yellow', 'Blue', 'Red', 'Green', 'Green', 'Yellow', 'Yellow']

   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_stacks, stack_capacity, move_costs, stack_tops, visited_costs, queue
  
def a_star():
  
   initial_state, num_stacks, stack_capacity, move_costs, stack_tops, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the state is the goal state, return the actions taken
       if all(len(stack) == 4 and len(set(stack)) == 1 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from one stack to another
       for from_stack in range(num_stacks):
           for to_stack in range(num_stacks):
               # Check if the action is valid
               if len(state[from_stack]) > 0 and (len(state[to_stack]) < stack_capacity or (len(state[to_stack]) == stack_capacity and state[to_stack][-1] == state[from_stack][-1])):
                   # Perform the action
                   new_state = [list(stack[:]) for stack in state]
                   new_state[to_stack].append(new_state[from_stack].pop())
                   new_state = [tuple(stack) for stack in new_state]
                   # The cost so far is the number of actions taken
                   new_cost = g + move_costs[from_stack]
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The heuristic is the sum of the costs to move the blocks to their correct stacks
                       h = heuristic(new_state, stack_tops, move_costs)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None




def heuristic(state, stack_tops, move_costs):
   # The heuristic is the sum of the costs to move the blocks to their correct stacks
   h = 0
   for i in range(len(state)):
       if len(state[i]) > 0:
           color = state[i][-1]
           if color != stack_tops[i]:
               h += move_costs[i]
   return h


print(a_star())
