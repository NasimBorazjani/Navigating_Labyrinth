
import heapq


def a_star():
    # Define the initial state of the stacks, with each stack represented as a list of blocks
    initial_state = [[], [], ['Blue', 'Blue', 'Blue', 'Green', 'Black', 'Red'], [], ['Red', 'Black', 'Blue', 'White', 'Blue', 'Yellow'], ['Yellow', 'White', 'Green', 'Black', 'Yellow', 'Red'], [], [], ['White', 'Black', 'White', 'White', 'Black', 'Red'], ['Red', 'Green', 'Green', 'Yellow', 'Yellow', 'Green']]
    num_stacks = 10
    stack_capacity = 6
    # Define the cost of moving a block to the top of each stack
    stack_costs = {0: 3, 1: 10, 2: 9, 3: 8, 4: 8, 5: 7, 6: 6, 7: 9, 8: 2, 9: 8}

    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if all stacks are sorted
        if all(sorted(stack) == stack for stack in state if stack):
            return actions

        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for i in range(num_stacks):
            for j in range(num_stacks):
                if i != j and state[i] and (not state[j] or state[i][-1] == state[j][-1]):
                    new_state = [list(stack) for stack in state]
                    new_state[i] = new_state[i][:-1]
                    new_state[j].append(state[i][-1])
                    new_state = tuple(tuple(stack) for stack in new_state)
                    new_cost = g + max(1, stack_costs[j])

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost, new_cost, actions + [(i, j)], new_state))

    return None


print(a_star())
