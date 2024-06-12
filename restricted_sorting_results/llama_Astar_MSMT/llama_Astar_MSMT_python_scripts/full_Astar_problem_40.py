
import heapq

def initialize():
    # Define the initial state of the stacks as a list of lists
    initial_state = [[],[],[['Green', 'Yellow', 'Black', 'Red', 'Black']],[['Black', 'Red', 'Yellow', 'Blue', 'Yellow'], ['Green', 'Blue', 'Blue', 'Red', 'Black']],[],[['Red', 'Green', 'Blue', 'Green', 'Yellow']]]
    num_stacks = 8
    stack_capacity = 5
    block_costs = {0: 5, 1: 5, 2: 1, 3: 7, 4: 7, 5: 9, 6: 1, 7: 6}
    # Create the set of the valid block types that could be in the stacks
    block_types = set(['Green', 'Yellow', 'Black', 'Red', 'Blue'])

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    queue = [(0, 0, [], str(initial_state))]
   
    return initial_state, num_stacks, stack_capacity, block_costs, block_types, visited_costs, queue
  
def a_star():
   
    initial_state, num_stacks, stack_capacity, block_costs, block_types, visited_costs, queue = initialize()

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # The goal state must have all stacks sorted, with a maximum of 4 blocks of the same shade in each non-empty stack
        if all(len(stack) <= 4 and (len(stack) == 0 or len(set(stack)) == 1) for stack in state):
            return actions

        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                # Check if the transfer is valid, ie if the top block of the from_stack is not the same as the top block of the to_stack
                if state[from_stack] and (not state[to_stack] or state[from_stack][-1] != state[to_stack][-1]):
                    # The number of the block to be transferred is the number of the top block in the from_stack
                    num_to_transfer = state[from_stack][-1]
                    # Generate the new state
                    new_state = [list(stack[:]) for stack in state]
                    new_state[from_stack].pop()
                    new_state[to_stack].append(num_to_transfer)
                    new_state = [tuple(stack) for stack in new_state]
                    # The cost of the action is the cost of moving the block to the top of the to_stack
                    new_cost = g + block_costs[to_stack]
                   
                    if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                        visited_costs[str(new_state)] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, block_types), new_cost, actions + [(from_stack, to_stack)], new_state))
   return None


def heuristic(state, block_types):
   # The heuristic function can be a simulation of transferring blocks greedily, using the most expensive stack as the destination for each block type
   # This heuristic is admissible because it is greedy, always opting for the action that transfers the blocks to the most expensive stack, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a block is transferred to a less expensive stack, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum cost of transferring a block is by using the most expensive stack that won't cause exceeding the stack's capacity

   h = 0
   # Calculate the remaining capacity of each stack
   remaining_capacity = [stack_capacity - len(stack) for stack in state]
   # Iterate through the block types
   for block_type in block_types:
       # Find the most expensive stack with remaining capacity for each block type
       max_cost = 0
       for stack_ind in range(len(state)):
           if any(block == block_type for block in state[stack_ind]):
               max_cost = max(max_cost, block_costs[stack_ind])
       # The heuristic is the sum of the maximum cost of transferring a block of the current type to the most expensive stack with remaining capacity
       h += max_cost
   return h


print(a_star())
