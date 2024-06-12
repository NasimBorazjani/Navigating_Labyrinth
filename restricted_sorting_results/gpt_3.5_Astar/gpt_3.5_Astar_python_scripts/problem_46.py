
import heapq


def a_star():
    # Define the initial state of the stacks, with each stack represented as a list of blocks
    initial_state = [[], [], [], ['Yellow', 'Black', 'Yellow', 'Black', 'Green'], ['Red', 'Yellow', 'Blue', 'Black', 'Black'], [], ['Red', 'Blue', 'Green', 'Red', 'Blue'], ['Green', 'Blue', 'Red', 'Yellow', 'Green']]
    num_stacks = 8
    stack_capacity = 5
    # Define the cost of moving a block to the top of each stack
    stack_costs = {0: 2, 1: 1, 2: 6, 3: 3, 4: 1, 5: 5, 6: 4, 7: 2}
    # Define the goal state, which is when all stacks are sorted by shade
    goal_state = [[], [], [], ['Black', 'Black', 'Green', 'Yellow', 'Yellow'], ['Black', 'Blue', 'Red', 'Yellow', 'Yellow'], [], ['Blue', 'Blue', 'Green', 'Red', 'Red'], ['Blue', 'Green', 'Green', 'Red', 'Yellow']]

    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if all(stack == goal_stack for stack, goal_stack in zip(state, goal_state)):
            return actions

        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                # Check if transferring a block from the 'from_stack' to the 'to_stack' is a valid action
                if from_stack != to_stack and state[from_stack] and (not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]) and len(state[to_stack]) < stack_capacity:
                    new_state = [stack[:] for stack in state]
                    new_state[from_stack] = new_state[from_stack][:-1]
                    new_state[to_stack].append(state[from_stack][-1])
                    new_state = tuple(tuple(stack) for stack in new_state)
                    # Calculate the cost of the new state
                    new_cost = g + stack_costs[from_stack]

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack, to_stack)], new_state))

    return None


print(a_star())
