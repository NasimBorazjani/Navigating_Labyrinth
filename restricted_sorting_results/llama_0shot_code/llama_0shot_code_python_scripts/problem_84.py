
import heapq

def restricted_sorting(stacks, costs):
    # Initialize the dictionary and the priority queue
    colors = {}
    queue = []
    for i, stack in enumerate(stacks):
        if stack:
            color = stack[-1]
            colors[i] = color
            heapq.heappush(queue, (costs[i], i))

    # Initialize the list of transfer pairs
    transfer_pairs = []

    # Sort the blocks
    while queue:
        cost, src = heapq.heappop(queue)
        if colors[src] in colors:
            dest = colors[colors[src]]
            transfer_pairs.append((src, dest))
            colors[dest].append(colors[src].pop())
            if not colors[src]:
                del colors[src]
        else:
            dest = colors[colors[src]] = []
            transfer_pairs.append((src, dest))
            dest.append(colors[src].pop())

    return transfer_pairs

stacks = [[], [], [], [], ['Pink', 'Red', 'Green', 'Pink', 'White', 'Blue', 'Yellow'], [], ['Yellow', 'White', 'Yellow', 'Blue', 'Yellow', 'Black', 'White'], ['Black', 'Green', 'Pink', 'Pink', 'Green', 'Yellow', 'Green'], ['White', 'Blue', 'Red', 'Red', 'Red', 'Yellow', 'Black'], ['Black', 'Blue', 'Blue', 'Pink', 'Red', 'White', 'Green'], [], ['Blue', 'Black', 'Black', 'White', 'Red', 'Green', 'Pink']]
costs = {0: 12, 1: 3, 2: 11, 3: 5, 4: 11, 5: 13, 6: 2, 7: 2, 8: 12, 9: 4, 10: 2, 11: 10}

print(restricted_sorting(stacks, costs))
