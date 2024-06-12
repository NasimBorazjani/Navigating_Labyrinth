
import heapq

def restricted_sorting(stacks, costs):
    # Create a dictionary to store the blocks and their counts
    blocks_count = {}
    for i, stack in enumerate(stacks):
        for block in stack:
            if block in blocks_count:
                blocks_count[block] += 1
            else:
                blocks_count[block] = 1

    # Create a priority queue to store the blocks in the order of their counts
    blocks_queue = [(-count, block) for block, count in blocks_count.items()]
    heapq.heapify(blocks_queue)

    # List to store the transfer pairs
    transfer_pairs = []

    while blocks_queue:
        count, block = heapq.heappop(blocks_queue)
        moved = False
        for i, stack in enumerate(stacks):
            if not stack or stack[-1] == block:
                # Move the block to the stack if it's empty or the top block is of the same color
                stacks[i].append(block)
                transfer_pairs.append((blocks.index(block), i))
                moved = True
                break
        if not moved:
            # If no suitable stack is found, push the block back to the queue
            heapq.heappush(blocks_queue, (count, block))

    # Calculate the total cost
    total_cost = sum(costs[i] for i, _ in transfer_pairs)

    return transfer_pairs, total_cost

stacks = [['Yellow', 'Green', 'Green', 'Black', 'Black'], [], ['Yellow', 'Green', 'Black', 'Green', 'Red'], ['Red', 'Black', 'Blue', 'Blue', 'Yellow'], [], [], ['Red', 'Blue', 'Yellow', 'Blue', 'Red'], []]
costs = [6, 1, 8, 8, 1, 6, 4, 1]

transfer_pairs, total_cost = restricted_sorting(stacks, costs)
print(transfer_pairs)
print(total_cost)
