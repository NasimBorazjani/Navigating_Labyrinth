
import heapq


def a_star():
   # Define the initial state of the stacks, with each stack represented as a list of blocks
   initial_state = [['Red', 'Yellow', 'Blue', 'Yellow'], [], [], ['Green', 'Blue', 'Green', 'Red'], [], ['Yellow', 'Red', 'Green', 'Blue']]
   num_stacks = 6
   stack_capacity = 4
   # Define the cost of moving a block to the top of each stack
   stack_costs = {0: 4, 1: 5, 2: 3, 3: 3, 4: 3, 5: 5}


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If all stacks are sorted, return the actions taken
       if all(stack == sorted(stack) for stack in state if stack):
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from the top of one stack to another
       for i in range(num_stacks):
           for j in range(num_stacks):
               if i != j and state[i] and (not state[j] or state[i][-1] == state[j][-1]):
                   new_state = [stack[:] for stack in state]
                   new_state[j].append(new_state[i].pop())
                   new_state = tuple(tuple(stack) for stack in new_state)
                   new_cost = g + stack_costs[j]
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost, new_cost, actions + [(i, j)], new_state))
   return None


print(a_star())
