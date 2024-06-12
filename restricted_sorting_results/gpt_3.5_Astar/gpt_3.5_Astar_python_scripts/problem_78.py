
import heapq
import math


def a_star():
    # Define the initial state of the stacks
    initial_state = [[],
                     ['Blue', 'Pink', 'Red', 'Red', 'Yellow', 'White', 'Green'],
                     [],
                     [],
                     ['White', 'Black', 'Blue', 'Yellow', 'Yellow', 'Pink', 'White'],
                     ['Green', 'Pink', 'White', 'Blue', 'Pink', 'Red', 'Pink'],
                     ['Black', 'Green', 'Yellow', 'White', 'Yellow', 'Red', 'Blue'],
                     [],
                     ['Red', 'White', 'Black', 'Blue', 'Black', 'Yellow', 'Green'],
                     [],
                     ['Green', 'Black', 'Pink', 'Black', 'Red', 'Green', 'Blue'],
                     []]
    num_stacks = 12
    stack_capacity = 7
    # Define the cost of moving a block to the top of each stack
    costs = {0: 2, 1: 7, 2: 5, 3: 11, 4: 6, 5: 13, 6: 12, 7: 7, 8: 8, 9: 6, 10: 7, 11: 7}

    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the state is the goal state where all stacks are sorted
        if all(all(stack[i] == stack[i+1] for i in range(len(stack) - 1)) for stack in state if stack):
            return actions

        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for i in range(num_stacks):
            for j in range(num_stacks):
                if i != j and state[i] and (not state[j] or state[i][-1] == state[j][-1]):
                    new_state = [list(stack[:]) for stack in state]
                    new_state[j].append(new_state[i].pop())
                    new_state = tuple(tuple(stack) for stack in new_state)
                    new_cost = g + max(1, costs[i])

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, costs), new_cost, actions + [(i, j)], new_state))

    return None


def heuristic(state, costs):
    # The heuristic is the sum of the costs of moving the blocks to the correct stacks
    # This heuristic is admissible because it underestimates the cost to reach the goal state, as it assumes that all blocks can be moved to the correct stacks in one move
    # The heuristic is consistent because the cost of moving a block to the correct stack is always at least 1, which is the decrease in the heuristic value
    h = 0
    for stack in state:
        if stack:
            h += costs[stack[-1]]
    return h


print(a_star())
