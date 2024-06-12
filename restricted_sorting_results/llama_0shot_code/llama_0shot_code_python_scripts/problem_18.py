
import heapq

def restricted_sorting(stacks, costs):
    # Initialize a priority queue with the blocks that need to be moved
    # The priority is based on the cost of moving the block to the respective stack
    priority_queue = []
    for i, stack in enumerate(stacks):
        for block in stack:
            heapq.heappush(priority_queue, (costs[i], i, block))

    # Maintain a dictionary to keep track of the number of blocks in each stack
    blocks_count = {i: len(stack) for i, stack in enumerate(stacks)}

    # List to store the transfer pairs
    transfer_pairs = []

    # Continue moving the blocks until the priority queue is empty
    while priority_queue:
        cost, from_stack, block = heapq.heappop(priority_queue)

        # Find the stack to move the block to
        to_stack = None
        for i, stack in enumerate(stacks):
            if i == from_stack or (stack and stack[-1] == block):
                if to_stack is None or costs[i] < costs[to_stack]:
                    to_stack = i

        # Move the block
        if to_stack is not None:
            if blocks_count[to_stack] < 3:
                stacks[to_stack].append(block)
                blocks_count[to_stack] += 1
                transfer_pairs.append((from_stack, to_stack))
            else:
                # If the stack is full, push the block back to the priority queue
                heapq.heappush(priority_queue, (cost, from_stack, block))

    return transfer_pairs

stacks = [[], [], ['Blue', 'Green', 'Yellow', 'Green'], ['Red', 'Yellow', 'Yellow', 'Green'], [], ['Red', 'Blue', 'Red', 'Blue']]
costs = [7, 6, 2, 7, 7, 4]
print(restricted_sorting(stacks, costs))
