
import heapq


def a_star():
    # Define the initial state of the stacks, with the leftmost item being the shade of the topmost block in each stack
    initial_state = [[], [], ['Blue', 'Yellow', 'Yellow', 'Yellow', 'Yellow', 'Black'], ['Red', 'Red', 'Blue', 'White', 'Blue', 'Black'], ['White', 'Green', 'Red', 'Black', 'Blue', 'Yellow'], [], ['White', 'Green', 'Green', 'White', 'Green', 'Green'], ['Black', 'Red', 'Red', 'Blue', 'White', 'Black'], [], []]
    num_stacks = 10
    stack_capacity = 6
    # Define the cost of moving one block to the top of each stack
    move_costs = {0: 7, 1: 7, 2: 8, 3: 5, 4: 8, 5: 10, 6: 5, 7: 5, 8: 4, 9: 8}


    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


    queue = [(0, 0, [], initial_state)]


    while queue:
        _, g, actions, state = heapq.heappop(queue)


        # Check if all stacks are sorted
        if all(all(stack[i] == stack[i+1] for i in range(len(stack) - 1)) for stack in state if stack):
            return actions


        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                # Check if the transfer is valid, ie the from_stack is not empty, the to_stack is not full, and the top block of the from_stack matches the shade of the top block of the to_stack or the to_stack is empty
                if state[from_stack] and (not state[to_stack] or state[from_stack][-1] == state[to_stack][-1]) and len(state[to_stack]) < stack_capacity:
                    # Generate the new state after the transfer
                    new_state = [list(stack) for stack in state]
                    new_state[from_stack].pop()
                    new_state[to_stack].append(state[from_stack][-1])
                    new_state = tuple(tuple(stack) for stack in new_state)
                    # Calculate the cost of the transfer
                    new_cost = g + move_costs[from_stack]
                  
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack, to_stack)], new_state))
    return None


print(a_star())
