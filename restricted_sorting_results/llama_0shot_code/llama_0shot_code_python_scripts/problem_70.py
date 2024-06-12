
import heapq

def restricted_sorting(stacks, costs):
    # Initialize the dictionary to keep track of the number of blocks of each color in each stack
    color_counts = {i: {} for i in range(len(stacks))}
    for i, stack in enumerate(stacks):
        for block in stack:
            if block in color_counts[i]:
                color_counts[i][block] += 1
            else:
                color_counts[i][block] = 1

    # Initialize the priority queue with the stacks that are not empty
    queue = []
    for i in range(len(stacks)):
        if stacks[i]:
            heapq.heappush(queue, (costs[i], i))

    # Initialize the list to store the transfer pairs
    transfer_pairs = []

    while queue:
        cost, src = heapq.heappop(queue)
        if stacks[src]:
            block = stacks[src].pop()
            if color_counts[src][block] > 1:
                color_counts[src][block] -= 1
            else:
                del color_counts[src][block]

            # Find the destination stack with the same color
            dest = None
            for i in range(len(stacks)):
                if i != src and (block in color_counts[i] and color_counts[i][block] < 5):
                    dest = i
                    break

            # If the destination stack is full, find the next least costly stack
            if dest is None:
                for i in range(len(stacks)):
                    if i != src and len(stacks[i]) < 5:
                        dest = i
                        break

            # Move the block to the destination stack
            stacks[dest].append(block)
            if block in color_counts[dest]:
                color_counts[dest][block] += 1
            else:
                color_counts[dest][block] = 1

            # Push the destination stack to the priority queue
            heapq.heappush(queue, (costs[dest], dest))

            # Add the transfer pair to the list
            transfer_pairs.append((src, dest))

    return transfer_pairs

stacks = [['Red', 'Green', 'Blue', 'Yellow', 'Yellow', 'Blue'], [], [], [], ['White', 'Black', 'White', 'Red', 'White', 'Blue'], ['Black', 'Green', 'Red', 'Black', 'Green', 'Yellow'], [], ['Red', 'White', 'Yellow', 'Black', 'Green', 'White'], [], ['Blue', 'Blue', 'Black', 'Green', 'Red', 'Yellow']]
costs = [11, 5, 9, 5, 2, 2, 6, 6, 6, 2]
print(restricted_sorting(stacks, costs))
