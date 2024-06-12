
import heapq


def a_star():
    # Define the initial state of the stacks
    initial_state = [[], [], ['Green', 'Red', 'Black', 'Blue', 'Blue'], ['Yellow', 'Blue', 'Blue', 'Green', 'Black'], ['Yellow', 'Yellow', 'Yellow', 'Red', 'Black'], [], [], ['Red', 'Green', 'Green', 'Red', 'Black']]
    num_stacks = 8
    stack_capacity = 5
    # Define the cost of moving a block to the top of each stack
    stack_costs = {0: 2, 1: 3, 2: 9, 3: 8, 4: 3, 5: 7, 6: 9, 7: 5}

    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if all stacks are sorted
        if all(all(state[i][j] == state[i][0] for j in range(len(state[i])) if state[i][j] != []) for i in range(num_stacks)):
            return actions

        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for i in range(num_stacks):
            for j in range(num_stacks):
                if i != j and state[i] and (not state[j] or state[j][-1] == state[i][0]) and len(state[j]) < stack_capacity:
                    new_state = [list(stack[:]) for stack in state]
                    new_state[j].append(new_state[i].pop(0))
                    new_state = tuple(tuple(stack) for stack in new_state)
                    new_cost = g + stack_costs[i]

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost, new_cost, actions + [(i, j)], new_state))

    return None


print(a_star())
