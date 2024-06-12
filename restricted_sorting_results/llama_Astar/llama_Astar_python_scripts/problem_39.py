
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = (['Green', 'Green', 'Black', 'Blue', 'Black'], [], [], [], ['Yellow', 'Red', 'Black', 'Red', 'Blue'], ['Yellow', 'Blue', 'Red', 'Black', 'Blue'], ['Red', 'Green', 'Green', 'Yellow', 'Yellow'], [])
   # Define the costs of moving one block to the top of each stack
   stack_costs = {0: 8, 1: 8, 2: 1, 3: 2, 4: 9, 5: 4, 6: 7, 7: 8}
   # Define the goal state, where each stack has 4 blocks of a single shade
   goal_state = (['Green', 'Green', 'Green', 'Green'], ['Black', 'Black', 'Black', 'Black'], ['Blue', 'Blue', 'Blue', 'Blue'], ['Red', 'Red', 'Red', 'Red'], ['Yellow', 'Yellow', 'Yellow', 'Yellow'])
   # Define the maximum capacity of each stack
   max_capacity = 5


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
                           # The heuristic is the sum of the differences between the current state and the goal state, for each stack
                           h = heuristic(state, goal_state, max_capacity)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], transfer_block(state, from_stack_ind, to_stack_ind)))


def transfer_block(state, from_stack_ind, to_stack_ind):
   # Generate the new state by transferring the top block from the from_stack to the to_stack
   new_state = [list(stack[:]) for stack in state]
   new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
   return tuple(tuple(stack) for stack in new_state)


def heuristic(state, goal_state, max_capacity):
   # The heuristic is the sum of the differences between the current state and the goal state, for each stack
   h = 0
   for from_stack_ind, from_stack in enumerate(state):
       goal_stack = goal_state[from_stack_ind]
       # If the from_stack is not empty
       if from_stack:
           # Calculate the difference between the current state and the goal state for the from_stack
           h += abs(len(from_stack) - max_capacity) + abs(from_stack[-1] != goal_stack[-1])
           # Calculate the difference between the current state and the goal state for the goal_stack
           h += abs(len(goal_stack) - max_capacity) + abs(from_stack[-1] != goal_stack[-1])
   return h


print(a_star())
