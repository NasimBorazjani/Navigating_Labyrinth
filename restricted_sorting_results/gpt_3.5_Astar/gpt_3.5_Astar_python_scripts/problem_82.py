
import heapq


def a_star():
    # Define the initial state of the stacks
    initial_state = [['Red', 'Black', 'Yellow', 'Black', 'White', 'Blue', 'White'], [], ['White', 'Blue', 'Green', 'Yellow', 'Blue', 'Yellow', 'Pink'], ['Yellow', 'Red', 'Pink', 'Green', 'Black', 'Red', 'White'], [], ['Pink', 'Red', 'Green', 'Green', 'Green', 'Black', 'Blue'], ['Pink', 'Blue', 'Blue', 'Black', 'Red', 'Pink', 'Black'], ['Yellow', 'Red', 'Pink', 'White', 'White', 'Yellow', 'Green'], [], [], [], []]
    num_stacks = 12
    stack_capacity = 7
    # Define the cost of moving a block to the top of each stack
    stack_costs = {0: 7, 1: 13, 2: 10, 3: 12, 4: 4, 5: 13, 6: 2, 7: 11, 8: 11, 9: 10, 10: 8, 11: 9}

    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if all stacks are sorted
        if all(stack == sorted(stack, key=lambda x: (x == 'Red', x == 'Black', x == 'Yellow', x == 'Green', x == 'Blue', x == 'Pink', x == 'White')) for stack in state):
            return actions

        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for i in range(num_stacks):
            for j in range(num_stacks):
                if i != j and state[i] and (not state[j] or state[i][-1] == state[j][-1]):
                    new_state = [list(stack) for stack in state]
                    new_state[j].append(new_state[i].pop())
                    new_state = tuple(tuple(stack) for stack in new_state)
                    new_cost = g + stack_costs[j]

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost, new_cost, actions + [(i, j)], new_state))

    return None


print(a_star())
