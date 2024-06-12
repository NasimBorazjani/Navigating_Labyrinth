
import heapq


def a_star():
    # Define the initial state of the stacks, where each stack is represented as a list of blocks
    initial_state = [[], ['Blue', 'Yellow', 'Pink', 'Green', 'Pink', 'Red', 'Red'], [], ['Pink', 'White', 'Pink', 'Black', 'White', 'Black', 'Pink'], ['Yellow', 'Green', 'White', 'Red', 'Yellow', 'Yellow', 'Red'], ['Green', 'Pink', 'White', 'Blue', 'Red', 'White', 'Red'], [], [], ['Blue', 'Blue', 'Yellow', 'Blue', 'Black', 'Blue', 'Green'], ['Yellow', 'Black', 'Black', 'White', 'Green', 'Green', 'Black'], [], []]
    num_stacks = 12
    stack_capacity = 7
    # Define the cost of moving a block to the top of each stack
    stack_costs = {0: 10, 1: 8, 2: 6, 3: 4, 4: 11, 5: 5, 6: 11, 7: 5, 8: 7, 9: 7, 10: 10, 11: 10}
  
    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if all stacks are sorted
        if all(sorted(stack) == stack for stack in state if stack):
            return actions

        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                if from_stack != to_stack and state[from_stack] and (not state[to_stack] or state[from_stack][-1] == state[to_stack][-1]):
                    new_state = [list(stack) for stack in state]
                    block = new_state[from_stack].pop()
                    new_state[to_stack].append(block)
                    new_state = tuple(tuple(stack) for stack in new_state)
                    new_cost = g + max(1, stack_costs[from_stack])

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack, to_stack)], new_state))
    return None


print(a_star())
