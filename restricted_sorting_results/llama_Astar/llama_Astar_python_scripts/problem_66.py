
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = ([], [], ['White', 'Black', 'Green', 'White', 'Green', 'Blue'], ['Red', 'Green', 'Black', 'Red', 'White', 'Yellow'], [], ['Yellow', 'Black', 'Yellow', 'Red', 'Green', 'White'], [], ['White', 'Blue', 'Red', 'Red', 'Blue', 'Black'], [], ['Yellow', 'Blue', 'Yellow', 'Blue', 'Green', 'Black'])
   # Define the cost of moving one block to the top of each stack
   cost_dict = {0: 4, 1: 5, 2: 2, 3: 10, 4: 6, 5: 8, 6: 2, 7: 11, 8: 2, 9: 8}
   # Define the maximum capacity of each stack
   capacity = 6
   # Define the goal state, where each stack has 5 blocks of a single shade
   goal_state = (['White', 'White', 'White', 'White', 'White'], ['Black', 'Black', 'Black', 'Black', 'Black'], ['Green', 'Green', 'Green', 'Green', 'Green'], ['Red', 'Red', 'Red', 'Red', 'Red'], ['Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow'], ['Blue', 'Blue', 'Blue', 'Blue', 'Blue'])
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
               if state[from_stack] and (not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]) and len(state[to_stack]) < capacity:
                   # Generate the new state
                   new_state = [list(stack[:]) for stack in state]
                   new_state[to_stack].append(new_state[from_stack].pop())
                   new_state = tuple(tuple(stack) for stack in new_state)
                   # Calculate the cost of the new state
                   new_cost = g + cost_dict[from_stack]
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # Calculate the heuristic
                       h = heuristic(new_state, goal_state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None




def heuristic(state, goal_state):
   # The heuristic is the sum of the differences between the number of blocks in each stack in the current state and the goal state
   # This heuristic is admissible because it is a lower bound on the cost to reach the goal state
   # The heuristic is consistent because the cost of moving a block is always at least 1
   h = 0
   for i in range(len(state)):
       h += abs(len(state[i]) - len(goal_state[i]))
   return h


print(a_star())
