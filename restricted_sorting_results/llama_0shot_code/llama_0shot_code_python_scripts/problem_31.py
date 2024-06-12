
import heapq

def restricted_sorting(stacks, costs):
    # Initialize the dictionary to keep track of the blocks in each stack
    blocks = {i: [] for i in range(8)}
    # Initialize the priority queue to keep track of the stacks with the minimum cost
    queue = []
    # Initialize the dictionary to keep track of the shades in each stack
    shades = {i: set() for i in range(8)}
    # Initialize an empty list to keep track of the transfer pairs
    transfers = []

    # Iterate over the initial state of the stacks
    for i, stack in enumerate(stacks):
        # Add the blocks to the dictionary
        blocks[i] = stack
        # If the stack is not empty, add the stack to the priority queue with its cost as the priority
        if stack:
            heapq.heappush(queue, (costs[i], i))
            shades[i].add(stack[-1])

    # Start transferring the blocks
    while queue:
        # Pop the stack with the minimum cost
        _, src = heapq.heappop(queue)
        # Pop the top block from the stack
        block = blocks[src].pop()
        # Find a suitable stack to transfer the block to
        for i, stack in enumerate(blocks):
            if not stack or stack[-1] == block:
                # Transfer the block to the suitable stack
                blocks[i].append(block)
                # Update the dictionary and the priority queue
                heapq.heappush(queue, (costs[i], i))
                shades[i].add(block)
                # Add the transfer pair to the list
                transfers.append((src, i))
                break

    # Return the list of transfer pairs
    return transfers

stacks = [[], [], ['Yellow', 'Yellow', 'Green', 'Black', 'Red'], ['Black', 'Green', 'Black', 'Blue', 'Yellow'], ['Green', 'Blue', 'Yellow', 'Red', 'Blue'], [], [], ['Black', 'Red', 'Green', 'Red', 'Blue']]
costs = [7, 2, 1, 1, 9, 4, 2, 7]
print(restricted_sorting(stacks, costs))
