
import heapq

def restricted_sorting(stacks, costs):
    # Initialize a priority queue with the cost of moving a block to the top of each stack.
    priority_queue = [(cost, i) for i, cost in enumerate(costs)]
    heapq.heapify(priority_queue)

    # Initialize a dictionary to keep track of the number of blocks of each color in each stack.
    blocks_count = {i: len(stack) for i, stack in enumerate(stacks)}

    # Initialize a dictionary to keep track of the color of the top block in each stack.
    top_block = {i: stack[-1] if stack else None for i, stack in enumerate(stacks)}

    # Initialize a dictionary to keep track of the number of blocks of each color.
    color_count = {}
    for stack in stacks:
        for color in stack:
            if color in color_count:
                color_count[color] += 1
            else:
                color_count[color] = 1

    # Initialize an empty list to store the transfer pairs.
    transfer_pairs = []

    # While there are still blocks that need to be sorted:
    while any(count > 0 for count in color_count.values()):
        # Pop the stack with the highest priority from the priority queue.
        cost, from_stack = heapq.heappop(priority_queue)

        # If the stack is empty, continue to the next stack.
        if blocks_count[from_stack] == 0:
            continue

        # Find the stack with the same color block or an empty stack with the lowest cost.
        to_stack = None
        for i, (stack_cost, stack_index) in enumerate(priority_queue):
            if top_block[stack_index] == top_block[from_stack] or (stack_cost == min(costs) and blocks_count[stack_index] < 4):
                to_stack = stack_index
                break

        # If no such stack is found, continue to the next stack.
        if to_stack is None:
            continue

        # Move the block from the stack with the highest priority to the stack found in step 3b.
        transfer_pairs.append((from_stack, to_stack))
        blocks_count[from_stack] -= 1
        blocks_count[to_stack] += 1
        color_count[top_block[from_stack]] -= 1
        if top_block[to_stack] is None or top_block[to_stack] == top_block[from_stack]:
            top_block[to_stack] = top_block[from_stack]
        else:
            top_block[from_stack] = stacks[from_stack][blocks_count[from_stack] - 1]

        # If the stack found in step 3b is full, remove it from the priority queue.
        if blocks_count[to_stack] == 4:
            heapq.heappop(priority_queue)

        # If the stack found in step 3b is not full, update its cost in the priority queue.
        else:
            heapq.heapify(priority_queue)

    # Return the list of transfer pairs.
    return transfer_pairs

stacks = [[], ['Green', 'Red', 'Yellow', 'Blue'], [], ['Red', 'Blue', 'Yellow', 'Green'], ['Red', 'Yellow', 'Blue', 'Green'], []]
costs = [4, 2, 5, 2, 4, 1]
print(restricted_sorting(stacks, costs))
