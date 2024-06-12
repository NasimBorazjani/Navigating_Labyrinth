
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = ([], ['Green', 'Red', 'Yellow', 'Blue'], [], ['Red', 'Blue', 'Yellow', 'Green'], ['Red', 'Yellow', 'Blue', 'Green'], [])
   # Define the cost of moving one block to the top of each stack
   stack_costs = {0: 4, 1: 2, 2: 5, 3: 2, 4: 4, 5: 1}
   # Define the goal state, where each stack has 3 blocks of a single shade
   goal_state = (['Green'], ['Red'], ['Yellow'], ['Blue'], [], [])
   # Define the maximum capacity of each stack
   stack_capacity = 4


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from a non-empty stack to an empty stack or a stack with only blocks of the same shade
       for from_stack_ind, from_stack in enumerate(state):
           if from_stack:
               for to_stack_ind, to_stack in enumerate(state):
                   # Check if the transfer is valid, ie if the to_stack is empty or has only blocks of the same shade as the top block of the from_stack
                   if not to_stack or to_stack[-1] == from_stack[-1]:
                       # The cost of the new state is the cost of moving the block from the from_stack to the to_stack
                       new_cost = g + stack_costs[from_stack_ind]


                       if new_cost < visited_costs.get((from_stack_ind, to_stack_ind), math.inf):
                           visited_costs[(from_stack_ind, to_stack_ind)] = new_cost
                           # Generate the new state
                           new_state = [list(stack[:]) for stack in state]
                           new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                           new_state = tuple(tuple(stack) for stack in new_state)
                           # The heuristic is the sum of the differences between the current state and the goal state, considering the cost of moving each block to its correct stack
                           h = heuristic(state, goal_state, stack_costs)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, goal_state, stack_costs):
   # The heuristic is the sum of the differences between the current state and the goal state, considering the cost of moving each block to its correct stack
   # This heuristic is admissible because it is a lower bound on the cost to reach the goal state
   # The heuristic is consistent because the cost of moving a block to its correct stack is always at least 1, which is exactly the decrease in the heuristic value
   h = 0
   for from_stack_ind, from_stack in enumerate(state):
       for block in from_stack:
           # Find the index of the goal stack that has the same shade as the block
           to_stack_ind = next(i for i, goal_stack in enumerate(goal_state) if goal_stack and goal_stack[-1] == block)
           # Add the cost of moving the block to its correct stack to the heuristic
           h += stack_costs[from_stack_ind]
   return h


print(a_star())
