
import heapq

def initialize():
   # Define the initial state of the stacks as a list of lists
   initial_state = [[], [], ['Green', 'Yellow', 'Green', 'Red'], ['Green', 'Red', 'Blue', 'Yellow'], [], ['Blue', 'Red', 'Yellow', 'Blue']]
   # Define the cost of moving one block to the top of each stack
   cost_dict = {0: 5, 1: 1, 2: 6, 3: 7, 4: 7, 5: 7}
   # Define the goal state, where each stack has 3 blocks of a single shade
   goal_state = [['Green', 'Green', 'Green'], ['Yellow', 'Yellow', 'Yellow'], ['Red', 'Red', 'Red'], ['Blue', 'Blue', 'Blue']]
   num_stacks = 6

   visited_costs = {}
   visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

   queue = [(0, 0, [], initial_state)]
  
   return initial_state, cost_dict, goal_state, num_stacks, visited_costs, queue
  
def a_star():
   initial_state, cost_dict, goal_state, num_stacks, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heapq.heappop(queue)

       # If the state is the goal state
       if state == goal_state:
           return actions

       # Generate all possible actions from the current state
       for from_stack in range(num_stacks):
           for to_stack in range(num_stacks):
               # Check if the action is valid
               if from_stack != to_stack and len(state[to_stack]) < 3 and (len(state[from_stack]) == 0 or state[to_stack][-1] == state[from_stack][-1]):
                   # Perform the action
                   new_state = [list(stack[:]) for stack in state]
                   new_state[to_stack].append(new_state[from_stack].pop())
                   new_state = [stack for stack in new_state if stack]  # Remove empty stacks
                   # Calculate the cost of the new state
                   new_cost = g + cost_dict[to_stack]
                  
                   if tuple(tuple(stack) for stack in new_state) not in visited_costs or new_cost < visited_costs[tuple(tuple(stack) for stack in new_state)]:
                       visited_costs[tuple(tuple(stack) for stack in new_state)] = new_cost
                       h = heuristic(new_state, goal_state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None

def heuristic(state, goal_state):
   # The heuristic function can be a simulation of moving blocks greedily, using the next smallest block as long as the stack does not exceed its capacity
   # This heuristic is admissible because it is greedy, always opting for the action that moves the blocks the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is removed from a stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of blocks that can be added to the stack is by using the smallest block that won't cause an overflow, which is exactly the block used to fill the stack in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(i + 1, len(state)):
           if state[i] and state[j] and state[i][-1] == state[j][-1]:
               while len(state[j]) < 3:
                   state[j].append(state[i].pop())
                   h += 1
   return h

print(a_star())
