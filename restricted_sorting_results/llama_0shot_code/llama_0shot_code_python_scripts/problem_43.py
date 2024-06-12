
import heapq

def restricted_sorting(stacks, costs):
    blocks = {}
    for i, stack in enumerate(stacks):
        for block in stack:
            if block not in blocks:
                blocks[block] = [0]*8
            blocks[block][i] += 1

    priority_queue = []
    for block, counts in blocks.items():
        heapq.heappush(priority_queue, (counts[::-1], block))

    result = []
    while priority_queue:
        counts, block = heapq.heappop(priority_queue)
        from_stack = counts.index(max(counts))
        to_stack = costs.index(min(costs[i] for i in range(8) if i != from_stack and counts[i] < 5))
        counts[from_stack] -= 1
        counts[to_stack] += 1
        heapq.heappush(priority_queue, (counts[::-1], block))
        result.append((from_stack, to_stack))

    return result

stacks = [['Green', 'Green', 'Red', 'Blue', 'Red'], ['Black', 'Red', 'Black', 'Red', 'Green'], ['Yellow', 'Green', 'Black', 'Black', 'Blue'], [], ['Blue', 'Yellow', 'Blue', 'Yellow', 'Yellow'], [], [], []]
costs = [5, 2, 8, 7, 5, 6, 1, 1]
print(restricted_sorting(stacks, costs))
