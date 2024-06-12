
import heapq


def a_star():
    # Define the initial state of the stacks, where each stack is represented as a list of blocks
    initial_state = [[], [], [], [], ['Pink', 'Red', 'Green', 'Pink', 'White', 'Blue', 'Yellow'], [], ['Yellow', 'White', 'Yellow', 'Blue', 'Yellow', 'Black', 'White'], ['Black', 'Green', 'Pink', 'Pink', 'Green', 'Yellow', 'Green'], ['White', 'Blue', 'Red', 'Red', 'Red', 'Yellow', 'Black'], ['Black', 'Blue', 'Blue', 'Pink', 'Red', 'White', 'Green'], [], ['Blue', 'Black', 'Black', 'White', 'Red', 'Green', 'Pink']]
    num_stacks = 12
    stack_capacity = 7
    # Define the cost of moving a block to the top of each stack
    stack_costs = {0: 12, 1: 3, 2: 11, 3: 5, 4: 11, 5: 13, 6: 2, 7: 2, 8: 12, 9: 4, 10: 2, 11: 10}

    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if all stacks are sorted
        if all(all(state[i][j] == state[i][0] for j in range(len(state[i]))) for i in range(num_stacks) if state[i]):
            return actions

        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for i in range(num_stacks):
            for j in range(num_stacks):
                if i != j and state[i] and (not state[j] or state[j][-1] == state[i][0]):
                    new_state = [list(stack[:]) for stack in state]
                    new_state[j].append(new_state[i].pop(0))
                    new_state = tuple(tuple(stack) for stack in new_state)
                    new_cost = g + stack_costs[j]

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost, new_cost, actions + [(i, j)], new_state))

    return None


print(a_star())
