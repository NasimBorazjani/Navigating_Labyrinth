
import heapq


def initialize():
   # Define the initial state of the stacks as a list of lists
   initial_state = [[], ['Blue', 'Red', 'Blue', 'Red'], [], ['Green', 'Green', 'Green', 'Red'], ['Yellow', 'Yellow', 'Yellow', 'Blue'], []]
   # Define the cost of moving one block to the top of each stack
   stack_costs = {0: 3, 1: 6, 2: 3, 3: 2, 4: 1, 5: 1}
   # Define the maximum capacity of each stack
   stack_capacity = 4
   # Define the goal state of the stacks, where each stack has 3 blocks of a single shade
   goal_state = [['Blue', 'Blue', 'Blue'], ['Red', 'Red', 'Red'], ['Green', 'Green', 'Green'], ['Yellow', 'Yellow', 'Yellow']]


   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, stack_costs, stack_capacity, goal_state, visited_costs, queue
  
def a_star():
  
   initial_state, stack_costs, stack_capacity, goal_state, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which involves transferring a block from one stack to another
       for from_stack_ind, from_stack in enumerate(state):
           if from_stack:
               for to_stack_ind, to_stack in enumerate(state):
                   # Check if transferring a block from the from_stack to the to_stack is valid, ie the to_stack is not full and the shade of the top block in the from_stack is the same as the shade of the top block in the to_stack
                   if len(to_stack) < stack_capacity and (not to_stack or to_stack[-1] == from_stack[-1]):
                       new_state = [list(stack[:]) for stack in state]
                       # Perform the transfer
                       new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                       # Calculate the cost of the new state
                       new_cost = g + stack_costs[from_stack_ind]
                      
                       if new_state not in visited_costs or new_cost < visited_costs[tuple(tuple(stack) for stack in new_state)]:
                           visited_costs[tuple(tuple(stack) for stack in new_state)] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None




def heuristic(state, goal):
   # The heuristic function can be a simulation of the transfer process, using the block with the most blocks in the same shade as the goal block
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is removed from a stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of blocks that can be added to a stack is by moving the block from the stack with the most blocks in the same shade, which is exactly the block used to fill the stack in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       # Sort the blocks in the stack by the number of blocks in the same shade
       stack = sorted(state[i], key=lambda x: len([block for block in state[i] if block == x]))
       # Calculate the difference between the goal state and the current state
       for block in stack:
           goal_blocks = [block for block in goal[i] if block == block]
           # Increment the estimated cost to the goal by the difference between the goal state and the current state
           h += len(goal_blocks) - len([block for block in state[i] if block == block])
   return h


print(a_star())
