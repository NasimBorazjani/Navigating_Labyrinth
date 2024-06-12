
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = ([], ['Yellow', 'White', 'Blue', 'Yellow', 'Red', 'White'], [], [], ['Blue', 'Blue', 'Green', 'Black', 'Black', 'Red'], ['Black', 'Green', 'Yellow', 'Yellow', 'Blue', 'Black'], [], ['White', 'Blue', 'Green', 'White', 'Yellow', 'Red'], [], ['Green', 'White', 'Black', 'Red', 'Green', 'Red'])
   # Define the costs of moving one block to the top of each stack
   costs = {0: 3, 1: 6, 2: 3, 3: 6, 4: 9, 5: 6, 6: 6, 7: 10, 8: 2, 9: 5}
   # Define the capacities of the stacks
   capacities = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
   # Define the goal state, where each stack has 5 blocks of a single shade
   goal_state = (['Blue', 'Blue', 'Blue', 'Blue', 'Blue'], ['Green', 'Green', 'Green', 'Green', 'Green'], ['Red', 'Red', 'Red', 'Red', 'Red'], ['White', 'White', 'White', 'White', 'White'], ['Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow'])
   # Initialize the visited costs
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize the priority queue
   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state
       for from_stack in range(len(state)):
           for to_stack in range(len(state)):
               # Check if the action is valid
               if state[from_stack] and (not state[to_stack] or state[from_stack][-1] == state[to_stack][-1]) and len(state[to_stack]) < capacities[to_stack]:
                   # Generate the new state
                   new_state = [list(stack[:]) for stack in state]
                   new_state[to_stack].append(new_state[from_stack].pop())
                   new_state = tuple(tuple(stack) for stack in new_state)
                   # The cost of the new state is the cost of the action
                   new_cost = g + costs[from_stack]
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The heuristic is the sum of the costs of moving all the blocks to the goal state
                       h = heuristic(new_state, goal_state, capacities, costs)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None




def heuristic(state, goal_state, capacities, costs):
   # The heuristic is the sum of the costs of moving all the blocks to the goal state
   h = 0
   for from_stack in range(len(state)):
       for block in state[from_stack]:
           # Find the stack in the goal state that the block should be moved to
           for to_stack in range(len(goal_state)):
               if goal_state[to_stack] and goal_state[to_stack][-1] == block:
                   # Add the cost of moving the block to the goal state
                   h += costs[to_stack]
   return h


print(a_star())
