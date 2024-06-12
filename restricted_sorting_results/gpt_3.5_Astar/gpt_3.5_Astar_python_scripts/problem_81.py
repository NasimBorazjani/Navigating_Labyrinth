
import heapq
import math


def a_star():
    # Define the initial state of the stacks, with each stack represented as a list of blocks
    initial_state = [[],
                     ['White', 'Black', 'Yellow', 'Black', 'Green', 'Blue', 'Pink'],
                     ['Black', 'Red', 'Yellow', 'White', 'Yellow', 'Black', 'Green'],
                     ['Yellow', 'White', 'Green', 'White', 'White', 'Black', 'Blue'],
                     ['Blue', 'Pink', 'Red', 'Pink', 'Green', 'Yellow', 'Black'],
                     ['White', 'Red', 'Pink', 'Blue', 'Blue', 'Pink', 'Green'],
                     [],
                     [],
                     [],
                     ['Red', 'Pink', 'Red', 'Blue', 'Red', 'Green', 'Yellow'],
                     [],
                     []]
    num_stacks = 12
    stack_capacity = 7
    # Define the cost of moving a block to the top of each stack
    stack_costs = {0: 5, 1: 3, 2: 3, 3: 4, 4: 2, 5: 2, 6: 12, 7: 9, 8: 5, 9: 11, 10: 11, 11: 10}

    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state, where all stacks are sorted
        if all(all(stack[i] == stack[i+1] for i in range(len(stack) - 1)) for stack in state if stack):
            return actions

        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for i in range(num_stacks):
            for j in range(num_stacks):
                if i != j and state[i] and (not state[j] or state[i][-1] == state[j][-1]):
                    new_state = [list(stack[:]) for stack in state]
                    new_state[j].append(new_state[i].pop())
                    new_state = tuple(tuple(stack) for stack in new_state)
                    new_cost = g + max(1, stack_costs[i])

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        h = heuristic(new_state, stack_costs)
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [(i, j)], new_state))

    return None


def heuristic(state, stack_costs):
    # The heuristic is the sum of the costs of moving the blocks to the correct stacks
    # This heuristic is admissible because it underestimates the cost to reach the goal state, as it assumes that all blocks can be moved to the correct stacks in one move
    # The heuristic is consistent because the cost of moving a block to a stack is always at least 1, which is the decrease in the heuristic value when moving a block to the correct stack
    h = 0
    for stack in state:
        if stack:
            h += stack_costs[0] if stack[-1] != 'White' else 0
            h += stack_costs[1] if stack[-1] != 'Black' else 0
            h += stack_costs[2] if stack[-1] != 'Yellow' else 0
            h += stack_costs[3] if stack[-1] != 'Green' else 0
            h += stack_costs[4] if stack[-1] != 'Blue' else 0
            h += stack_costs[5] if stack[-1] != 'Pink' else 0
            h += stack_costs[6] if stack[-1] != 'Red' else 0
    return h


print(a_star())
