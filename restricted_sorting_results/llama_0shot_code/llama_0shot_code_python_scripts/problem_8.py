
import heapq

def restricted_sorting(stacks, costs):
    # Initialize the dictionary and the priority queue
    blocks_to_move = {}
    pq = []

    # Count the number of blocks of each color that need to be moved
    for i, stack in enumerate(stacks):
        for block in stack:
            if block not in blocks_to_move:
                blocks_to_move[block] = [0, 0, 0, 0, 0, 0]
            blocks_to_move[block][i] += 1

    # Add the blocks to the priority queue
    for block, counts in blocks_to_move.items():
        for i, count in enumerate(counts):
            if count > 0:
                heapq.heappush(pq, (costs[i], block, i))

    # Initialize the list of transfer pairs
    transfer_pairs = []

    # Move the blocks
    while pq:
        cost, block, from_stack = heapq.heappop(pq)
        to_stack = blocks_to_move[block].index(0)
        if stacks[to_stack]:
            to_stack = blocks_to_move[block].index(min(filter(None, blocks_to_move[block])))
        stacks[to_stack].append(block)
        blocks_to_move[block][from_stack] -= 1
        if blocks_to_move[block][from_stack] > 0:
            heapq.heappush(pq, (costs[from_stack], block, from_stack))
        transfer_pairs.append((from_stack, to_stack))

    return transfer_pairs

stacks = [['Blue', 'Green', 'Green', 'Red'], ['Yellow', 'Yellow', 'Green', 'Yellow'], [], [], [], ['Red', 'Blue', 'Red', 'Blue']]
costs = [3, 6, 1, 7, 2, 3]
print(restricted_sorting(stacks, costs))
