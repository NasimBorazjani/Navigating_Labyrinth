
import heapq


def a_star():
    # Define the initial state of the stacks
    initial_state = [['Red', 'Pink', 'Pink', 'Pink', 'Red', 'Black', 'Pink'], [], ['Green', 'Green', 'Blue', 'White', 'Yellow', 'Blue', 'Blue'], [], ['Green', 'Blue', 'White', 'Red', 'Blue', 'Black', 'Red'], ['Pink', 'White', 'Yellow', 'Black', 'Yellow', 'Green', 'White'], [], ['Red', 'Green', 'Black', 'White', 'Green', 'Red', 'Black'], [], [], ['Yellow', 'White', 'Yellow', 'Blue', 'Black', 'Yellow', 'Pink'], []]
    num_stacks = 12
    stack_capacity = 7
    # Define the cost of moving a block to the top of each stack
    costs = {0: 10, 1: 4, 2: 5, 3: 4, 4: 7, 5: 3, 6: 11, 7: 5, 8: 9, 9: 3, 10: 11, 11: 2}

    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if all stacks are sorted
        if all(stack == sorted(stack, key=lambda x: (x == 'Red', x == 'Pink', x == 'White', x == 'Yellow', x == 'Green', x == 'Blue', x == 'Black')) for stack in state):
            return actions

        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for i in range(num_stacks):
            for j in range(num_stacks):
                if i != j and state[i] and (not state[j] or state[i][-1] == state[j][-1]):
                    new_state = [list(stack) for stack in state]
                    new_state[j].append(new_state[i].pop())
                    new_state = tuple(tuple(stack) for stack in new_state)
                    new_cost = g + max(1, costs[i])

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost, new_cost, actions + [(i, j)], new_state))

    return None


print(a_star())
