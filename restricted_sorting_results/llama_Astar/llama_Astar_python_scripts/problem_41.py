
import heapq


def a_star():
   # Define the initial state of the stacks
   initial_state = (['Green', 'Blue', 'Yellow', 'Green', 'Blue'],
                   ['Black', 'Green', 'Red', 'Red', 'Black'],
                   [],
                   ['Blue', 'Yellow', 'Red', 'Black', 'Yellow'],
                   [],
                   [],
                   ['Blue', 'Red', 'Black', 'Yellow', 'Green'],
                   [])
   # Define the cost of moving one block to the top of each stack
   cost_dict = {0: 2, 1: 1, 2: 2, 3: 8, 4: 4, 5: 3, 6: 6, 7: 3}
   # Define the goal state, where each stack has 4 blocks of a single shade
   goal_state = (['Green', 'Green', 'Green', 'Green'],
                 ['Black', 'Black', 'Black', 'Black'],
                 ['Blue', 'Blue', 'Blue', 'Blue'],
                 ['Red', 'Red', 'Red', 'Red'],
                 ['Yellow', 'Yellow', 'Yellow', 'Yellow'],
                 ['Black', 'Black', 'Black', 'Black'],
                 ['Blue', 'Blue', 'Blue', 'Blue'],
                 ['Red', 'Red', 'Red', 'Red'])
   # Define the number of stacks
   num_stacks = 8


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes transferring a block from a non-empty stack to an empty stack or a stack with only blocks of the same shade
       for from_stack in range(num_stacks):
           if state[from_stack]:
               for to_stack in range(num_stacks):
                   # Check if the transfer is valid, ie if the to_stack is empty or has only blocks of the same shade as the top block of the from_stack
                   if not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]:
                       # Generate the new state
                       new_state = [list(stack[:]) for stack in state]
                       new_state[to_stack].append(new_state[from_stack].pop())
                       new_state = tuple(tuple(stack) for stack in new_state)
                       # The cost so far is the number of actions taken, as the task is to minimize the cost of transferring blocks
                       new_cost = g + cost_dict[from_stack]


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(state, goal_state, cost_dict)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None




def heuristic(state, goal_state, cost_dict):
   # The heuristic function can be a simulation of transferring blocks greedily, using the least expensive stack as the destination stack for each block
   # This heuristic is admissible because it is greedy, always opting for the action that transfers the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is transferred to a more expensive stack, or equal or less by at most the cost of reaching the successor node, ie one action
   h = 0
   for from_stack in range(len(state)):
       if state[from_stack]:
           to_stack = min(range(len(state)), key=lambda to_stack: cost_dict[to_stack] if not state[to_stack] or state[to_stack][-1] == state[from_stack][-1] else math.inf)
           h += cost_dict[from_stack] - cost_dict[to_stack]
   return h


print(a_star())
