
import heapq


def initialize():
    # Define the initial state of the stacks as a list of lists
    initial_state = [[], [], ['Yellow', 'Yellow', 'Green', 'Black', 'Red'], ['Black', 'Green', 'Black', 'Blue', 'Yellow'], ['Green', 'Blue', 'Yellow', 'Red', 'Blue'], [], [], ['Black', 'Red', 'Green', 'Red', 'Blue']]
    num_stacks = 8
    stack_capacity = 5
    # Define the costs of moving one block to the top of each stack
    move_costs = {0: 7, 1: 2, 2: 1, 3: 1, 4: 9, 5: 4, 6: 2, 7: 7}

    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]
   
    return initial_state, num_stacks, stack_capacity, move_costs, visited_costs, queue
  
def a_star():
   
    initial_state, num_stacks, stack_capacity, move_costs, visited_costs, queue = initialize()

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # The goal state must be all stacks with 4 blocks of a single shade
        if all(len(stack) == 4 and len(set(stack)) == 1 for stack in state):
            return actions

        # Generate all possible actions from the current state, which includes transferring one block from a non-empty stack to an empty stack or a stack with only blocks of that shade
        for from_stack_ind, from_stack in enumerate(state):
            if from_stack:
                for to_stack_ind, to_stack in enumerate(state):
                    if len(to_stack) < stack_capacity and (not to_stack or to_stack[-1] == from_stack[-1]):
                        # Generate the new state
                        new_state = [list(stack[:]) for stack in state]
                        new_state[to_stack_ind].append(new_state[from_stack_ind].pop())
                        new_state = [tuple(stack) for stack in new_state]
                        # The additional cost of this state is the cost of moving one block from the from_stack to the to_stack
                        new_cost = g + move_costs[to_stack_ind]
                       
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            # The heuristic is the sum of the costs of moving all blocks to their final positions
                            h = heuristic(new_state, move_costs)
                            heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
   return None


def heuristic(state, move_costs):
    # The heuristic is the sum of the costs of moving all blocks to their final positions
    # This heuristic is admissible because it is a lower bound on the cost to reach the goal state
    # The heuristic is consistent because the cost of moving a block is always at least 1, and the cost of moving a block to its final position is always at least the cost of moving it to any other position
    h = 0
    for from_stack_ind, from_stack in enumerate(state):
        for block in from_stack:
            to_stack_ind = state.index(tuple(block for stack in state if block in stack))
            h += move_costs[to_stack_ind]
    return h


print(a_star())
