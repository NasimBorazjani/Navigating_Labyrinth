
import heapq

def initialize():
    # Define the initial state of the stacks as a list of lists
    initial_state = [[], [], ['Blue', 'Blue', 'Green', 'Black', 'Red'], [], ['Red', 'Green', 'Red', 'Black', 'Yellow'], [], ['Blue', 'Yellow', 'Green', 'Yellow', 'Black'], ['Yellow', 'Green', 'Black', 'Red', 'Blue']]
    # Define the capacities of the stacks
    capacities = [5, 5, 5, 5, 5, 5, 5, 5]
    # Define the costs of moving one block to the top of each stack
    costs = {0: 6, 1: 2, 2: 7, 3: 1, 4: 1, 5: 5, 6: 3, 7: 2}
    # Initialize the visited_costs dictionary and the priority queue
    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0
    queue = [(0, 0, [], initial_state)]
    return initial_state, capacities, costs, visited_costs, queue

def a_star():
    initial_state, capacities, costs, visited_costs, queue = initialize()
    while queue:
        _, g, actions, state = heapq.heappop(queue)
        # The goal state is when all stacks are sorted by shade with 4 blocks of a single shade in each non-empty stack
        if all(len(stack) == 0 or (len(stack) == 4 and stack[0] == stack[1] == stack[2] == stack[3]) for stack in state):
            return actions
        # Generate all possible actions from the current state
        for from_stack_ind, from_stack in enumerate(state):
            if from_stack:
                from_block = from_stack.pop()
                for to_stack_ind, to_stack in enumerate(state):
                    if len(to_stack) < capacities[to_stack_ind] and (not to_stack or to_stack[-1] == from_block):
                        # The cost of the new state is the cost of moving the block from the from_stack to the to_stack
                        new_cost = g + costs[to_stack_ind]
                        new_state = [stack[:] for stack in state]
                        new_state[to_stack_ind].append(from_block)
                        new_state[from_stack_ind] = from_stack
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[tuple(tuple(stack) for stack in new_state)] = new_cost
                            heapq.heappush(queue, (new_cost + heuristic(new_state, capacities), new_cost, actions + [(from_stack_ind, to_stack_ind)], new_state))
    return None

def heuristic(state, capacities):
    # The heuristic function can be a simulation of moving blocks greedily, using the least cost stack as the destination stack for each block
    h = 0
    for from_stack_ind, from_stack in enumerate(state):
        for block in from_stack:
            min_cost = float('inf')
            for to_stack_ind, to_stack in enumerate(state):
                if len(to_stack) < capacities[to_stack_ind] and (not to_stack or to_stack[-1] == block):
                    cost = costs[to_stack_ind]
                    if cost < min_cost:
                        min_cost = cost
            h += min_cost
    return h

print(a_star())
