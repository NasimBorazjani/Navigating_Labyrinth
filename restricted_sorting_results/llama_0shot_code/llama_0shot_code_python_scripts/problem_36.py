
import heapq

def restricted_sorting(stacks, costs):
    # Create a dictionary to store the blocks and their counts
    blocks_counts = {}
    for i, stack in enumerate(stacks):
        for block in stack:
            if block not in blocks_counts:
                blocks_counts[block] = [0]*8
            blocks_counts[block][i] += 1

    # Create a priority queue to get the stack with the least cost
    queue = [(-costs[i], i) for i in range(8)]

    # List to store the transfer pairs
    transfer_pairs = []

    # Iterate over each block
    for block, counts in blocks_counts.items():
        while any(counts):
            # Get the stack with the least cost
            cost, src = heapq.heappop(queue)

            # Find the destination stack
            dest = None
            for i in range(8):
                if counts[i]:
                    dest = i
                    break

            # If the destination stack is full, move a block from it
            if sum(counts[i] for i in range(8) if i != dest and i != src) == 0:
                for i in range(8):
                    if i != src and counts[i]:
                        dest = i
                        break

            # Move the block
            counts[src] -= 1
            counts[dest] += 1
            transfer_pairs.append((src, dest))

            # Update the cost of the source stack
            heapq.heappush(queue, (-costs[src]-counts[src], src))

    return transfer_pairs

stacks = [['Blue', 'Yellow', 'Yellow', 'Green', 'Black'], [], [], [], ['Blue', 'Red', 'Black', 'Yellow', 'Green'], ['Black', 'Red', 'Green', 'Blue', 'Red'], ['Green', 'Yellow', 'Black', 'Red', 'Blue'], []]
costs = [4, 4, 7, 1, 8, 8, 8, 4]

print(restricted_sorting(stacks, costs))
