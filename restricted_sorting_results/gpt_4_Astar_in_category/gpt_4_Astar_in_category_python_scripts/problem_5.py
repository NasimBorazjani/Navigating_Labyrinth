
import heapq
from collections import Counter


def a_star():
   # Define the initial state of the stacks, as a 2d tuple of color of the blocks in stacks 0 to 5
   initial_state = (('Red', 'Green', 'Green', 'Yellow'), (), ('Blue', 'Blue', 'Green', 'Red'), (), ('Blue', 'Yellow', 'Red', 'Yellow'), ())
  
   # Encoding other variables given in the problem statement
   num_stacks = 6
   capacity = 4
   stack_costs = {0: 4, 1: 1, 2: 7, 3: 3, 4: 2, 5: 2}


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check of the current state is the goal state
       # The goal state is where each stack only contains blocks of 1 single color
       if all(len(set(stack)) <= 1 for stack in state):
           return actions


       # Generate all possible actions from the current state, which includes moving a block from any of the 6 stacks to another stack
       for from_stack_ind in range(num_stacks):
           for to_stack_ind in range(num_stacks):
               # Check if the new state would be valid, ie from_stack and to_stack must not be the same stack
               # And from_stack must at least have 1 block to move and the to_stack cannot be at capacity
               if from_stack_ind != to_stack_ind and state[from_stack_ind] and len(state[to_stack_ind]) < capacity:
                   # Generate the new state
                   new_state = [list(stack[:]) for stack in state]
                   # The block to move is the topmost block in the from_stack, at index 0
                   block_to_move = new_state[from_stack_ind].pop(0)
                   # Add the block to the top of the to_stack
                   new_state[to_stack_ind].insert(0, block_to_move)
                   new_state = tuple(tuple(stack) for stack in new_state)
                   # The cost so far is the cost of moving a block to the to_stack
                   new_cost = g + stack_costs[to_stack_ind]


                   # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state), g + 1, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None


def heuristic(stacks):
   # An admissible and consistent heuristic for this problem is the count of blocks that are not the same color as the most frequent color in their stack
   # This heuristic relaxes the constraint that only the block at the top of the stack can be moved
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched block must be moved at least once
   # It's consistent because moving a block from one stack to another reduces the heuristic cost of the successor node by a max of 1 (if the moved block's color matches the most common color in the new stack but not in the old one), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for stack in stacks:
       if stack:
           # If there are ties in the frequency of colors, the most_common_color must be match the color of the blocks lower that are in the stack, as moving lower blocks is costlier          
           reversed_stack = stack[:]
           reversed_stack = reversed_stack[::-1]
           # Get the most common color
           most_common_color = Counter(reversed_stack).most_common(1)[0][0]
           for block in stack:
               if block != most_common_color:
                   h += 1
   return h


print(a_star())
