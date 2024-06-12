
import heapq


def a_star():
    # Define the initial state of the stacks
    initial_state = [['Black', 'Black', 'Yellow', 'Blue', 'Black', 'Black', 'Green'], [], ['Blue', 'Yellow', 'Green', 'Black', 'White', 'White', 'Blue'], ['Red', 'White', 'Pink', 'White', 'Pink', 'Green', 'Pink'], ['Green', 'Blue', 'Black', 'Green', 'Red', 'Green', 'Yellow'], [], [], ['Red', 'White', 'Blue', 'Yellow', 'Blue', 'White', 'Red'], ['Yellow', 'Yellow', 'Red', 'Pink', 'Red', 'Pink', 'Pink'], [], [], []]
    num_stacks = 12
    stack_capacity = 7
    # Define the cost of moving a block to the top of each stack
    stack_costs = {0: 10, 1: 7, 2: 7, 3: 7, 4: 9, 5: 3, 6: 8, 7: 5, 8: 4, 9: 10, 10: 7, 11: 7}
    # Define the goal state where all stacks are sorted
    goal_state = [['Black', 'Black', 'Black', 'Black', 'Black', 'Black', 'Black'], ['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'], ['Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green'], ['Pink', 'Pink', 'Pink', 'Pink', 'Pink', 'Pink', 'Pink'], ['Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red'], ['White', 'White', 'White', 'White', 'White', 'White', 'White'], ['Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow'], [], [], [], []]
  
    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                # Check if transferring a block from the 'from_stack' to the 'to_stack' is valid
                if from_stack != to_stack and state[from_stack] and (not state[to_stack] or state[from_stack][-1] == state[to_stack][-1]) and len(state[to_stack]) < stack_capacity:
                    new_state = [list(stack) for stack in state]
                    new_state[to_stack].append(new_state[from_stack].pop())
                    new_state = tuple(tuple(stack) for stack in new_state)
                    # Calculate the cost of the new state
                    new_cost = g + max(1, stack_costs[from_stack])

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack, to_stack)], new_state))

    return None


print(a_star())
